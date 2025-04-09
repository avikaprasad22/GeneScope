---
layout: tailwind
permalink: /career/
---

  <title>Biotechnology Career Quiz</title>
<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  th, td {
    border: 1px solid #4a6d87; /* Dull dark blue */
    padding: 10px;
    text-align: left;
  }
  th {
    background-color:rgb(17, 51, 123); /* Light blue */
  }
  .quiz-section {
    margin-top: 20px;
  }
  #career-result {
    display: none;
    margin-top: 20px;
    padding: 15px;
    border: 2px solid #4a6d87; /* Dull dark blue */
    border-radius: 10px;
    background-color:rgb(21, 20, 102); /* Light blue */
    animation: fadeIn 0.5s ease-in-out;
  }
  .spinner {
    margin-top: 10px;
    border: 4px solidrgb(0, 0, 0);
    border-top: 4px solid #4a6d87; /* Dull dark blue */
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
</style>

<body>
  <h1>Biotechnology Career Quiz</h1>

  <div class="quiz-section">
    <h3>Answer these questions to find your future career in Biotechnology:</h3>
    <form id="quiz-form">
      <label for="q1">1. Are you interested in working with genetic data?</label><br>
      <input type="radio" name="q1" value="5"> Yes<br>
      <input type="radio" name="q1" value="0"> No<br><br>

      <label for="q2">2. Do you enjoy conducting experiments in a lab?</label><br>
      <input type="radio" name="q2" value="5"> Yes<br>
      <input type="radio" name="q2" value="0"> No<br><br>

      <label for="q3">3. Are you interested in coding and analyzing biological data?</label><br>
      <input type="radio" name="q3" value="5"> Yes<br>
      <input type="radio" name="q3" value="0"> No<br><br>

      <label for="q4">4. Do you want to contribute to developing new medical treatments?</label><br>
      <input type="radio" name="q4" value="5"> Yes<br>
      <input type="radio" name="q4" value="0"> No<br><br>

      <label for="q5">5. Are you curious about how living organisms function at the molecular level?</label><br>
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
  let displayedCareers = new Set();  // Set to store unique career names that have been displayed
  let allCareers = []; // Array to store all available filtered careers
  let currentIndex = 0; // Track how many careers have been shown

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
    resultText.innerHTML = `<strong>Your quiz score:</strong> ${score} out of 25<br><strong>Estimated Biology Score:</strong> ${biologyScore}/100<br><br>Finding the best match...`;
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
        // Filter out "Unknown" and already displayed careers
        const careers = result.careers.filter(career => {
          const careerName = career.career_aspiration.toLowerCase();
          if (
            careerName !== "unknown" &&
            !displayedCareers.has(careerName)
          ) {
            displayedCareers.add(careerName);
            return true;
          }
          return false;
        });

        allCareers = careers;
        currentIndex = 0; // Reset for new quiz submission
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
    let resultHTML = `🎯 Based on your score, you might become:<br><strong>${careersText}</strong>`;

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

