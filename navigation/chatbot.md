---
layout: tailwind
permalink: /risk-quiz/
author: Nora Ahadian
show_reading_time: false
menu: nav/home.html
---



  <form id="disease-form" onsubmit="startQuiz(event)" class="mt-6 flex flex-col gap-2">
    <input type="text" id="disease" placeholder="e.g., diabetes" required
      class="p-2 border border-gray-300 rounded text-gray-900 text-base" />
    <button type="submit"
      class="p-2 bg-green-600 text-white rounded-md text-base hover:bg-green-700">Start Quiz</button>
  </form>

  <form id="symptom-form" style="display:none;" onsubmit="submitSymptoms(event)" class="flex flex-col gap-4 mt-4">
    <div id="symptom-questions" class="mt-4"></div>
    <button type="submit"
      class="p-2 bg-green-600 text-white rounded-md text-base hover:bg-green-700">Submit Answers</button>
  </form>

  <div id="result" class="mt-6 font-bold text-lg text-gray-900"></div>
</div>

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
          <label class="block font-medium">${label}</label>
          <div class="flex gap-4 mt-1">
            <label class="flex items-center gap-1">
              <input type="radio" name="${symptom}" value="1" required class="accent-green-600" /> Yes
            </label>
            <label class="flex items-center gap-1">
              <input type="radio" name="${symptom}" value="0" class="accent-green-600" /> No
            </label>
          </div>
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
      warning.className = 'text-red-700 font-bold mt-2';
      warning.textContent = "⚠️ High risk! Please consult a healthcare professional.";
      result.appendChild(warning);
    }
  }
</script>
