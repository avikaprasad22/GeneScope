---
layout: tailwind
permalink: /college/
show_reading_time: false
menu: nav/home.html
---

<title>Top College Match Quiz</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap" rel="stylesheet">

<style>
  body {
    font-family: 'Montserrat', sans-serif;
    color: #2a2a2a;
    padding: 20px;
    overflow-x: hidden;
  }

  h1, h2, h3 {
    text-align: center;
    color: rgb(38, 80, 138);
  }

  label {
    color: #1b1b1b; /* ✅ Darker text for quiz questions */
    font-weight: 500;
    display: block;
    margin-bottom: 10px;
  }

  .college-quiz-section {
    background-color: #e0f7fa;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
    max-width: 750px;
    margin: 40px auto;
    animation: slideUp 0.8s ease-out;
  }

  .college-quiz-section h3 {
    font-size: 1.4rem;
    margin-bottom: 20px;
    color: #00796b;
  }

  select {
    width: 100%;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid #a7c0cd;
    margin-bottom: 20px;
    font-size: 1rem;
  }

  .college-quiz-button {
    background: #00796b;
    color: #fff;
    padding: 14px 28px;
    font-size: 1rem;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: block;
    margin: 0 auto;
    animation: glowPulse 2s infinite ease-in-out;
  }

  .college-quiz-button:hover {
    background-color: #004d40;
    transform: scale(1.05);
  }

  #college-result {
    display: none;
    background-color: rgb(38, 37, 35);
    margin-top: 30px;
    padding: 25px;
    border: 2px dashed #ffb74d;
    border-radius: 20px;
    animation: fadeIn 0.6s ease-in-out;
    max-width: 750px;
    margin-left: auto;
    margin-right: auto;
  }

  #college-website-button {
    background-color: #f57c00;
    color: white;
    padding: 10px 20px;
    margin-top: 15px;
    border-radius: 10px;
    font-weight: bold;
    border: none;
    cursor: pointer;
    transition: background 0.3s ease;
  }

  #college-website-button:hover {
    background-color: #ef6c00;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  @keyframes slideUp {
    0% { transform: translateY(50px); opacity: 0; }
    100% { transform: translateY(0); opacity: 1; }
  }

  @keyframes glowPulse {
    0% { box-shadow: 0 0 10px #00796b; }
    50% { box-shadow: 0 0 25px #004d40; }
    100% { box-shadow: 0 0 10px #00796b; }
  }
</style>

<!-- College Quiz Section -->
<div class="college-quiz-section">
  <h3>Take this quick quiz to discover your top college for Biotechnology! 🎓</h3>
  <form id="college-form">
    <label><strong>1.</strong> What campus setting do you prefer?</label>
    <select name="setting" required>
      <option value="">Select one</option>
      <option value="Urban">Urban</option>
      <option value="Suburban">Suburban</option>
      <option value="Rural">Rural</option>
    </select>
    <label><strong>2.</strong> Do you prefer a public or private institution?</label>
    <select name="type" required>
      <option value="">Select one</option>
      <option value="Public">Public</option>
      <option value="Private not-for-profit">Private</option>
    </select>
    <label><strong>3.</strong> Which region are you most interested in?</label>
    <select name="region" required>
      <option value="">Select one</option>
      <option value="Northeast">Northeast</option>
      <option value="Midwest">Midwest</option>
      <option value="South">South</option>
      <option value="West">West</option>
    </select>
    <label><strong>4.</strong> What size college are you most comfortable with?</label>
    <select name="size" required>
      <option value="">Select one</option>
      <option value="Small">Small (&lt;5,000 students)</option>
      <option value="Medium">Medium (5,000–15,000 students)</option>
      <option value="Large">Large (&gt;15,000 students)</option>
    </select>
    <label><strong>5.</strong> Are you interested in doing biotechnology research as an undergraduate?</label>
    <select name="research" required>
      <option value="">Select one</option>
      <option value="Yes">Yes</option>
      <option value="No">No</option>
    </select>
    <button type="button" class="college-quiz-button" onclick="getTopCollege()">Find My Best Match</button>
  </form>
</div>
<!-- Biotech Info Pop-up -->
<div id="biotech-popup" class="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-60 hidden">
  <div class="bg-white text-black p-6 rounded-2xl shadow-xl max-w-xl w-full relative">
    <button onclick="closePopup()" class="absolute top-2 right-3 text-gray-500 hover:text-black text-2xl font-bold">&times;</button>
    <h2 class="text-2xl font-semibold mb-3">🔬 What is Biotechnology?</h2>
    <p class="mb-4 text-sm leading-relaxed">
      Biotechnology is a field that uses living organisms and biological systems to develop products and technologies that improve lives and the environment. It spans careers in medicine, agriculture, data science, and more!
    </p>
    <button onclick="closePopup()" class="mt-3 bg-teal-500 hover:bg-teal-600 text-white px-4 py-2 rounded-md shadow transition">
      Got it!
    </button>
  </div>
</div>

<!-- Reopen Button -->
<button onclick="openPopup()" id="reopen-popup-btn"
  style="position: fixed; top: 120px; right: 24px; background-color: #14b8a6; 
         color: white; padding: 8px 16px; border-radius: 9999px; 
         box-shadow: 0 4px 6px rgba(0,0,0,0.1); z-index: 9999;">
  ℹ️ About Biotech
</button>

<!-- College Result Section -->
<div id="college-result" class="college-quiz-section">
  <h2>Your Top College Match 🎯</h2>
  <p id="college-description"></p>
  <button id="college-website-button" style="display:none;" onclick="window.open('', '_blank')">Visit Website</button>
</div>

<script>
async function getTopCollege() {
  const form = document.getElementById("college-form");

  const setting = encodeURIComponent(form.elements["setting"].value);
  const type = encodeURIComponent(form.elements["type"].value);
  const region = encodeURIComponent(form.elements["region"].value);
  const size = encodeURIComponent(form.elements["size"].value);
  const research = encodeURIComponent(form.elements["research"].value);

  const resultDiv = document.getElementById("college-result");
  const descText = document.getElementById("college-description");
  const websiteButton = document.getElementById("college-website-button");

  try {
    const url = `http://127.0.0.1:8504/api/get_colleges?campus_setting=${setting}&college_type=${type}&region=${region}&size=${size}&research=${research}`;
    const res = await fetch(url);
    const data = await res.json();

    if (data.colleges && data.colleges.length > 0) {
      const top = data.colleges[0];
      resultDiv.style.display = "block";
      descText.innerHTML = `<strong>${top.organizationName}</strong><br><br>${top.description}`;
      websiteButton.style.display = "inline-block";
      websiteButton.onclick = () => window.open(top.website, '_blank');
    } else {
      resultDiv.style.display = "block";
      descText.innerText = "No matching college found for your preferences.";
      websiteButton.style.display = "none";
    }
  } catch (err) {
    console.error("Error fetching college:", err);
    resultDiv.style.display = "block";
    descText.innerText = "Error retrieving data.";
    websiteButton.style.display = "none";
  }
}
window.addEventListener('DOMContentLoaded', () => {
  const popupShown = sessionStorage.getItem('biotechPopupShown');
  if (!popupShown) {
    document.getElementById('biotech-popup').classList.remove('hidden');
    sessionStorage.setItem('biotechPopupShown', 'true');
  }
});

function closePopup() {
  document.getElementById('biotech-popup').classList.add('hidden');
}

function openPopup() {
  document.getElementById('biotech-popup').classList.remove('hidden');
}
