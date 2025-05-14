---
layout: tailwind
permalink: /genes/
menu: nav/home.html
author: Nora Ahadian
show_reading_time: false
---

<style>
  .sequence-box {
    display: flex;
    gap: 6px;
    padding: 12px;
    border: 1px solid #ccc;
    background: #f9f9f9;
    font-family: monospace;
    font-size: 22px;
    margin-top: 10px;
    min-height: 40px;
    flex-wrap: wrap;
  }

  .base {
    cursor: move;
    padding: 4px 10px;
    border: 1px solid #999;
    border-radius: 4px;
    background: #fff;
  }

  .A { color: #e74c3c; }
  .T { color: #2980b9; }
  .C { color: #27ae60; }
  .G { color: #f39c12; }

  button, select {
    margin-top: 10px;
    padding: 8px 14px;
    background: #4CAF50;
    color: white;
    border: none;
    font-size: 16px;
    cursor: pointer;
    margin-right: 8px;
  }

  button:hover {
    background-color: #45a049;
  }

  select {
    color: black;
  }

  #mutation-type, #mutation-effect {
    margin-top: 18px;
    font-weight: bold;
    font-size: 18px;
  }

  .hidden {
    display: none;
  }

  .progress-container {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 4px;
    margin-top: 10px;
    height: 20px;
    overflow: hidden;
  }

  .progress-bar {
    height: 100%;
    width: 0%;
    background-color: #4CAF50;
    text-align: center;
    color: white;
    line-height: 20px;
    font-size: 12px;
  }

  #move-counter {
    font-weight: bold;
    margin-top: 10px;
  }

  #you-won-message {
    font-size: 20px;
    color: green;
    font-weight: bold;
    margin-top: 12px;
  }
</style>

# Gene Mutation Game

<!-- Game Mode Selector -->
<div id="mode-select" style="margin-bottom: 20px;">
  <h2 style="font-size: 20px; font-weight: bold;">Select a Game Mode:</h2>
  <select id="mode" onchange="handleModeChange()" style="font-size: 16px; margin-top: 8px;">
    <option value="fix">🧩 Fix the Gene</option>
    <option value="sandbox">🧪 Sandbox</option>
  </select>
  <br>
  <button onclick="startGame()" style="margin-top: 10px;">Start Game</button>
</div>


<!-- Shared Gene Selection -->
<div id="game-ui" class="hidden">
  <label for="gene-select">Select a gene:</label>
  <select id="gene-select">
    <option value="random">Random</option>
  </select>
  <button onclick="loadSelectedGene()">Load Gene</button>

  <p id="gene-name">Gene: ...</p>
  <p id="condition-name">Condition: ...</p>

  <div id="dna-sequence" class="sequence-box"></div>

  <!-- Fix the Gene Mode UI -->
  <div id="fix-tools" class="hidden">
    <div class="progress-container">
      <div class="progress-bar" id="progress-bar">0%</div>
    </div>
    <div id="move-counter">Moves: 0</div>
    <p id="you-won-message"></p>
  </div>

  <!-- Sandbox Mode UI -->
  <div id="sandbox-tools" class="hidden" style="margin-top: 12px;">
    <select id="mutation-action">
      <option value="substitute">Substitution</option>
      <option value="insert">Insertion</option>
      <option value="delete">Deletion</option>
    </select>
    <input type="text" id="base-input" maxlength="1" placeholder="Base (A/T/C/G)" />
    <button onclick="applyMutation()">Apply Mutation</button>
  </div>

  <p id="mutation-effect"></p>
</div>

<!-- Scramble popup (for Fix mode only) -->
<div id="scramble-popup" style="
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.8);
  color: white;
  font-size: 24px;
  display: none;
  justify-content: center;
  align-items: center;
  z-index: 100;
  flex-direction: column;
">
  <p>Randomizing sequence…</p>
</div>
<script>
const BACKEND_URL = "http://127.0.0.1:8504/api";
let currentGene = "";
let currentCondition = "";
let correctSequence = "";
let currentSequence = "";
let moveCount = 0;
let mode = "sandbox";  // default
function handleModeChange() {
  const selected = document.getElementById("mode").value;
  if (selected === "fix") {
    document.getElementById("fix-tools").classList.remove("hidden");
    document.getElementById("sandbox-tools").classList.add("hidden");
  } else {
    document.getElementById("fix-tools").classList.add("hidden");
    document.getElementById("sandbox-tools").classList.remove("hidden");
  }
}
function startGame() {
  mode = document.getElementById("mode").value;
  document.getElementById("mode-select").classList.add("hidden");
  document.getElementById("game-ui").classList.remove("hidden");
  handleModeChange(); // toggle UI tools
  populateGeneList();
  loadSelectedGene();
}
async function populateGeneList() {
  try {
    const res = await fetch(`${BACKEND_URL}/gene-list`);
    const data = await res.json();
    const select = document.getElementById("gene-select");
    select.innerHTML = `<option value="random">Random</option>`;
    data.genes.forEach(gene => {
      const opt = document.createElement("option");
      opt.value = gene;
      opt.textContent = gene;
      select.appendChild(opt);
    });
  } catch (err) {
    console.error("Failed to load gene list:", err);
  }
}
function scrambleSequence(seq) {
  const arr = seq.split('');
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr.join('');
}
async function loadSelectedGene() {
  const selected = document.getElementById("gene-select").value;
  const res = await fetch(`${BACKEND_URL}/choose-gene?name=${selected}`);
  const data = await res.json();
  currentGene = data.gene;
  currentCondition = data.condition;
  correctSequence = data.sequence;
  moveCount = 0;
  document.getElementById("you-won-message").textContent = "";
  document.getElementById("gene-name").textContent = `Gene: ${currentGene}`;
  document.getElementById("condition-name").textContent = `Condition: ${currentCondition}`;
  document.getElementById("mutation-effect").textContent = "";
  document.getElementById("move-counter").textContent = `Moves: 0`;
  if (mode === "fix") {
    document.getElementById("scramble-popup").style.display = "flex";
    renderSequence(correctSequence); // show original briefly
    setTimeout(() => {
      currentSequence = scrambleSequence(correctSequence);
      renderSequence(currentSequence);
      document.getElementById("scramble-popup").style.display = "none";
      updateProgress();
    }, 1500);
  } else {
    currentSequence = correctSequence;
    renderSequence(currentSequence);
  }
  updateProgress();
}
function renderSequence(sequence) {
  const box = document.getElementById("dna-sequence");
  box.innerHTML = "";
  for (let i = 0; i < sequence.length; i++) {
    const span = document.createElement("span");
    span.textContent = sequence[i];
    span.className = `base ${sequence[i]}`;
    span.setAttribute("draggable", "true");
    span.dataset.index = i;
    span.ondragstart = e => {
      e.dataTransfer.setData("text/plain", e.target.dataset.index);
    };
    span.ondragover = e => e.preventDefault();
    span.ondrop = e => {
      e.preventDefault();
      const fromIndex = parseInt(e.dataTransfer.getData("text/plain"));
      const toIndex = parseInt(e.target.dataset.index);
      swapBases(fromIndex, toIndex);
    };
    box.appendChild(span);
  }
}
function swapBases(fromIndex, toIndex) {
  let arr = currentSequence.split('');
  [arr[fromIndex], arr[toIndex]] = [arr[toIndex], arr[fromIndex]];
  currentSequence = arr.join('');
  if (mode === "fix") {
    moveCount++;
    document.getElementById("move-counter").textContent = `Moves: ${moveCount}`;
    updateProgress();
  }
  renderSequence(currentSequence);
}
function applyMutation() {
  const action = document.getElementById("mutation-action").value;
  const base = document.getElementById("base-input").value.toUpperCase();
  const bases = currentSequence.split("");
  if (!["A", "T", "C", "G"].includes(base) && action !== "delete") {
    alert("Please enter a valid base (A, T, C, G)");
    return;
  }
  if (action === "substitute") {
    bases[0] = base;
    showEffect("Substitution changes one base and can alter a protein, or sometimes do nothing (silent).");
  } else if (action === "insert") {
    bases.splice(0, 0, base);
    showEffect("Insertion can cause a frameshift, altering the entire protein downstream.");
  } else if (action === "delete") {
    bases.splice(0, 1);
    showEffect("Deletion removes a base, often causing a frameshift mutation.");
  }
  currentSequence = bases.join("").substring(0, 12);
  renderSequence(currentSequence);
}
function updateProgress() {
  if (mode !== "fix") return;
  let correct = 0;
  for (let i = 0; i < correctSequence.length; i++) {
    if (currentSequence[i] === correctSequence[i]) correct++;
  }
  const percent = Math.floor((correct / correctSequence.length) * 100);
  const bar = document.getElementById("progress-bar");
  bar.style.width = percent + "%";
  bar.textContent = `${percent}%`;
  if (percent === 100) {
    document.getElementById("you-won-message").textContent = "🎉 You fixed the gene!";
  }
}
function showEffect(text) {
  document.getElementById("mutation-effect").textContent = `Effect: ${text}`;
}
</script>
