---
layout: tailwind
permalink: /genes/
menu: nav/home.html
author: Nora Ahadian
show_reading_time: false
---
<style>
  body {
    background-image: url('{{site.baseurl}}/images/dnacircle.png');
    background-repeat: no-repeat;
    background-position: center calc(50% + 20px);
    background-size: 700px;
  }

  body.no-bg {
    background-image: none;
  }

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

  .genes-page .base {
    cursor: move;
    padding: 4px 10px;
    border: 1px solid #999;
    border-radius: 4px;
    background: #fff;
  }

  .genes-page .A { color: #e74c3c; }
  .genes-page .T { color: #2980b9; }
  .genes-page .C { color: #27ae60; }
  .genes-page .G { color: #f39c12; }

  .genes-page button,
  .genes-page select {
    margin-top: 10px;
    padding: 8px 14px;
    background: rgb(66, 136, 223); /* Dropdown/button color */
    color: white!important ;
    border: none;
    font-size: 16px;
    cursor: pointer;
    margin-right: 8px;
    border-radius: 6px;
  }

  .genes-page button:hover {
    background-color:rgb(255, 255, 255); /* Button Hover color */
    color: SteelBlue !important ;

  }

  .genes-page select {
    color: black;
  }

  .genes-page #mutation-type,
  .genes-page #mutation-effect {
    margin-top: 18px;
    font-weight: bold;
    font-size: 18px;
  }

  .genes-page .hidden {
    display: none;
  }

  .genes-page .progress-container {
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 4px;
    margin-top: 10px;
    height: 20px;
    overflow: hidden;
  }

  .genes-page .progress-bar {
    height: 100%;
    width: 0%;
    background-color: #4CAF50;
    text-align: center;
    color: white;
    line-height: 20px;
    font-size: 12px;
  }

  .genes-page #move-counter {
    font-weight: bold;
    margin-top: 10px;
  }

  .genes-page #you-won-message {
    font-size: 20px;
    color: green;
    font-weight: bold;
    margin-top: 12px;
  }

  /* Popup overlay for mode selector */
  .popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgb(34, 90, 232); 
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }

  .popup-content {
    background-color: #e6f0ff; /* light blue */
    padding: 40px;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
    text-align: center;
  }

  .popup-content h2 {
    font-size: 22px;
    margin-bottom: 12px;
    color: #003366;
  }

  .popup-content select {
    font-size: 16px;
    padding: 8px 12px;
    margin-bottom: 20px;
  }

  .popup-content button {
    padding: 10px 20px;
    background-color: #003366;
    color: white;
    font-size: 16px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
  }

  .popup-content button:hover {
    background-color: #002244;
  }

  .highlighted {
  box-shadow: 0 0 0 4px yellow !important;
  position: relative;
  z-index: 1001;
}
</style>

<div class="genes-page">

<!-- Game Mode Selector -->
<div id="mode-select" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
  <div style="background-color:rgba(17, 75, 156, 0.66);" class="p-6 rounded-lg max-w-md w-full text-white text-center shadow-xl">
    <h2 class="text-2xl font-bold mb-4">Select a Game Mode</h2>
    <select id="mode" onchange="handleModeChange()" class="mb-4 p-2 rounded bg-gray-700 text-white w-full">
      <option value="sandbox">Sandbox</option>
      <option value="fix">Fix the Gene</option>
    </select>
    <div id="difficulty-container" class="hidden mb-4">
      <h3 class="font-semibold mb-2">Select Difficulty</h3>
      <select id="difficulty" class="p-2 rounded bg-gray-700 text-white w-full">
        <option value="easy">Easy (4 bases)</option>
        <option value="medium" selected>Medium (8 bases)</option>
        <option value="hard">Hard (12 bases)</option>
      </select>
    </div>
    <button id="start-button" class="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded w-full mt-2">Start Game</button>
  </div>
</div>


<!-- Difficulty Level Selector (hidden by default) -->
<div id="difficulty-container" class="hidden">
  <h2 style="font-size: 18px; font-weight: bold;">Select Difficulty:</h2>
  <select id="difficulty" style="font-size: 16px; margin-bottom: 10px;">
    <option value="easy">Easy (4 bases)</option>
    <option value="medium" selected>Medium (8 bases)</option>
    <option value="hard">Hard (12 bases)</option>
  </select>
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

</div>

<script>
// Finalized tutorial with locked steps, button highlighting, and mode-specific logic
const BACKEND_URL = "http://127.0.0.1:8504/api";
let currentGene = "";
let currentCondition = "";
let correctSequence = "";
let currentSequence = "";
let moveCount = 0;
let mode = "sandbox";
let baseMoved = false;
let mutationUsed = false;

function handleModeChange() {
const selected = document.getElementById("mode").value;
if (selected === "fix") {
document.getElementById("fix-tools").classList.remove("hidden");
document.getElementById("sandbox-tools").classList.add("hidden");
document.getElementById("difficulty-container").classList.remove("hidden");
} else {
document.getElementById("fix-tools").classList.add("hidden");
document.getElementById("sandbox-tools").classList.remove("hidden");
document.getElementById("difficulty-container").classList.add("hidden");
}
}

function startGame() {
mode = document.getElementById("mode").value;
mutationUsed = false;
baseMoved = false;
document.getElementById("mode-select").classList.add("hidden");
document.getElementById("game-ui").classList.remove("hidden");
document.body.classList.add("no-bg");
handleModeChange();
populateGeneList();
showTutorial();
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

function loadSelectedGene() {
const selected = document.getElementById("gene-select").value;
const difficulty = document.getElementById("difficulty").value;
const lengthMap = { easy: 4, medium: 8, hard: 12 };
const desiredLength = lengthMap[difficulty];
fetch(`${BACKEND_URL}/choose-gene?name=${selected}&length=${desiredLength}`)
.then(res => res.json())
.then(data => {
currentGene = data.gene;
currentCondition = data.condition;
correctSequence = data.sequence;
moveCount = 0;
document.getElementById("you-won-message").textContent = "";
document.getElementById("gene-name").textContent = `Gene: ${currentGene}`;
document.getElementById("condition-name").textContent = `Condition: ${currentCondition}`;
document.getElementById("mutation-effect").textContent = "";
document.getElementById("move-counter").textContent = "Moves: 0";
if (mode === "fix") {
document.getElementById("scramble-popup").style.display = "flex";
let scrambled = correctSequence;
let attempts = 0;
while (similarity(scrambled, correctSequence) >= 0.5 && attempts < 100) {
scrambled = scrambleSequence(correctSequence);
attempts++;
}
currentSequence = scrambled;
setTimeout(() => {
renderSequence(currentSequence);
document.getElementById("scramble-popup").style.display = "none";
updateProgress();
}, 1200);
} else {
currentSequence = correctSequence;
renderSequence(currentSequence);
}
updateProgress();
});
}

function similarity(seq1, seq2) {
let correct = 0;
for (let i = 0; i < seq1.length; i++) {
if (seq1[i] === seq2[i]) correct++;
}
return correct / seq1.length;
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
baseMoved = true;
if (mode === "fix") {
moveCount++;
document.getElementById("move-counter").textContent = `Moves: ${moveCount}`;
updateProgress();
}
renderSequence(currentSequence);
}

function applyMutation() {
mutationUsed = true;
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
let tutorialStep = 0;
let tutorialLock = false;
const tutorialSteps = [];

function highlightElement(selector) {
  document.querySelectorAll(".highlighted").forEach(el => el.classList.remove("highlighted"));
  const el = document.querySelector(selector);
  if (el) el.classList.add("highlighted");
}

function showTutorial() {
  tutorialStep = 0;
  tutorialLock = false;
  baseMoved = false;
  mutationUsed = false;
  document.getElementById("tutorial-overlay")?.remove();

  tutorialSteps.length = 0;
  tutorialSteps.push(
    { text: "Welcome! Click 'Next' to begin.", selector: null },
    { text: "Step 1: Open the gene dropdown.", selector: "#gene-select", waitFor: "#gene-select" },
    { text: "Step 2: Click 'Load Gene'.", selector: "button[onclick='loadSelectedGene()']", waitFor: "button[onclick='loadSelectedGene()']" },
    { text: "Step 3: Try dragging a base.", selector: "#dna-sequence", waitFor: () => baseMoved },
    mode === "sandbox"
      ? { text: "Step 4: Apply a mutation.", selector: "#sandbox-tools", waitFor: () => mutationUsed }
      : { text: "Step 4: Watch the progress bar.", selector: ".progress-container" },
    { text: "You're ready! Click 'Next' to finish.", selector: null }
  );

  const overlay = document.createElement("div");
  overlay.id = "tutorial-overlay";
  overlay.className = "fixed inset-0 bg-black bg-opacity-75 z-50 flex items-center justify-center";
  overlay.innerHTML = `
    <div class="bg-white text-black p-6 rounded-lg max-w-md w-full shadow-lg relative text-center flex flex-col items-center mt-64">
      <p id="tutorial-text" class="text-lg mb-4">${tutorialSteps[0].text}</p>
      <button id="tutorial-next" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Next</button>
      <button id="skip-tutorial" class="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 mt-6 font-bold">Skip Tutorial ✖</button>
    </div>`;


  document.body.appendChild(overlay);

  document.getElementById("tutorial-next").onclick = () => {
    if (tutorialLock) return;
    tutorialStep++;
    if (tutorialStep < tutorialSteps.length) {
      runTutorialStep();
    } else {
      endTutorial();
    }
  };

  document.getElementById("skip-tutorial").onclick = endTutorial;
  runTutorialStep();
}
function runTutorialStep() {
  const step = tutorialSteps[tutorialStep];
  document.getElementById("tutorial-text").textContent = step.text;
  tutorialLock = !!step.waitFor;
  document.getElementById("tutorial-next").disabled = tutorialLock;

  highlightElement(step.selector);

  if (typeof step.waitFor === "function") {
    const interval = setInterval(() => {
      if (step.waitFor()) {
        clearInterval(interval);
        unlockTutorial();
      }
    }, 300);
  } else if (typeof step.waitFor === "string") {
    const el = document.querySelector(step.waitFor);
    if (el) el.addEventListener("click", unlockTutorial, { once: true });
  }
}

function unlockTutorial() {
  tutorialLock = false;
  document.getElementById("tutorial-next").disabled = false;
}

function endTutorial() {
  document.getElementById("tutorial-overlay")?.remove();
  document.querySelectorAll(".highlighted").forEach(el => el.classList.remove("highlighted"));
}
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("start-button").addEventListener("click", startGame);
});

</script>