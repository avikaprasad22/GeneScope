---
layout: tailwind
permalink: /risk-quiz/
author: Nora Ahadian
show_reading_time: false
menu: nav/home.html
---

<style>
  /* Glowing nav button style */
  .nav-btn {
    position: relative;
    padding: 10px 20px;
    border-radius: 7px;
    border: 1px solid rgb(61, 106, 255);
    font-size: 14px;
    text-transform: uppercase;
    font-weight: 600;
    letter-spacing: 2px;
    background: transparent;
    color: black;
    overflow: hidden;
    box-shadow: 0 0 0 0 transparent;
    transition: all 0.2s ease-in;
  }

  .nav-btn:hover {
    background: rgb(61, 106, 255);
    box-shadow: 0 0 30px 5px rgba(0, 142, 236, 0.815);
    color: black;
  }

  .nav-btn:hover::before {
    animation: sh02 0.5s 0s linear;
  }

  .nav-btn::before {
    content: '';
    display: block;
    width: 0px;
    height: 86%;
    position: absolute;
    top: 7%;
    left: 0%;
    opacity: 0;
    background: #fff;
    box-shadow: 0 0 50px 30px #fff;
    transform: skewX(-20deg);
  }

  @keyframes sh02 {
    from {
      opacity: 0;
      left: 0%;
    }

    50% {
      opacity: 1;
    }

    to {
      opacity: 0;
      left: 100%;
    }
  }

  .nav-btn:active {
    box-shadow: 0 0 0 0 transparent;
    transition: box-shadow 0.2s ease-in;
  }

  /* Button text & page styles */
  h1, p, label, span, input, button {
    color: black;
  }

  .span {
    transform: skewX(15deg);
  }

  .second {
    margin-left: 10px;
  }
</style>

<div class="max-w-3xl mx-auto px-4 py-10">
  <div class="bg-white shadow-md rounded-lg p-6 border border-gray-200">
    <h1 class="text-2xl font-bold text-center">🩺 Disease Risk Analysis Quiz</h1>
    <p class="mt-2 text-center text-base">Enter a disease to check your symptom risk level.</p>
    <form id="disease-form" onsubmit="startQuiz(event)" class="mt-6 flex flex-col gap-2">
      <input type="text" id="disease" placeholder="e.g., diabetes" required class="p-2 border border-gray-300 rounded text-base" />
      <button type="submit" class="nav-btn w-fit self-center mt-4">Start Quiz</button>
    </form>
    <form id="symptom-form" style="display:none;" onsubmit="submitSymptoms(event)" class="mt-6">
      <div id="symptom-questions"></div>
      <div class="flex justify-center">
        <button type="submit" id="submit-btn" style="display:none;" class="nav-btn mt-4">See Risk</button>
      </div>
    </form>

    <div id="result" class="mt-8 font-bold text-lg text-center text-black"></div>
  </div>
</div>

<script>
  const BACKEND_URL = "http://127.0.0.1:5329";
  let currentQuestionIndex = 0;
  let symptomList = [];
  const userAnswers = {};

  async function startQuiz(event) {
    event.preventDefault();
    const disease = document.getElementById("disease").value.trim();
    if (!disease) return;

    const result = document.getElementById("result");
    result.textContent = "";

    try {
      const res = await fetch(`${BACKEND_URL}/riskquiz/get_symptoms?disease=${encodeURIComponent(disease)}`);
      if (!res.ok) throw new Error("Disease not found.");
      const data = await res.json();

      if (!data.success) {
        result.innerText = "⚠️ Disease not found. Please try another.";
        return;
      }

      symptomList = data.symptoms;
      userAnswers["target_disease"] = data.matched_disease;

      document.getElementById("disease-form").style.display = "none";
      document.getElementById("symptom-form").style.display = "block";
      currentQuestionIndex = 0;
      renderQuestion(currentQuestionIndex);
    } catch (err) {
      result.innerText = "❌ Error loading symptoms.";
    }
  }

  function renderQuestion(index) {
    const container = document.getElementById("symptom-questions");
    container.innerHTML = "";
    if (index >= symptomList.length) return;

    const symptom = symptomList[index];
    const label = symptom.replace(/_/g, ' ');

    container.innerHTML = `
      <p class="text-lg font-semibold mb-2 text-center">${label}</p>
      <div class="flex justify-center gap-6 mb-4">
        <label><input type="radio" name="${symptom}" value="1" ${userAnswers[symptom] === 1 ? "checked" : ""}/> Yes</label>
        <label><input type="radio" name="${symptom}" value="0" ${userAnswers[symptom] === 0 ? "checked" : ""}/> No</label>
      </div>
      <div class="flex justify-center gap-4">
        ${index > 0 ? `<button type="button" class="nav-btn" onclick="goBack()">← Back</button>` : ""}
        <button type="button" class="nav-btn" onclick="nextQuestion('${symptom}')">Next →</button>
      </div>
      <div class="flex justify-center mt-4">
        <button type="button" class="text-sm text-blue-700 underline hover:text-blue-900" onclick="restartQuiz()">
          ← Restart Quiz
        </button>
      </div>
    `;
  }

  function nextQuestion(symptom) {
    const value = document.querySelector(`input[name="${symptom}"]:checked`);
    if (!value) return alert("Please select an answer");
    userAnswers[symptom] = parseInt(value.value);
    currentQuestionIndex++;

    if (currentQuestionIndex < symptomList.length) {
      renderQuestion(currentQuestionIndex);
    } else {
      document.getElementById("symptom-questions").innerHTML = "<p class='text-center text-xl font-semibold'>All questions answered!</p>";
      document.getElementById("submit-btn").style.display = "inline-flex";
    }
  }

  function goBack() {
    if (currentQuestionIndex > 0) {
      currentQuestionIndex--;
      renderQuestion(currentQuestionIndex);
    }
  }

  const baseUrl = "{{ site.baseurl }}";

  function restartQuiz() {
    window.location.href = baseUrl + "/risk-quiz/";
  }

  async function submitSymptoms(event) {
    event.preventDefault();
    const result = document.getElementById("result");

    try {
      const res = await fetch(`${BACKEND_URL}/riskquiz/predict`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userAnswers)
      });

      if (!res.ok) {
        result.innerText = "❌ Error predicting risk.";
        return;
      }

      const data = await res.json();
      result.innerText = `📊 Likelihood of ${userAnswers["target_disease"]}: ${data.risk.toFixed(2)}%`;

      if (data.risk > 50) {
        const warning = document.createElement("div");
        warning.className = "text-red-700 font-bold mt-2";
        warning.innerText = "⚠️ High risk! Please consult a healthcare professional.";
        result.appendChild(warning);
      }
    } catch (err) {
      result.innerText = "❌ Network error.";
    }
  }
</script>