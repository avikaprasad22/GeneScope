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

    .tooltip-box {
      position: absolute;
      color: white;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 0.8rem;
      pointer-events: none;
      z-index: 50;
      white-space: nowrap;
      transform: translate(-50%, -120%);
      box-shadow: 0 0 10px rgba(255,255,255,0.5);
      background-color: rgba(0, 0, 0, 0.85);
      transition: all 0.2s ease;
    }

    .codon-info {
      max-width: 320px;
      border-left: 4px solid white;
      transition: border-color 0.3s ease, box-shadow 0.3s ease;
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

<!-- Tooltip Overlay -->
<div id="tooltipContainer" class="absolute top-0 left-0 w-full h-full pointer-events-none z-20"></div>
<div id="customTooltip" class="tooltip-box hidden"></div>

<!-- Side Info Box -->
<div id="codonInfoBox" class="absolute top-[150px] right-5 bg-gray-900 bg-opacity-90 text-white p-5 rounded-xl shadow-xl z-30 codon-info hidden">
  <h3 class="text-lg font-bold mb-2" id="codonTitle">Codon Info</h3>
  <p id="codonDescription" class="text-sm leading-relaxed"></p>
</div>

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

  const baseDescriptions = {
    'A': 'Adenine (Green)',
    'T': 'Thymine (Blue)',
    'C': 'Cytosine (Yellow)',
    'G': 'Guanine (Red)'
  };

  const fullDescriptions = {
    'A': 'DNA is composed of four nitrogenous bases: adenine, guanine, thymine, and cytosine, each with distinct structures and functions. Adenine (A) is a purine base characterized by a double-ring structure consisting of fused imidazole and pyrimidine rings. It pairs with thymine through two hydrogen bonds, contributing to the stability of the DNA double helix. Beyond its role in DNA, adenine is also found in essential biomolecules like ATP (adenosine triphosphate), NAD, and FAD, playing key roles in cellular energy transfer and enzymatic activity.',
    'T': 'thymine (T) is a pyrimidine base with a single six-membered ring and a methyl group at the fifth carbon. Thymine pairs with adenine via two hydrogen bonds and is unique to DNA, being replaced by uracil in RNA. The presence of the methyl group enhances DNA stability by protecting it from enzymatic degradation, making DNA more chemically stable than RNA.',
    'C': 'Cytosine is another pyrimidine, with an amino group at carbon 4 and a carbonyl group at carbon 2. It pairs with guanine through three hydrogen bonds, contributing to DNA’s structural strength. Cytosine is also notable for its role in epigenetic regulation, as it can be chemically modified through methylation to form 5-methylcytosine, which affects gene expression without altering the DNA sequence.',
    'G': 'Guanine (G) is the second purine base in DNA and shares a similar double-ring structure with adenine but differs in its functional groups. It forms three hydrogen bonds with cytosine, resulting in a stronger and more thermally stable base pair. Guanine is also involved in cellular signaling through its role in GTP (guanosine triphosphate) and influences gene regulation and DNA structural integrity.'
  };

  let currentSequence = 'ATCG'.repeat(50); // Default 200 bases

  const tooltipContainer = document.getElementById('tooltipContainer');
  const customTooltip = document.getElementById('customTooltip');
  const codonBox = document.getElementById('codonInfoBox');
  const codonTitle = document.getElementById('codonTitle');
  const codonDescription = document.getElementById('codonDescription');

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

  function updateTooltips() {
    tooltipContainer.innerHTML = '';
    const centerX = WIDTH / 2;

    for (let i = 0; i < currentSequence.length; i++) {
      const angle = i * 0.4 + angleOffset;
      const y = 100 + i * baseSpacing;
      const x1 = centerX + amplitude * Math.sin(angle);
      const x2 = centerX - amplitude * Math.sin(angle);

      const base1 = currentSequence[i];
      const base2 = complements[base1] || 'A';

      [[x1, base1], [x2, base2]].forEach(([x, base]) => {
        const dot = document.createElement('div');
        dot.style.position = 'absolute';
        dot.style.left = `${x - 10}px`;
        dot.style.top = `${y - 10}px`;
        dot.style.width = '20px';
        dot.style.height = '20px';
        dot.style.borderRadius = '50%';
        dot.style.pointerEvents = 'auto';
        dot.style.backgroundColor = 'rgba(255, 255, 255, 0.01)';
        dot.addEventListener('mouseenter', () => {
          const color = baseColors[base] || 'white';

          customTooltip.textContent = baseDescriptions[base] || base;
          customTooltip.style.left = `${x}px`;
          customTooltip.style.top = `${y}px`;
          customTooltip.style.boxShadow = `0 0 12px ${color}`;
          customTooltip.classList.remove('hidden');

          codonTitle.textContent = baseDescriptions[base];
          codonDescription.textContent = fullDescriptions[base];
          codonBox.style.borderColor = color;
          codonBox.style.boxShadow = `0 0 20px ${color}`;
          codonBox.classList.remove('hidden');
        });

        dot.addEventListener('mouseleave', () => {
          customTooltip.classList.add('hidden');
        });

        tooltipContainer.appendChild(dot);
      });
    }
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

      updateTooltips();
      angleOffset += speed;
    }

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
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({ organism, gene })
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || "Unknown error");
      }

      currentSequence = result.sequence.slice(0, 200);
      angleOffset = 0;
    } catch (err) {
      errorEl.textContent = `Error: ${err.message}`;
    }
  }

  animateDNA();
</script>
</body>