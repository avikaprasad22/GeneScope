---
layout: tailwind
title: Trivia Game
permalink: /trivia/
show_reading_time: false
menu: nav/home.html
---

<div class="pt-6"></div>

<div class="trivia-container space-y-6 p-6 bg-blue-100 rounded-2xl shadow-2xl max-w-2xl mx-auto font-[Comic Sans MS,cursive,sans-serif]">
  <h2 class="text-3xl font-extrabold text-blue-800 text-center">🧬 Genetics Trivia Challenge 🧠</h2>

  <div class="text-center space-y-4">
    <button id="showInstructionsButton"
      class="bg-blue-400 text-white px-4 py-2 rounded-full hover:bg-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-300 shadow-md transition duration-300">
      ℹ️ How to Play
    </button>
    <div class="flex justify-center items-center space-x-4">
      <label for="difficultySelect" class="font-semibold text-blue-800">Select Difficulty:</label>
      <select id="difficultySelect" class="rounded-md px-3 py-2 border border-blue-400 focus:outline-none focus:ring-2 focus:ring-blue-300">
        <option value="easy" selected>Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
    </div>
    <button id="startGameButton"
      class="bg-blue-500 text-white px-6 py-3 rounded-full hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-300 shadow-md transition duration-300">
      Start 30‑Second Challenge
    </button>
  </div>

  <div id="gameContainer" class="hidden space-y-4">
    <h3 id="questionText" class="text-xl font-semibold text-blue-900 text-center"></h3>
    <div id="answersContainer" class="grid grid-cols-2 gap-4"></div>
    <div class="flex justify-between px-2">
      <p class="text-blue-800">⏳ Time Left: <span id="timer" class="font-bold text-blue-600">30</span>s</p>
      <p class="text-blue-800">🌟 Score: <span id="score" class="font-bold text-blue-700">0</span></p>
    </div>
  </div>

  <button id="playAgainButton"
          class="hidden bg-blue-400 text-white px-6 py-3 rounded-full hover:bg-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-300 shadow-md transition duration-300">
     Play Again
  </button>

  <div id="leaderboardContainer" class="space-y-2 max-h-64 overflow-y-auto bg-white p-4 rounded-xl shadow-inner">
    <h3 class="text-xl font-semibold text-blue-900 text-center">🏆 Leaderboard</h3>
    <div class="text-center mb-2 flex flex-col sm:flex-row justify-center items-center space-y-2 sm:space-y-0 sm:space-x-4">
      <label for="filterDifficulty" class="text-sm font-medium text-blue-800 mr-2">Filter by Difficulty:</label>
      <select id="filterDifficulty" class="rounded px-2 py-1 border border-blue-300 focus:outline-none">
        <option value="all">All</option>
        <option value="easy">Easy</option>
        <option value="medium">Medium</option>
        <option value="hard">Hard</option>
      </select>
      <input
        type="text"
        id="searchUsername"
        placeholder="Search username..."
        class="rounded px-2 py-1 border border-blue-300 focus:outline-none max-w-xs"
        aria-label="Search leaderboard by username"
      />
    </div>
    <table class="w-full table-auto border-collapse">
      <thead>
        <tr class="bg-blue-200">
          <th class="border px-3 py-2 text-blue-900">Username</th>
          <th class="border px-3 py-2 text-blue-900">Score</th>
          <th class="border px-3 py-2 text-blue-900">Difficulty</th>
        </tr>
      </thead>
      <tbody id="leaderboardBody" class="text-blue-800"></tbody>
    </table>
  </div>

  <p id="message" class="text-red-500 text-center pt-2"></p>
</div>

<div id="instructionsModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 hidden">
  <div class="bg-white rounded-2xl p-6 max-w-xl mx-4 max-h-[80vh] overflow-y-auto shadow-2xl relative">
    <button id="closeInstructions" class="absolute top-3 right-3 text-gray-600 hover:text-gray-900 text-xl font-bold">&times;</button>
    <h3 class="text-2xl font-bold text-blue-800 mb-4 text-center">How to Play & Key Terms</h3>
    <div class="space-y-4 text-blue-900 text-sm leading-relaxed">
      <p><strong>Objective:</strong> Answer as many genetics trivia questions correctly within 30 seconds to earn a high score!</p>
      <p><strong>Gameplay:</strong> Select the correct answer from multiple choices. Each correct answer increases your score by 1.</p>
      <p><strong>Difficulty Levels:</strong> Choose from Easy, Medium, or Hard questions before starting the game.</p>
      <p><strong>Timer:</strong> You have 30 seconds per challenge. Try to answer quickly and accurately!</p>
      <hr class="my-3 border-blue-300" />
      <h4 class="font-semibold text-blue-700">Key Terms:</h4>
      <ul class="list-disc pl-5 space-y-1">
        <li><strong>Gene:</strong> A unit of heredity made up of DNA that codes for a specific trait.</li>
        <li><strong>Chromosome:</strong> Structures in cells that contain genes.</li>
        <li><strong>Allele:</strong> Different versions of a gene.</li>
        <li><strong>DNA:</strong> The molecule that carries genetic information.</li>
        <li><strong>Mutation:</strong> A change in the DNA sequence.</li>
      </ul>
    </div>
  </div>
</div>

<script type="module">
  import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

  let currentQuestions = [];
  let allScores = [];

  async function getUserId() {
    const res = await fetch(pythonURI + '/api/id', fetchOptions);
    return (await res.json()).id;
  }

  async function fetchGameQuestions(difficulty) {
    const url = `${pythonURI}/api/get_questions?difficulty=${difficulty}`;
    const res = await fetch(url, fetchOptions);
    if (!res.ok) throw new Error('Failed to load questions');
    return await res.json();
  }

  async function updateLeaderboard() {
    const topRes = await fetch(pythonURI + '/api/scoreboard/top', fetchOptions);
    allScores = await topRes.json();
    renderLeaderboard('all', '');
  }

  // Updated renderLeaderboard with searchTerm param
  function renderLeaderboard(filter, searchTerm) {
    const tbody = document.getElementById('leaderboardBody');
    tbody.innerHTML = '';
    searchTerm = searchTerm?.toLowerCase() || '';
    const filtered = allScores.filter(entry => {
      const matchesDifficulty = filter === 'all' || entry.difficulty === filter;
      const matchesSearch = entry.username.toLowerCase().includes(searchTerm);
      return matchesDifficulty && matchesSearch;
    });
    filtered.forEach(entry => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td class="border px-2 py-1">${entry.username}</td>
        <td class="border px-2 py-1">${entry.score}</td>
        <td class="border px-2 py-1 capitalize">${entry.difficulty}</td>
      `;
      tbody.appendChild(row);
    });
  }

  function startChallenge(questions) {
    let idx = 0, score = 0;
    const duration = 30;
    let timeLeft = duration, timerId;
    const startBtn = document.getElementById('startGameButton');
    const gameCtn = document.getElementById('gameContainer');
    const qText = document.getElementById('questionText');
    const ansCtn = document.getElementById('answersContainer');
    const timerEl = document.getElementById('timer');
    const scoreEl = document.getElementById('score');
    const playAgainBtn = document.getElementById('playAgainButton');
    const difficulty = document.getElementById('difficultySelect').value;

    scoreEl.textContent = '0';
    timerEl.textContent = duration;
    startBtn.classList.add('hidden');
    playAgainBtn.classList.add('hidden');
    gameCtn.classList.remove('hidden');

    function showQuestion() {
      if (idx >= questions.length) idx = 0;
      const q = questions[idx++];
      qText.textContent = q.question;
      ansCtn.innerHTML = '';

      const opts = [...q.options].sort(() => Math.random() - 0.5);
      opts.forEach(opt => {
        const btn = document.createElement('button');
        btn.className = 'bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-400 focus:outline-none focus:ring-2 focus:ring-blue-300 transition-all';
        btn.textContent = opt;

        btn.addEventListener('click', () => {
          ansCtn.querySelectorAll('button').forEach(b => b.disabled = true);
          if (opt === q.correct_answer) {
            btn.classList.replace('bg-blue-500', 'bg-green-500');
            btn.classList.add('animate-pulse');
            score++;
            scoreEl.textContent = score;
          } else {
            btn.classList.replace('bg-blue-500', 'bg-red-500');
            btn.classList.add('animate-pulse');
          }
          setTimeout(() => {
            btn.classList.remove('animate-pulse');
            updateLeaderboard();
            showQuestion();
          }, 800);
        });

        ansCtn.appendChild(btn);
      });
    }

    function tick() {
      timeLeft--;
      timerEl.textContent = timeLeft;
      if (timeLeft <= 0) {
        clearInterval(timerId);
        endChallenge();
      }
    }

    async function endChallenge() {
      ansCtn.querySelectorAll('button').forEach(b => b.disabled = true);
      const userId = await getUserId();
      await fetch(pythonURI + '/api/scoreboard/', {
        ...fetchOptions,
        method: 'POST',
        body: JSON.stringify({ score, userId, difficulty })
      });
      updateLeaderboard();
      playAgainBtn.classList.remove('hidden');
    }

    showQuestion();
    timerId = setInterval(tick, 1000);
  }

  document.getElementById('startGameButton').addEventListener('click', async () => {
    document.getElementById('message').textContent = '';
    const difficulty = document.getElementById('difficultySelect').value;
    try {
      currentQuestions = await fetchGameQuestions(difficulty);
      startChallenge(currentQuestions);
    } catch (e) {
      document.getElementById('message').textContent = e.message;
    }
  });

  const filterDifficulty = document.getElementById('filterDifficulty');
  const searchUsername = document.getElementById('searchUsername');

  filterDifficulty.addEventListener('change', () => {
    renderLeaderboard(filterDifficulty.value, searchUsername.value);
  });

  searchUsername.addEventListener('input', () => {
    renderLeaderboard(filterDifficulty.value, searchUsername.value);
  });

  document.getElementById('playAgainButton').addEventListener('click', () => {
    document.getElementById('startGameButton').click();
  });

  // Instructions modal toggle
  const instructionsModal = document.getElementById('instructionsModal');
  document.getElementById('showInstructionsButton').addEventListener('click', () => {
    instructionsModal.classList.remove('hidden');
  });
  document.getElementById('closeInstructions').addEventListener('click', () => {
    instructionsModal.classList.add('hidden');
  });

  // On load, fetch leaderboard
  updateLeaderboard();
</script>
