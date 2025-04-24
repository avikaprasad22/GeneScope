---
layout: tailwind
title: DNA Animation
permalink: /dnasimulation/
show_reading_time: false
---

<head>
  <meta charset="UTF-8">
  <title>DNA Simulation</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body, html {
      margin: 0;
      padding: 0;
      overflow: hidden;
    }
  </style>
</head>

<body class="bg-black text-white">

<!-- Form -->
<div class="absolute top-5 left-5 z-10 bg-gray-900 bg-opacity-80 p-4 rounded-xl shadow-lg">
  <h2 class="text-lg font-bold mb-2">Search DNA Sequence</h2>
  <input id="organismInput" type="text" placeholder="Organism (e.g. homo sapiens)"
         class="mb-2 p-2 rounded w-full text-black" />
  <input id="geneInput" type="text" placeholder="Gene symbol (e.g. BRCA1)"
         class="mb-2 p-2 rounded w-full text-black" />
  <button onclick="fetchSequence()"
          class="w-full bg-indigo-600 hover:bg-indigo-700 text-white p-2 rounded">Load Sequence</button>
  <p id="errorMessage" class="text-red-400 mt-2"></p>
</div>

<!-- Freeze Button -->
<div class="absolute bottom-10 left-10 z-10">
  <button id="freezeButton" onclick="toggleFreeze()"
          class="p-3 bg-gray-700 hover:bg-gray-800 text-white rounded-lg shadow-md transition duration-300">Freeze</button>
</div>

<!-- Canvas -->
<canvas id="dnaCanvas" class="absolute top-0 left-0 w-full h-full"></canvas>

<script>
  const canvas = document.getElementById('dnaCanvas');
  const ctx = canvas.getContext('2d');
  const WIDTH = window.innerWidth;
  const HEIGHT = window.innerHeight;
  canvas.width = WIDTH;
  canvas.height = HEIGHT;

  let isFrozen = false;
  let angleOffset = 0;
  const baseSpacing = 40;
  const amplitude = 100;
  const speed = 0.02;
  const complements = { 'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C' };
  const baseColors = {
    'A': '#99ff99',
    'T': '#66b2ff',
    'C': '#ffff99',
    'G': '#ff6666'
  };

  let currentSequence = 'ATCG'.repeat(50); // Default 200 bases

  function toggleFreeze() {
    isFrozen = !isFrozen;
    document.getElementById('freezeButton').textContent = isFrozen ? 'Unfreeze' : 'Freeze';
  }

  function drawBasePairLine(x1, y, x2, y2) {
    ctx.strokeStyle = 'white';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(x1, y);
    ctx.lineTo(x2, y2);
    ctx.stroke();
  }

  function animateDNA() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    const centerX = WIDTH / 2;

    if (!isFrozen) {
      for (let i = 0; i < currentSequence.length; i++) {
        const angle = i * 0.4 + angleOffset;
        const y = 100 + i * baseSpacing;
        const x1 = centerX + amplitude * Math.sin(angle);
        const x2 = centerX - amplitude * Math.sin(angle);

        const base1 = currentSequence[i];
        const base2 = complements[base1] || 'A';

        drawBasePairLine(x1, y, x2, y);
        ctx.beginPath();
        ctx.arc(x1, y, 8, 0, Math.PI * 2);
        ctx.fillStyle = baseColors[base1] || 'gray';
        ctx.fill();

        ctx.beginPath();
        ctx.arc(x2, y, 8, 0, Math.PI * 2);
        ctx.fillStyle = baseColors[base2] || 'gray';
        ctx.fill();
      }
    }

    angleOffset += speed;
    requestAnimationFrame(animateDNA);
  }

  async function fetchSequence() {
    const organism = document.getElementById('organismInput').value.trim();
    const gene = document.getElementById('geneInput').value.trim();
    const errorEl = document.getElementById('errorMessage');
    errorEl.textContent = "";

    if (!organism || !gene) {
      errorEl.textContent = "Please enter both organism and gene symbol.";
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:8504/sequence', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        credentials: 'include',
        body: JSON.stringify({ organism, gene })
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || "Unknown error");
      }

      currentSequence = result.sequence.slice(0, 200); // Limit to 200 bases
      angleOffset = 0;
    } catch (err) {
      errorEl.textContent = `Error: ${err.message}`;
    }
  }

  animateDNA();
</script>
</body>
