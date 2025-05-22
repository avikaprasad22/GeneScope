---
layout: tailwind
permalink: /risk-quiz/
author: Nora Ahadian
show_reading_time: false
menu: nav/home.html
---

<style>
  .question-slide {
    transition: transform 0.5s ease-in-out;
  }
  .hidden-slide {
    transform: translateX(-100%);
    display: none;
  }
  .cta {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 11px 33px;
    font-size: 20px;
    color: white;
    background: linear-gradient(135deg, #1b2e75, #2aa5d8);
    transition: 0.4s ease-in-out;
    box-shadow: 6px 6px 0 #0a1d55;
    transform: skewX(-15deg);
    border: none;
    cursor: pointer;
    border-radius: 6px;
    margin: 0 auto;
    margin-top: 24px;
  }
  .cta:hover {
    box-shadow: 10px 10px 0 #00c6ff;
    background: linear-gradient(135deg, #0c1a47, #1ca3ec);
  }
  .cta .second {
    transition: 0.5s;
    margin-right: 0;
  }
  .cta:hover .second {
    margin-right: 45px;
  }
  .span {
    transform: skewX(15deg);
  }
  .second {
    width: 20px;
    margin-left: 30px;
    position: relative;
    top: 12%;
  }
  .one, .two, .three {
    transition: 0.4s;
    transform: translateX(-60%);
  }
  .cta:hover .three { animation: color_anim 1s infinite 0.2s; }
  .cta:hover .one { transform: translateX(0%); animation: color_anim 1s infinite 0.6s; }
  .cta:hover .two { transform: translateX(0%); animation: color_anim 1s infinite 0.4s; }
  @keyframes color_anim {
    0% { fill: white; } 50% { fill: #fbc638; } 100% { fill: white; }
  }
  h1, p, label, span, input, button {
    color: black ;
  }
</style>

<div class="max-w-3xl mx-auto px-4 py-10">
  <div class="bg-white shadow-md rounded-lg p-6 border border-gray-200">
    <h1 class="text-2xl font-bold text-center">🩺 Disease Risk Analysis Quiz</h1>
    <p class="mt-2 text-center text-base">Enter a disease to check your symptom risk level.</p>
    <form id="disease-form" onsubmit="startQuiz(event)" class="mt-6 flex flex-col gap-2">
      <input type="text" id="disease" placeholder="e.g., diabetes" required
        class="p-2 border border-gray-300 rounded text-base" />
      <button type="submit" class="p-2 bg-green-600 text-white rounded-md text-base hover:bg-green-700">Start Quiz</button>
    </form>
    <form id="symptom-form" style="display:none;" onsubmit="submitSymptoms(event)" class="mt-6">
      <div id="symptom-questions"></div>
      <div class="flex justify-center">
        <button type="submit" id="submit-btn" style="display: none;" class="cta">
          <span class="span">SEE RISK</span>
          <span class="second">
            <svg width="50px" height="20px" viewBox="0 0 66 43" xmlns="http://www.w3.org/2000/svg">
              <g id="arrow" fill="none" fill-rule="evenodd">
                <path class="one" d="M40.15,3.89L43.98,0.14..." fill="#FFFFFF"></path>
                <path class="two" d="M20.15,3.89L23.98,0.14..." fill="#FFFFFF"></path>
                <path class="three" d="M0.15,3.89L3.98,0.14..." fill="#FFFFFF"></path>
              </g>
            </svg>
          </span>
        </button>
      </div>
    </form>
    <div id="result" class="mt-8 font-bold text-lg text-center text-black"></div>
  </div>
</div>

<script>
  const BACKEND_URL = "http://127.0.0.1:8504";
  let currentQuestionIndex = 0;
  let symptomList = [];
  const userAnswers = {};

  async function startQuiz(event) {
    event.preventDefault();
    const disease = document.getElementById("disease").value.trim();
    if (!disease) return;

    const res = await fetch(`${BACKEND_URL}/riskquiz/get_symptoms?disease=${encodeURIComponent(disease)}`);
    const data = await res.json();
    const result = document.getElementById("result");

    if (!data.success) {
      result.innerText = "⚠️ Disease not found. Please try another.";
      return;
    }

    symptomList = data.symptoms;
    document.getElementById("disease-form").style.display = "none";
    document.getElementById("symptom-form").style.display = "block";
    renderQuestion(currentQuestionIndex);
  }

  function renderQuestion(index) {
    const container = document.getElementById("symptom-questions");
    container.innerHTML = "";
    if (index >= symptomList.length) return;

    const symptom = symptomList[index];
    const label = symptom.replace(/_/g, ' ');

    const block = document.createElement("div");
    block.className = "question-slide";
    block.innerHTML = `
      <p class="text-lg font-semibold mb-2 text-center">${label}</p>
      <div class="flex justify-center gap-6">
        <label class="flex items-center gap-2">
          <input type="radio" name="${symptom}" value="1" required /> <span>Yes</span>
        </label>
        <label class="flex items-center gap-2">
          <input type="radio" name="${symptom}" value="0" /> <span>No</span>
        </label>
      </div>
      <div class="flex justify-center">
        <button type="button" class="cta" onclick="nextQuestion('${symptom}')">
          <span class="span">NEXT</span>
          <span class="second">→</span>
        </button>
      </div>
    `;
    container.appendChild(block);
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

  async function submitSymptoms(event) {
    event.preventDefault();
    const result = document.getElementById("result");
    userAnswers["target_disease"] = document.getElementById("disease").value.trim();

    const res = await fetch(`${BACKEND_URL}/riskquiz/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userAnswers)
    });

    if (!res.ok) {
      const text = await res.text();
      console.error("Error predicting:", text);
      result.innerText = "Error getting prediction.";
      return;
    }

    const data = await res.json();
    result.innerText = `📊 Likelihood of ${userAnswers["target_disease"]}: ${data.risk.toFixed(2)}%`;

    if (data.risk > 50) {
      const warning = document.createElement('div');
      warning.className = 'text-red-700 font-bold mt-2';
      warning.textContent = "⚠️ High risk! Please consult a healthcare professional.";
      result.appendChild(warning);
    }
  }
</script>