---
layout: tailwind
permalink: /matching/
show_reading_time: false
menu: nav/home.html
---

<head>
  <meta charset="UTF-8">
  <title>Biotech Matching Game</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      background: #f9f9fb;
      margin: 0;
      padding: 40px;
    }
    h1 {
      margin-bottom: 20px;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 15px;
      max-width: 900px;
      width: 100%;
    }
    .card {
      background: white;
      padding: 20px;
      text-align: center;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      cursor: pointer;
      transition: transform 0.2s, background 0.3s;
      color: black;
    }
    .card:hover {
      transform: scale(1.02);
    }
    .matched {
      background-color: #d1ffd6;
      pointer-events: none;
      opacity: 0.6;
    }
    .selected {
      border: 2px solid #4A90E2;
    }
    .modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 1000;
    }
    .modal-content {
      background: white;
      padding: 30px;
      border-radius: 12px;
      text-align: center;
      max-width: 500px;
      box-shadow: 0 8px 16px rgba(0,0,0,0.2);
      color: black;
    }
    .modal-content h2 {
      margin-top: 0;
    }
    .modal-content button {
      margin-top: 20px;
      padding: 10px 20px;
      background: #4A90E2;
      color: white;
      border: none;
      border-radius: 8px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>
<!-- Instruction Modal -->
  <div id="instruction-modal" class="modal">
    <div class="modal-content">
      <h2>How to Play</h2>
      <p>Match each biotechnology term with its correct definition. Click one card to select a term, then another card to select a definition. If they match, they disappear. Keep matching until all pairs are gone!</p>
      <button onclick="closeModal()">Start Game</button>
    </div>
  </div>
  <h1>Match the Biotech Term to its Definition</h1>
  <div class="grid" id="card-grid"></div>

  <script>
    const pairs = [
      { term: "DNA", definition: "A molecule that carries genetic instructions." },
      { term: "Gene", definition: "A segment of DNA that determines a trait." },
      { term: "Genome", definition: "All the genetic material in an organism." },
      { term: "Insulin", definition: "A hormone produced to regulate blood sugar." },
      { term: "Bacteria", definition: "Microscopic organisms used to produce medicine." },
      { term: "Mutation", definition: "A change in the DNA sequence." },
      { term: "Enzyme", definition: "A protein that speeds up chemical reactions." },
      { term: "CRISPR", definition: "A modern tool for precise gene editing." }
    ];

    let selectedCards = [];
    const grid = document.getElementById("card-grid");

    function shuffleArray(array) {
      for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
      }
    }

    function renderCards() {
      const allCards = [];
      pairs.forEach((pair, index) => {
        allCards.push({ type: "term", text: pair.term, id: index });
        allCards.push({ type: "definition", text: pair.definition, id: index });
      });
      shuffleArray(allCards);

      allCards.forEach(card => {
        const div = document.createElement("div");
        div.classList.add("card");
        div.textContent = card.text;
        div.dataset.id = card.id;
        div.dataset.type = card.type;
        div.addEventListener("click", handleCardClick);
        grid.appendChild(div);
      });
    }

    function handleCardClick(e) {
      const card = e.currentTarget;
      if (card.classList.contains("matched") || selectedCards.includes(card)) return;

      card.classList.add("selected");
      selectedCards.push(card);

      if (selectedCards.length === 2) {
        const [card1, card2] = selectedCards;
        if (card1.dataset.id === card2.dataset.id && card1.dataset.type !== card2.dataset.type) {
          card1.classList.add("matched");
          card2.classList.add("matched");
        }
        setTimeout(() => {
          selectedCards.forEach(c => c.classList.remove("selected"));
          selectedCards = [];
        }, 700);
      }
    }

    renderCards();
window.onload = function () {
  document.getElementById("instruction-modal").style.display = "flex";
};

function closeModal() {
  document.getElementById("instruction-modal").style.display = "none";
} 
  </script>

</body>
</html>
