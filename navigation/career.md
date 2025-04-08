---
layout: base
permalink: /career_aspirations/
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Biotechnology Career Quiz</title>
  <style>
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 20px;
    }
    th, td {
      border: 1px solid black;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f4f4f4;
    }
    .quiz-section {
      margin-top: 20px;
    }
  </style>
</head>
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

      <button type="button" onclick="calculateScore()">Submit Quiz</button>
    </form>
  </div>

  <div id="career-result" style="display:none; margin-top: 20px;">
    <h2>Your Suggested Career in Biotechnology:</h2>
    <p id="career-result-text"></p>
  </div>

  <script>
    async function calculateScore() {
      let score = 0;
      const form = document.getElementById("quiz-form");
      const radios = form.querySelectorAll('input[type="radio"]:checked');

      radios.forEach(radio => {
        score += parseInt(radio.value);
      });

      // Now, based on the score, fetch career data from the backend (subject scores)
      const careerData = await fetchCareersByScore(score);

      // Show the result
      document.getElementById("career-result-text").textContent = careerData;
      document.getElementById("career-result").style.display = "block";
    }

    async function fetchCareersByScore(score) {
      // Set a range based on quiz score (can adjust based on your preference)
      const biologyScoreRange = getBiologyScoreRange(score);
      
      try {
        // Send request to backend with score range to fetch matching careers
        const response = await fetch(`http://127.0.0.1:8504/api/get_careers?biology_score_min=${biologyScoreRange.min}&biology_score_max=${biologyScoreRange.max}`);
        const result = await response.json();

        if (result && result.careers) {
          // Process the careers and suggest the most frequent ones
          const careerCounts = {};
          result.careers.forEach(student => {
            const career = student.career_aspiration;
            careerCounts[career] = (careerCounts[career] || 0) + 1;
          });

          // Sort careers by most frequent
          const sortedCareers = Object.entries(careerCounts)
            .sort(([, countA], [, countB]) => countB - countA)
            .slice(0, 3);

          return `Based on your score, the top 3 career suggestions are: ${sortedCareers.map(([career]) => career).join(', ')}`;
        } else {
          return "No matching career data found.";
        }
      } catch (error) {
        console.error("Error fetching career data:", error);
        return "Error fetching career data.";
      }
    }

    function getBiologyScoreRange(score) {
      // Example of defining ranges based on quiz score (can be adjusted)
      if (score >= 15) return { min: 80, max: 100 };
      if (score >= 10) return { min: 60, max: 79 };
      return { min: 0, max: 59 };
    }
  </script>
</body>
</html>
