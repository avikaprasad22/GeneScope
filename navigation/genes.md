---
layout: tailwind 
permalink: /genes/
menu: nav/home.html
author: Nora Ahadian
show_reading_time: false
---

<style>
  .sequence-box {
    font-family: monospace;
    font-size: 22px;
    background: #f9f9f9;
    border: 1px solid #ccc;
    padding: 12px;
    display: inline-block;
    margin-top: 20px;
    min-width: 300px;
  }

  .A { color: #e74c3c; }
  .T { color: #2980b9; }
  .C { color: #27ae60; }
  .G { color: #f39c12; }
  .underscore { color: #bbb; }

  form {
    margin-top: 25px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }

  button {
    margin-top: 12px;
    padding: 8px 14px;
    background: #4CAF50;
    color: white;
    border: none;
    font-size: 16px;
    cursor: pointer;
  }

  button:hover {
    background-color: #45a049;
  }

  #result, #reveal-section {
    margin-top: 20px;
    font-weight: bold;
    font-size: 18px;
  }

  .hidden {
    display: none;
  }
</style>

# 🔬 Spot the Mutation!

<p id="sequence-status">Loading sequence...</p>
<div id="dna-sequence" class="sequence-box">
  <span class="underscore">_</span>
  <span class="underscore">_</span>
  <span class="underscore">_</span>
  <span class="underscore">_</span>
  <span class="underscore">_</span>
  <span class="underscore">_</span>
</div>

<form id="mutation-form">
  <label><input type="radio" name="mutation" value="substitution"> Substitution</label>
  <label><input type="radio" name="mutation" value="insertion"> Insertion</label>
  <label><input type="radio" name="mutation" value="deletion"> Deletion</label>
  <label><input type="radio" name="mutation" value="none"> No Mutation</label>
  <button type="submit">Submit</button>
</form>

<p id="result"></p>

<div id="reveal-section" class="hidden">
  <button onclick="revealGene()">Reveal the Gene</button>
  <button onclick="tryAgain()">Try Again</button>
  <p id="gene-info" class="hidden"></p>
</div>

<script>
  const BACKEND_URL = "http://127.0.0.1:8504/api";
  let correctMutation = null;
  let currentGene = "";
  let currentCondition = "";
  let currentSequence = "";
  let currentMutation = "";

  async function loadNewSequence() {
    const status = document.getElementById("sequence-status");
    const sequenceBox = document.getElementById("dna-sequence");
    const result = document.getElementById("result");
    const geneInfo = document.getElementById("gene-info");
    const revealSection = document.getElementById("reveal-section");

    try {
      status.textContent = "🧬 Loading sequence...";
      sequenceBox.innerHTML = '<span class="underscore">_</span>'.repeat(6);
      result.textContent = "";
      geneInfo.textContent = "";
      geneInfo.classList.add("hidden");
      revealSection.classList.add("hidden");

      const res = await fetch(`${BACKEND_URL}/get-sequence`);
      if (!res.ok) throw new Error(`HTTP error ${res.status}`);
      const data = await res.json();

      correctMutation = data.mutation;
      currentGene = data.gene;
      currentCondition = data.condition;
      currentSequence = data.sequence;
      currentMutation = data.mutation;

      status.textContent = `🔍 Spot the Mutation Below`;
      sequenceBox.innerHTML = "";
      for (const base of data.sequence) {
        const span = document.createElement("span");
        span.textContent = base;
        if ("ATCG".includes(base)) {
          span.className = base;
        } else {
          span.className = "underscore";
        }
        sequenceBox.appendChild(span);
      }

    } catch (error) {
      console.error("[ERROR] Failed to fetch sequence:", error);
      status.textContent = "❌ Error loading sequence.";
    }
  }

  window.onload = loadNewSequence;

  document.getElementById("mutation-form").onsubmit = async function (e) {
    e.preventDefault();
    const guess = new FormData(e.target).get("mutation");

    try {
      const res = await fetch(`${BACKEND_URL}/check-mutation`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          guess: guess,
          correct: correctMutation,
          gene: currentGene,
          condition: currentCondition,
          mutation: currentMutation,
          sequence: currentSequence
        })
      });

      const result = await res.json();
      document.getElementById("result").textContent = result.message;
      document.getElementById("reveal-section").classList.remove("hidden");

    } catch (error) {
      console.error("Error submitting guess:", error);
      document.getElementById("result").textContent = "❌ Error submitting guess.";
    }
  };

  function revealGene() {
    const geneInfo = document.getElementById("gene-info");
    geneInfo.textContent = `🧬 Gene: ${currentGene} — 🧾 Condition: ${currentCondition}`;
    geneInfo.classList.remove("hidden");
  }

  function tryAgain() {
    loadNewSequence();
    document.querySelector("#mutation-form").reset();
  }
</script>
