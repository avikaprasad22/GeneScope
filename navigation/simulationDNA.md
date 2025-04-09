---
layout: tailwind
# title: DNA Animation
permalink: /dnasimulation/
show_reading_time: false
---

<head>
  <meta charset="UTF-8">
  <title>DNA Animation</title>
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

<!-- Buttons -->
<div class="absolute bottom-10 left-10 z-10 flex flex-col gap-4">
  <button onclick="changeSequence('human')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Human</button>
  <button onclick="changeSequence('virus')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Virus</button>
  <button onclick="changeSequence('bacteria')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Bacteria</button>
  <button onclick="changeSequence('strawberry')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Strawberry</button>
  <button id="freezeButton" onclick="toggleFreeze()" class="p-3 bg-gray-700 hover:bg-gray-800 text-white rounded-lg shadow-md transition duration-300">Freeze</button>
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

  const sequences = {
    'human': "ATGCGTACGTTGACCTAGGCTAACCGTTCAGC",
    'virus': "TTAAGCGGCTGACCGAATTCCGGTAGCTTAGG",
    'bacteria': "GCTTAGGCCAATCGTTAAGGCCGATCCTAGGT",
    'strawberry': "ATGGTGAGCTCAGTTGGTGACCTGAGGCTTCA"
  };

  let currentSequence = sequences['human'];

  function toggleFreeze() {
    isFrozen = !isFrozen;
    document.getElementById('freezeButton').textContent = isFrozen ? 'Unfreeze' : 'Freeze';
  }

  function changeSequence(sequence) {
    currentSequence = sequences[sequence];
    angleOffset = 0;
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
        const base2 = complements[base1];

        // White connecting line
        drawBasePairLine(x1, y, x2, y);

        // Colored nucleotide dots
        ctx.beginPath();
        ctx.arc(x1, y, 8, 0, Math.PI * 2);
        ctx.fillStyle = baseColors[base1];
        ctx.fill();

        ctx.beginPath();
        ctx.arc(x2, y, 8, 0, Math.PI * 2);
        ctx.fillStyle = baseColors[base2];
        ctx.fill();
      }
    } else {
      const ladderX = centerX;
      for (let i = 0; i < currentSequence.length; i++) {
        const y = 100 + i * baseSpacing;
        const base1 = currentSequence[i];
        const base2 = complements[base1];

        // White bar
        ctx.fillStyle = 'white';
        ctx.fillRect(ladderX - 50, y - 4, 100, 8);

        // White rung
        drawBasePairLine(ladderX - 50, y, ladderX + 50, y);

        // Colored dots
        ctx.beginPath();
        ctx.arc(ladderX - 55, y, 8, 0, Math.PI * 2);
        ctx.fillStyle = baseColors[base1];
        ctx.fill();

        ctx.beginPath();
        ctx.arc(ladderX + 55, y, 8, 0, Math.PI * 2);
        ctx.fillStyle = baseColors[base2];
        ctx.fill();
      }
    }

    angleOffset += speed;
    requestAnimationFrame(animateDNA);
  }

  animateDNA();
</script>
</body>
</html>
