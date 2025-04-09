---
layout: post 
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

  .A { color: #e74c3c; }   /* Red */
  .T { color: #2980b9; }   /* Blue */
  .C { color: #27ae60; }   /* Green */
  .G { color: #f39c12; }   /* Orange */
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

  #result {
    margin-top: 20px;
    font-weight: bold;
    font-size: 18px;
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

<script>
  const BACKEND_URL = "http://127.0.0.1:8504/api";
  let correctMutation = null;

  const renderSequence = (sequence) => {
    const box = document.getElementById("dna-sequence");
    box.innerHTML = "";
    for (let char of sequence) {
      const span = document.createElement("span");
      if ("ATCG".includes(char)) {
        span.className = char;
        span.textContent = char;
      } else {
        span.className = "underscore";
        span.textContent = "_";
      }
      box.appendChild(span);
    }
  };

  window.onload = async function () {
    try {
      const res = await fetch(`${BACKEND_URL}/get-sequence`);
      if (!res.ok) throw new Error("Network error");
      const data = await res.json();
      document.getElementById("sequence-status").textContent = "Sequence loaded:";
      renderSequence(data.sequence);
      correctMutation = data.mutation;
    } catch (error) {
      console.error("Failed to load sequence:", error);
      document.getElementById("sequence-status").textContent = "❌ Error loading sequence.";
      renderSequence("______");
    }
  };

  document.getElementById("mutation-form").onsubmit = async function (e) {
    e.preventDefault();
    const guess = new FormData(e.target).get("mutation");

    try {
      const res = await fetch(`${BACKEND_URL}/check-mutation`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ guess, correct: correctMutation })
      });
      const result = await res.json();
      document.getElementById("result").textContent = result.message;
    } catch (error) {
      console.error("Error submitting guess:", error);
      document.getElementById("result").textContent = "❌ Error submitting guess.";
    }
  };
</script>
