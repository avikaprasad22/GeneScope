---
layout: tailwind
permalink: /risk-quiz/
menu: nav/home.html
author: Nora Ahadian
show_reading_time: false
---

<style>
  body {
    background-color: #ffffff;
    color: #1a202c;
  }

  form {
    margin-top: 25px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  input[type="text"] {
    padding: 8px;
    border: 1px solid #ccc;
    font-size: 16px;
    border-radius: 4px;
    color: #1a202c;
  }

  button {
    padding: 10px;
    background: #4CAF50;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
  }

  button:hover {
    background-color: #45a049;
  }

  .question-block {
    margin-top: 15px;
  }

  .result, .warning {
    margin-top: 20px;
    font-weight: bold;
    font-size: 18px;
    color: #1a202c;
  }

  .warning {
    color: #b91c1c;
  }
</style>


# 🧬 SymbiBot Disease Risk Quiz

<p>Type a disease to begin. You’ll be asked about related symptoms, and then we’ll predict your risk.</p>

<form id="disease-form" onsubmit="startQuiz(event)">
  <input type="text" id="disease" placeholder="e.g., diabetes" required />
  <button type="submit">Start Quiz</button>
</form>

<form id="symptom-form" style="display:none;" onsubmit="submitSymptoms(event)">
  <div id="symptom-questions" class="question-block"></div>
  <button type="submit">Submit Answers</button>
</form>

<div id="result" class="result"></div>

<script>
  const BACKEND_URL = "http://127.0.0.1:8504";

  async function startQuiz(event) {
    event.preventDefault();
    const disease = document.getElementById("disease").value.trim();
    if (!disease) return;

    const res = await fetch(`${BACKEND_URL}/chatbot/get_symptoms?disease=${encodeURIComponent(disease)}`);
    if (!res.ok) {
      const text = await res.text();
      console.error("❌ Error fetching symptoms:", text);
      return;
    }
    const data = await res.json();

    const result = document.getElementById("result");
    if (!data.success) {
      result.textContent = "⚠️ Disease not found. Please try another.";
      return;
    }

    result.textContent = '';
    const questionsDiv = document.getElementById("symptom-questions");
    questionsDiv.innerHTML = '';

    data.symptoms.forEach(symptom => {
      const label = symptom.replace(/_/g, ' ');
      questionsDiv.innerHTML += `
        <div>
          <label>${label}</label><br>
          <input type="radio" name="${symptom}" value="1" required> Yes
          <input type="radio" name="${symptom}" value="0"> No
        </div>
      `;
    });

    document.getElementById("symptom-form").style.display = "block";
  }

  async function submitSymptoms(event) {
    event.preventDefault();
    const form = document.getElementById("symptom-form");
    const formData = new FormData(form);
    const payload = {};
    formData.forEach((value, key) => {
      payload[key] = parseInt(value);
    });

    payload["target_disease"] = document.getElementById("disease").value.trim();

    const res = await fetch(`${BACKEND_URL}/chatbot/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) {
      const text = await res.text();
      console.error("❌ Error predicting:", text);
      return;
    }

    const data = await res.json();
    const result = document.getElementById("result");
    result.innerText = `📊 Likelihood of ${payload["target_disease"]}: ${data.risk.toFixed(2)}%`;

    if (data.risk > 50) {
      const warning = document.createElement('div');
      warning.className = 'warning';
      warning.textContent = "⚠️ High risk! Please consult a healthcare professional.";
      result.appendChild(warning);
    }
  }
</script>
