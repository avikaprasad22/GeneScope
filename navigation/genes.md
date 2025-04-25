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

  button {
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

  #gene-name, #condition-name, #mutation-type {
    margin-top: 18px;
    font-weight: bold;
    font-size: 18px;
  }

  .hidden {
    display: none;
  }
</style>

# 🧬 Gene Explorer

<p id="gene-name">Gene: ...</p>
<div id="dna-sequence" class="sequence-box"></div>

<div style="margin-top: 12px;">
  <button onclick="revealMutation()">Reveal Mutation Type</button>
  <button onclick="checkSequence()">Check New Sequence</button>
</div>

<p id="condition-name">Condition: ...</p>
<p id="mutation-type" class="hidden">Mutation: ...</p>

<script>
  const BACKEND_URL = "http://127.0.0.1:8504/api";

  let currentGene = "";
  let currentCondition = "";
  let currentMutation = "";

  async function loadNewSequence() {
    const seqBox = document.getElementById("dna-sequence");
    const geneText = document.getElementById("gene-name");
    const conditionText = document.getElementById("condition-name");
    const mutationText = document.getElementById("mutation-type");

    try {
      const res = await fetch(`${BACKEND_URL}/get-sequence`);
      const data = await res.json();

      currentGene = data.gene;
      currentCondition = data.condition;
      currentMutation = data.mutation;

      geneText.textContent = `Gene: ${currentGene}`;
      conditionText.textContent = `Condition: ${currentCondition}`;
      mutationText.textContent = "Mutation: ...";
      mutationText.classList.add("hidden");

      renderSequence(data.sequence);

    } catch (error) {
      console.error("Error loading sequence:", error);
    }
  }

  function renderSequence(sequence) {
    const seqBox = document.getElementById("dna-sequence");
    seqBox.innerHTML = "";

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

      seqBox.appendChild(span);
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

  async function checkSequence() {
    const newSeq = Array.from(document.getElementById("dna-sequence").children)
      .map(el => el.textContent)
      .join("");

    try {
      const res = await fetch(`${BACKEND_URL}/check-sequence`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ sequence: newSeq })
      });

      if (!res.ok) throw new Error("No match");

      const data = await res.json();
      document.getElementById("gene-name").textContent = `Gene: ${data.gene}`;
      document.getElementById("condition-name").textContent = `Condition: ${data.condition}`;
      currentMutation = data.mutation;

    } catch (err) {
      document.getElementById("condition-name").textContent = "❌ No match found for this sequence.";
      console.error("❌ Error in checkSequence():", err);
    }
  }

  function revealMutation() {
    const mutationText = document.getElementById("mutation-type");
    mutationText.textContent = `Mutation: ${currentMutation}`;
    mutationText.classList.remove("hidden");
  }

// TESTING CORS
fetch("http://127.0.0.1:8504/test-cors")
  .then(res => res.json())
  .then(console.log)
  .catch(console.error);

  window.onload = loadNewSequence;
</script>