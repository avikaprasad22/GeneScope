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

  select {
    color: black;
  }

  button:hover {
    background-color: #45a049;
  }

  #mutation-type, #mutation-effect {
    margin-top: 18px;
    font-weight: bold;
    font-size: 18px;
  }

  .hidden {
    display: none;
  }
</style>

# 🧬 Gene Explorer

<label for="gene-select">Select a gene:</label>
<select id="gene-select">
  <option value="random">Random</option>
</select>
<button onclick="loadSelectedGene()">Load Gene</button>

<p id="gene-name">Gene: ...</p>
<div id="dna-sequence" class="sequence-box"></div>

<div style="margin-top: 12px;">
  <select id="mutation-action">
    <option value="substitute">Substitution</option>
    <option value="insert">Insertion</option>
    <option value="delete">Deletion</option>
  </select>
  <input type="text" id="base-input" maxlength="1" placeholder="Base (A/T/C/G)" />
  <button onclick="applyMutation()">Apply Mutation</button>
</div>

<p id="condition-name">Condition: ...</p>
<p id="mutation-type">Mutation: Hidden</p>
<p id="mutation-effect"></p>

<script>
  const BACKEND_URL = "http://127.0.0.1:8504/api";

  let currentGene = "";
  let currentCondition = "";
  let currentSequence = "";

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

  async function loadSelectedGene() {
    const selected = document.getElementById("gene-select").value;
    const res = await fetch(`${BACKEND_URL}/choose-gene?name=${selected}`);
    const data = await res.json();

    currentGene = data.gene;
    currentCondition = data.condition;
    currentSequence = data.sequence;

    document.getElementById("gene-name").textContent = `Gene: ${currentGene}`;
    document.getElementById("condition-name").textContent = `Condition: ${currentCondition}`;
    document.getElementById("mutation-type").textContent = `Mutation: Hidden`;
    document.getElementById("mutation-effect").textContent = "";

    renderSequence(currentSequence);
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
        const fromIndex = e.dataTransfer.getData("text/plain");
        const toIndex = e.target.dataset.index;
        swapBases(fromIndex, toIndex);
      };

      box.appendChild(span);
    }
  }

  function swapBases(fromIndex, toIndex) {
    const seqBox = document.getElementById("dna-sequence");
    const items = Array.from(seqBox.children);
    const temp = items[fromIndex].textContent;
    items[fromIndex].textContent = items[toIndex].textContent;
    items[toIndex].textContent = temp;

    const tempClass = items[fromIndex].className;
    items[fromIndex].className = items[toIndex].className;
    items[toIndex].className = tempClass;
  }

  function applyMutation() {
    const action = document.getElementById("mutation-action").value;
    const base = document.getElementById("base-input").value.toUpperCase();
    const seqBox = document.getElementById("dna-sequence");
    const bases = Array.from(seqBox.children).map(e => e.textContent);

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

  function showEffect(text) {
    document.getElementById("mutation-effect").textContent = `Effect: ${text}`;
  }

  window.onload = () => {
    populateGeneList();
    loadSelectedGene();
  };
</script>