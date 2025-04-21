---
layout: tailwind
permalink: /career/
show_reading_time: false
menu: nav/home.html
---

<title>Biotechnology Career Quiz</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">

<style>
  body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg,rgb(0, 0, 0),rgb(0, 0, 0));
    color: #3b0d7d; /* Updated to match the title */
    padding: 20px;
  }

   h1 {
    font-family: 'Poppins', sans-serif;
    color:rgb(233, 221, 255); /* Title color set to white */
    text-align: center;
    margin-bottom: 10px;
  }

  h3 {
    color:rgb(232, 228, 249); /* Also matching for consistency */
  }

  label {
    font-weight: 500;
  }

  .quiz-section {
    background-color:rgb(87, 67, 217);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    max-width: 700px;
    margin: 20px auto;
  }

  button {
    background: #5b21b6;
    color: white;
    padding: 12px 24px;
    font-size: 16px;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    transition: background 0.3s ease;
    margin-top: 10px;
  }

  button:hover {
    background: #6d28d9;
  }

  #career-result {
    display: none;
    margin-top: 30px;
    padding: 25px;
    border: 2px dashedrgb(90, 67, 218);
    border-radius: 16px;
    background-color:rgb(73, 52, 167);
    animation: fadeIn 0.5s ease-in-out;
    max-width: 700px;
    margin-left: auto;
    margin-right: auto;
  }

  .spinner {
    margin-top: 10px;
    border: 4px solid #d1d5db;
    border-top: 4px solid #5b21b6;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
    display: inline-block;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>


<body>
  <h1>🔬 Biotechnology Career Quiz</h1>

  <div class="quiz-section">
    <h3>Answer these questions to discover your future career in Biotechnology💡:</h3>
    <form id="quiz-form">
      <p><strong>1.</strong> Are you interested in working with genetic data?</p>
      <input type="radio" name="q1" value="5"> Yes<br>
      <input type="radio" name="q1" value="0"> No<br><br>

      <p><strong>2.</strong> Do you enjoy conducting experiments in a lab?</p>
      <input type="radio" name="q2" value="5"> Yes<br>
      <input type="radio" name="q2" value="0"> No<br><br>

      <p><strong>3.</strong> Are you interested in coding and analyzing biological data?</p>
      <input type="radio" name="q3" value="5"> Yes<br>
      <input type="radio" name="q3" value="0"> No<br><br>

      <p><strong>4.</strong> Do you want to contribute to developing new medical treatments?</p>
      <input type="radio" name="q4" value="5"> Yes<br>
      <input type="radio" name="q4" value="0"> No<br><br>

      <p><strong>5.</strong> Are you curious about how living organisms function at the molecular level?</p>
      <input type="radio" name="q5" value="5"> Yes<br>
      <input type="radio" name="q5" value="0"> No<br><br>

      <button type="button" onclick="calculateScore()">Submit Quiz</button>
    </form>
  </div>

  <div id="career-result">
    <h2>Your Suggested Career in Biotechnology:</h2>
    <p id="career-result-text"></p>
    <div id="spinner" class="spinner" style="display: none;"></div>
  </div>

<script>
  let displayedCareers = new Set();
  let allCareers = [];
  let currentIndex = 0;

  async function calculateScore() {
    let score = 0;
    const form = document.getElementById("quiz-form");
    const radios = form.querySelectorAll('input[type="radio"]:checked');

    radios.forEach(radio => {
      score += parseInt(radio.value);
    });

    const biologyScore = Math.round((score / 25) * 100);

    const resultDiv = document.getElementById("career-result");
    const resultText = document.getElementById("career-result-text");
    const spinner = document.getElementById("spinner");

    resultDiv.style.display = "block";
    resultText.innerHTML = `<strong>🎓 Your quiz score:</strong> ${score} out of 25<br><strong>🧬 Estimated Biotechnology Score:</strong> ${biologyScore}/100<br><br>🔍 Finding the best match...`;
    spinner.style.display = "inline-block";

    const careerData = await fetchCareersByBiologyScore(biologyScore);

    spinner.style.display = "none";
    resultText.innerHTML += `<br><br>${careerData}`;
  }

  async function fetchCareersByBiologyScore(score) {
    try {
      const response = await fetch(`http://127.0.0.1:8504/api/get_careers?biology_score=${score}`);
      const result = await response.json();

      if (result && result.careers && result.careers.length > 0) {
        const careers = result.careers.filter(career => {
          const careerName = career.career_aspiration.toLowerCase();
          if (careerName !== "unknown" && !displayedCareers.has(careerName)) {
            displayedCareers.add(careerName);
            return true;
          }
          return false;
        });

        allCareers = careers;
        currentIndex = 0;
        return showCareers();
      } else {
        return "No matching career data found.";
      }
    } catch (error) {
      console.error("Error fetching career data:", error);
      return "Error fetching career data.";
    }
  }

  function showCareers() {
    const careersToShow = allCareers.slice(currentIndex, currentIndex + 5);
    currentIndex += careersToShow.length;

    const careersText = careersToShow.map(career => `${career.career_aspiration}`).join('<br>');
    let resultHTML = `Based on your answers, consider exploring:<br><strong>${careersText}</strong>`;

    if (currentIndex < allCareers.length) {
      resultHTML += `<br><br><button onclick="showMoreCareers()">Show More</button>`;
    }

    return resultHTML;
  }

  function showMoreCareers() {
    const careersToShow = allCareers.slice(currentIndex, currentIndex + 5);
    currentIndex += careersToShow.length;

    const careersText = careersToShow.map(career => `${career.career_aspiration}`).join('<br>');
    const resultText = document.getElementById("career-result-text");

    resultText.innerHTML += `<br><br><strong>${careersText}</strong>`;

    if (currentIndex >= allCareers.length) {
      const showMoreButton = document.querySelector("button");
      if (showMoreButton) showMoreButton.style.display = "none";
    }
  }
</script>
</body>
