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

  <div class="text-center">
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
    <table class="w-full table-auto border-collapse">
      <thead>
        <tr class="bg-blue-200">
          <th class="border px-3 py-2 text-blue-900">Username</th>
          <th class="border px-3 py-2 text-blue-900">Score</th>
        </tr>
      </thead>
      <tbody id="leaderboardBody" class="text-blue-800"></tbody>
    </table>
  </div>

  <p id="message" class="text-red-500 text-center pt-2"></p>

  <!-- 🧬 Gene Information Table Section -->
  <div id="geneTableSection" class="mt-10">
    <h3 class="text-xl font-bold text-center text-blue-900 mb-4">🧬 Learn About Key Genes</h3>
    <!-- Search Bar -->
    <div class="mb-4 text-center">
    <input
      id="geneSearch"
      type="text"
      placeholder="Search Genes by Name or Location"
      class="p-2 border-2 border-gray-300 rounded-lg w-80 text-black"
      oninput="filterGeneTable()">    
    </div>
    <div id="geneTableContainer" class="overflow-x-auto bg-white rounded-2xl shadow-inner">
      <table class="min-w-full table-auto text-center border-collapse">
        <thead>
          <tr class="bg-blue-200">
            <th class="border px-3 py-2 text-blue-900">Gene Symbol</th>
            <th class="border px-3 py-2 text-blue-900">Gene Name</th>
            <th class="border px-3 py-2 text-blue-900">Chromosome</th>
            <th class="border px-3 py-2 text-blue-900">Location</th>
            <th class="border px-3 py-2 text-blue-900">Description</th>
            <th class="border px-3 py-2 text-blue-900">Learn More</th>
          </tr>
        </thead>
        <tbody id="geneTableBody" class="text-blue-800">
          <!-- Gene data rows will be dynamically inserted here -->
        </tbody>
      </table>
    </div>
  </div>
</div>

<script type="module">
  import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

  let currentQuestions = [];

  async function getUserId() {
    const res = await fetch(pythonURI + '/api/id', fetchOptions);
    return (await res.json()).id;
  }

  async function fetchGameQuestions() {
    const res = await fetch(pythonURI + '/api/get_questions', fetchOptions);
    if (!res.ok) throw new Error('Failed to load questions');
    return await res.json();
  }

  async function updateLeaderboard() {
    const topRes = await fetch(pythonURI + '/api/scoreboard/top', fetchOptions);
    const top = await topRes.json();
    const tbody = document.getElementById('leaderboardBody');
    tbody.innerHTML = '';
    top.forEach(e => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td class="border px-2 py-1">${e.username}</td>
        <td class="border px-2 py-1">${e.score}</td>
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
    const qText    = document.getElementById('questionText');
    const ansCtn   = document.getElementById('answersContainer');
    const timerEl  = document.getElementById('timer');
    const scoreEl  = document.getElementById('score');
    const playAgainBtn = document.getElementById('playAgainButton');

    // Reset UI
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
            btn.classList.remove('bg-blue-500', 'hover:bg-blue-400');
            btn.classList.add('bg-green-500', 'animate-pulse');
            score++;
            scoreEl.textContent = score;
          } else {
            btn.classList.remove('bg-blue-500', 'hover:bg-blue-400');
            btn.classList.add('bg-red-500', 'animate-pulse');
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
        body: JSON.stringify({ score, userId })
      });
      updateLeaderboard();
      playAgainBtn.classList.remove('hidden');
    }

    showQuestion();
    timerId = setInterval(tick, 1000);
  }

  document.getElementById('startGameButton').addEventListener('click', async () => {
    document.getElementById('message').textContent = '';
    try {
      currentQuestions = await fetchGameQuestions();
      startChallenge(currentQuestions);
    } catch (e) {
      document.getElementById('message').textContent = e.message;
    }
  });

  document.getElementById('playAgainButton').addEventListener('click', async () => {
    document.getElementById('message').textContent = '';
    document.getElementById('playAgainButton').classList.add('hidden');
    try {
      currentQuestions = await fetchGameQuestions();
      startChallenge(currentQuestions);
    } catch (e) {
      document.getElementById('message').textContent = e.message;
    }
  });

  document.addEventListener("DOMContentLoaded", async () => {
    updateLeaderboard();
    const genes = await fetchGeneResources();
    renderGeneTable(genes);
  });

  async function fetchGeneResources() {
    const res = await fetch(pythonURI + '/api/gene_resources', fetchOptions);
    if (!res.ok) throw new Error('Failed to load gene resources');
    return await res.json();
  }

  function renderGeneTable(genes) {
    const tbody = document.getElementById('geneTableBody');
    tbody.innerHTML = '';

    genes.forEach(gene => {
      const row = document.createElement('tr');
      row.innerHTML = `
        <td class="border px-3 py-2 text-purple-900">${gene.symbol}</td>
        <td class="border px-3 py-2 text-purple-900">${gene.name}</td>
        <td class="border px-3 py-2 text-purple-900">${gene.chromosome}</td>
        <td class="border px-3 py-2 text-purple-900">${gene.map_location}</td>
        <td class="border px-3 py-2 text-purple-900">${gene.description}</td>
        <td class="border px-3 py-2 text-purple-900"><a href="${gene.url}" target="_blank" class="text-blue-500 underline">Learn more</a></td>
      `;
      tbody.appendChild(row);
    });
  }

  function filterGeneTable() {
    const query = document.getElementById('geneSearch').value.toLowerCase();
    const rows = document.querySelectorAll('#geneTableBody tr');
    rows.forEach(row => {
      const name = row.cells[1].textContent.toLowerCase();
      const location = row.cells[3].textContent.toLowerCase();
      row.style.display = (name.includes(query) || location.includes(query)) ? '' : 'none';
    });
  }
</script>
