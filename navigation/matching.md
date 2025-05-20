---
layout: tailwind
permalink: /matching-game/
show_reading_time: false
menu: nav/home.html
---

<head>
  <meta charset="UTF-8" />
  <title>Biotech Matching Game</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
  :root {
    --navy:rgb(105, 142, 177);
  }
  body {
    font-family: 'Inter', sans-serif;
    background: rgb(201, 204, 216);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 40px 20px;
    margin: 0;
    color: var(--navy);
  }
  h1, h2, h3, h4, h5, h6,
  p, label, select, .card,
  .modal-content, .timer {
    color: var(--navy);
  }
  h1 {
    font-size: 1.875rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1rem;
    max-width: 960px;
    width: 100%;
  }
  .card {
    background: white;
    padding: 1.25rem;
    text-align: center;
    border-radius: 0.75rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
    cursor: pointer;
    transition: transform 0.2s, background 0.3s, box-shadow 0.3s;
    font-weight: 500;
  }
  .card:hover {
    transform: scale(1.025);
    box-shadow: 0 6px 14px rgba(0, 0, 0, 0.1);
  }
  .matched {
    pointer-events: none;
  }
  .selected {
  border: 2px solid #3b82f6;
  background-color: rgb(227, 230, 240); 
}
  @keyframes fadeOut {
    from {
      opacity: 1;
      transform: scale(1);
    }
    to {
      opacity: 0;
      transform: scale(0.9);
    }
  }
  .fade-out {
    animation: fadeOut 0.4s forwards;
  }
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 10, 24, 0.7);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 50;
  }
  .modal-content {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    max-width: 480px;
    width: 90%;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
  }
  .modal-content h2 {
    margin-top: 0;
    font-size: 1.5rem;
    font-weight: 600;
  }
  .modal-content p {
    font-size: 1rem;
    margin: 1rem 0;
  }
  .modal-content button {
    margin: 0.5rem;
    padding: 0.75rem 1.5rem;
    background: #3b82f6;
    color: white;
    border: none;
    border-radius: 0.5rem;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.2s;
  }
  .modal-content button:hover {
    background: #2563eb;
  }
  .timer {
    font-weight: 600;
    font-size: 1.125rem;
    margin-bottom: 1rem;
  }
  select {
    padding: 0.5rem 1rem;
    font-size: 1rem;
    border-radius: 0.5rem;
    border: 1px solid #d1d5db;
    outline: none;
    margin-left: 0.5rem;
    background: white;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    transition: border 0.2s;
  }
  select:focus {
    border-color: #3b82f6;
  }
  label {
    font-weight: 500;
    margin-right: 0.5rem;
  }
  @media (max-width: 480px) {
    .modal-content {
      padding: 1.5rem;
    }
    .modal-content h2 {
      font-size: 1.25rem;
    }
  }
</style>

</head>

<body>
  <!-- Instruction Modal -->
  <div id="instruction-modal" class="modal">
    <div class="modal-content">
      <h2>How to Play</h2>
      <p>
        Match each biotechnology term with its correct definition. Click one card to select a term, then another card to select a definition. If they match, they disappear. Keep matching until all pairs are gone. When you finish the game, you can choose to keep playing or try some interesting quizzes!
      </p>
      <button onclick="closeModal()">Start Game</button>
    </div>
  </div>

  <!-- Victory Modal -->
<div id="victory-modal" class="modal" style="display: none;">
  <div class="modal-content">
    <h2>Congratulations!🎉</h2>
    <p id="victory-time">You completed the game in X seconds!</p>
    <p>Beat your time by hitting "Play Again" or take a Career/College Quiz</p>
    <button onclick="restartGame()">Play Again</button>
    <button onclick="window.location.href='/illumina_dna/career/'">Take Career Quiz</button>
    <button onclick="window.location.href='/illumina_dna/college/'">Take College Quiz</button>
  </div>
</div>
  <h1>Match the Biotech Term to its Definition</h1>
  <div class="timer" id="timer">Time: 0s</div>

  <div style="margin-bottom: 20px;">
    <label for="difficulty">Select Difficulty:</label>
    <select id="difficulty" onchange="loadGame()">
      <option value="beginner">Beginner</option>
      <option value="intermediate">Intermediate</option>
      <option value="advanced">Advanced</option>
    </select>
  </div>

  <div class="grid" id="card-grid"></div>

  <script>
    const API_BASE_URL = "http://127.0.0.1:8504";
    let selectedCards = [];
    let matchedCount = 0;
    let totalPairs = 0;
    let timerInterval;
    let secondsElapsed = 0;
    const grid = document.getElementById("card-grid");

    function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }

    function startTimer() {
      clearInterval(timerInterval);
      secondsElapsed = 0;
      document.getElementById("timer").textContent = `Time: 0s`;
      timerInterval = setInterval(() => {
        secondsElapsed++;
        document.getElementById("timer").textContent = `Time: ${secondsElapsed}s`;
      }, 1000);
    }

    function stopTimer() {
      clearInterval(timerInterval);
    }

    function renderCards(pairs) {
      grid.innerHTML = "";
      selectedCards = [];
      matchedCount = 0;
      totalPairs = pairs.length;

      shuffleArray(pairs); // Shuffle the order of the pairs themselves

      const allCards = [];
      pairs.forEach((pair, index) => {
        allCards.push({ type: "term", text: pair.term, id: index });
        allCards.push({ type: "definition", text: pair.definition, id: index });
      });

      shuffleArray(allCards);

      allCards.forEach((card) => {
        const div = document.createElement("div");
        div.classList.add("card");
        div.textContent = card.text;
        div.dataset.id = card.id;
        div.dataset.type = card.type;
        div.addEventListener("click", handleCardClick);
        grid.appendChild(div);
      });

      startTimer();
    }

    function handleCardClick(e) {
      const card = e.currentTarget;
      if (card.classList.contains("matched") || selectedCards.includes(card)) return;

      card.classList.add("selected");
      selectedCards.push(card);

      if (selectedCards.length === 2) {
        const [card1, card2] = selectedCards;

        if (card1.dataset.id === card2.dataset.id && card1.dataset.type !== card2.dataset.type) {
          card1.classList.add("matched", "fade-out");
          card2.classList.add("matched", "fade-out");

          let animationsDone = 0;
          const removeCards = () => {
            card1.remove();
            card2.remove();
            matchedCount++;
            if (matchedCount === totalPairs) {
              stopTimer();
              showVictoryModal();
            }
          };

          [card1, card2].forEach((card) =>
            card.addEventListener("animationend", () => {
              animationsDone++;
              if (animationsDone === 2) removeCards();
            }, { once: true })
          );
        }

        setTimeout(() => {
          selectedCards.forEach((c) => c.classList.remove("selected"));
          selectedCards = [];
        }, 700);
      }
    }

    function showVictoryModal() {
      document.getElementById("victory-time").textContent = `You completed the game in ${secondsElapsed} seconds!`;
      document.getElementById("victory-modal").style.display = "flex";
    }

    function loadGame() {
      const level = document.getElementById("difficulty").value;
      fetch(`${API_BASE_URL}/api/pairs?level=${level}`)
        .then((response) => {
          if (!response.ok) throw new Error("Failed to load pairs.");
          return response.json();
        })
        .then((pairs) => renderCards(pairs))
        .catch((err) => {
          console.error("Error loading pairs:", err);
          grid.innerHTML = "<p>Could not load game data.</p>";
        });
    }

    function closeModal() {
      document.getElementById("instruction-modal").style.display = "none";
    }

    window.onload = function () {
      document.getElementById("instruction-modal").style.display = "flex";
      loadGame();
    };
    function restartGame() {
  document.getElementById("victory-modal").style.display = "none";
  startTimer();
  loadGame();
  }
  </script>
</body>
