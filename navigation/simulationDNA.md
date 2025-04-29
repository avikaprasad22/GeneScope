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
    .hover-line {
      position: absolute;
      height: 2px;
      width: 0;
      transition: width 0.4s ease;
      pointer-events: none;
      z-index: 40;
    }
    .loader {
  position: relative;
  width: 2.5em;
  height: 2.5em;
  transform: rotate(165deg);
  margin: 0 auto;
  margin-top: 20px;
}
.loader:before, .loader:after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  display: block;
  width: 0.5em;
  height: 0.5em;
  border-radius: 0.25em;
  transform: translate(-50%, -50%);
}
.loader:before {
  animation: before8 2s infinite;
}
.loader:after {
  animation: after6 2s infinite;
}
@keyframes before8 {
  0% {
    width: 0.5em;
    box-shadow: 1em -0.5em rgba(225, 20, 98, 0.75), -1em 0.5em rgba(111, 202, 220, 0.75);
  }
  35% {
    width: 2.5em;
    box-shadow: 0 -0.5em rgba(225, 20, 98, 0.75), 0 0.5em rgba(111, 202, 220, 0.75);
  }
  70% {
    width: 0.5em;
    box-shadow: -1em -0.5em rgba(225, 20, 98, 0.75), 1em 0.5em rgba(111, 202, 220, 0.75);
  }
  100% {
    box-shadow: 1em -0.5em rgba(225, 20, 98, 0.75), -1em 0.5em rgba(111, 202, 220, 0.75);
  }
}
@keyframes after6 {
  0% {
    height: 0.5em;
    box-shadow: 0.5em 1em rgba(61, 184, 143, 0.75), -0.5em -1em rgba(233, 169, 32, 0.75);
  }
  35% {
    height: 2.5em;
    box-shadow: 0.5em 0 rgba(61, 184, 143, 0.75), -0.5em 0 rgba(233, 169, 32, 0.75);
  }
  70% {
    height: 0.5em;
    box-shadow: 0.5em -1em rgba(61, 184, 143, 0.75), -0.5em 1em rgba(233, 169, 32, 0.75);
  }
  100% {
    box-shadow: 0.5em 1em rgba(61, 184, 143, 0.75), -0.5em -1em rgba(233, 169, 32, 0.75);
  }
}

  </style>
</head>

<body class="bg-black text-white">

<!-- Form -->
<div class="absolute top-15 left-5 z-10 bg-gray-900 bg-opacity-80 p-4 rounded-xl shadow-lg">
  <h2 class="text-lg font-bold mb-2">Search DNA Sequence</h2>
  <input id="organismInput" type="text" placeholder="Organism (e.g. homo sapiens)"
         class="mb-2 p-2 rounded w-full text-black" />
  <input id="geneInput" type="text" placeholder="Gene symbol (e.g. BRCA1)"
         class="mb-2 p-2 rounded w-full text-black" />
  <button onclick="fetchSequence()"
          class="w-full bg-indigo-600 hover:bg-indigo-700 text-white p-2 rounded">Load Sequence</button>
          <div id="loader" class="loader hidden"></div>

  <p id="errorMessage" class="text-red-400 mt-2"></p>
</div>

<!-- Freeze Button -->
<div class="absolute bottom-10 left-10 z-10">
  <button id="freezeButton" onclick="toggleFreeze()"
          class="p-3 bg-gray-700 hover:bg-gray-800 text-white rounded-lg shadow-md transition duration-300">Freeze</button>
</div>

<button class="bg-red-950 text-red-400 border border-red-400 border-b-4 font-medium overflow-hidden relative px-4 py-2 rounded-md hover:brightness-150 hover:border-t-4 hover:border-b active:opacity-75 outline-none duration-300 group">
  <span class="bg-red-400 shadow-red-400 absolute -top-[150%] left-0 inline-flex w-80 h-[5px] rounded-md opacity-50 group-hover:top-[150%] duration-500 shadow-[0_0_10px_10px_rgba(0,0,0,0.3)]"></span>
  Hover Over Colored Dots For More Info
</button>

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
    'A': 'Adenine is a purine, meaning it has a double-ring structure made of a six-membered and a five-membered ring fused together. It pairs specifically with thymine in DNA through two hydrogen bonds, a pairing that helps stabilize the double helix structure. In addition to its role in DNA, adenine is a key component of important biomolecules like ATP (adenosine triphosphate), NAD, and FAD, all of which are involved in energy transfer and enzymatic processes.',
    'T': 'Thymine, a pyrimidine base with a single six-membered ring, pairs with adenine via two hydrogen bonds. Unique to DNA, thymine contains a methyl group that contributes to the chemical stability of DNA compared to RNA. In RNA, thymine is replaced by uracil, which lacks this methyl group.',
    'C': 'Cytosine is another pyrimidine, with an amino group at carbon 4 and a carbonyl group at carbon 2. It pairs with guanine through three hydrogen bonds, contributing to DNA’s structural strength. Cytosine is also notable for its role in epigenetic regulation, as it can be chemically modified through methylation to form 5-methylcytosine, which affects gene expression without altering the DNA sequence.',
    'G': 'Guanine is the second purine base, structurally similar to adenine but with a carbonyl group at position 6 and an amino group at position 2. It pairs with cytosine using three hydrogen bonds, forming a more thermally stable bond than adenine-thymine pairs. Guanine is also found in molecules like GTP (guanosine triphosphate), which play essential roles in signal transduction and protein synthesis.'
  };

  let currentSequence = 'ATCG'.repeat(50);

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
          // show tooltip and codon info
          customTooltip.textContent = baseDescriptions[base] || base;
          customTooltip.style.left = `${x}px`;
          customTooltip.style.top = `${y}px`;
          customTooltip.style.boxShadow = `0 0 12px ${baseColors[base]}`;
          customTooltip.classList.remove('hidden');

          codonTitle.textContent = baseDescriptions[base];
          codonDescription.textContent = fullDescriptions[base];
          codonBox.style.borderColor = baseColors[base];
          codonBox.style.boxShadow = `0 0 20px ${baseColors[base]}`;
          codonBox.classList.remove('hidden');

          // create and animate line
          const line = document.createElement('div');
          line.className = 'hover-line';
          line.style.backgroundColor = baseColors[base];
          line.style.left = `${x}px`;
          line.style.top = `${y}px`;
          tooltipContainer.appendChild(line);
          requestAnimationFrame(() => {
            line.style.width = '180px';
          });
        });

        dot.addEventListener('mouseleave', () => {
          customTooltip.classList.add('hidden');
          codonBox.classList.add('hidden');
          // remove line
          const existing = tooltipContainer.querySelector('.hover-line');
          if (existing) tooltipContainer.removeChild(existing);
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
  const loaderEl = document.getElementById('loader');  // The loader element
  errorEl.textContent = "";

  if (!organism || !gene) {
    errorEl.textContent = "Please enter both organism and gene symbol.";
    return;
  }

  // Show the loader while fetching
  loaderEl.style.display = 'block';

  try {
    const response = await fetch('http://127.0.0.1:8504/api/sequence', {
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
  } finally {
    // Hide the loader when done (or error)
    loaderEl.style.display = 'none';
  }
}


  animateDNA();
</script>
</body>
