---
layout: tailwind
title: Trivia Game
permalink: /trivia/
show_reading_time: false
menu: nav/home.html
---
<head>
  <title>Trivia Game</title>
  <style>
    body {
        font-family: 'Arial', sans-serif;
        text-align: center;
        font-size: 18px;
        line-height: 1.6;
        background-color: #f4f4f4;
        color: #333;
    }
    h1 {
        font-size: 28px;
        color: #0077cc;
    }
    button {
        padding: 12px 20px;
        margin: 15px;
        cursor: pointer;
        font-size: 18px;
        border: none;
        background-color: #0077cc;
        color: white;
        border-radius: 8px;
        transition: background 0.3s;
    }
    button:hover {
        background-color: #005fa3;
    }
    input, select {
        padding: 10px;
        font-size: 16px;
        margin: 10px;
        width: 200px;
    }
    #question-container {
        margin-top: 20px;
        background: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        display: inline-block;
        max-width: 600px;
    }
    .question-box p {
        font-size: 20px;
        font-weight: bold;
        color: #000;
    }
    .answer-btn {
        display: block;
        width: 90%;
        margin: 8px auto;
        padding: 10px;
        font-size: 16px;
        background-color: #28a745;
        color: white;
        border-radius: 6px;
        transition: background 0.3s;
    }
    .answer-btn:hover {
        background-color: #218838;
    }
    ul {
        list-style-type: none;
        font-size: 16px;
        padding: 0;
    }
    ul li {
        background: white;
        margin: 5px auto;
        padding: 10px;
        max-width: 300px;
        border-radius: 6px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        color: #000;
        font-weight: bold;
    }
    #message-box {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        padding: 10px;
    }
    .success {
        color: green;
    }
    .error {
        color: red;
    }
    .info {
        color: #0077cc;
    }
    #timer {
        font-size: 22px;
        font-weight: bold;
        color: #d9534f;
    }
    #loader {
        display: none;
        margin: 30px auto;
    }
    .spinner {
        border: 8px solid #f3f3f3;
        border-top: 8px solid #0077cc;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        animation: spin 1s linear infinite;
        margin: 0 auto;
    }
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    .loading-text {
        margin-top: 10px;
        font-size: 18px;
        color: #0077cc;
    }
  </style>
</head>
<body>
  <h1>Biology Trivia Game 🎉</h1>
  <p>Test your knowledge of biotechnology! Answer as many questions as you can before time runs out.</p>

  <label for="username"><strong>Enter your name:</strong></label>
  <input type="text" id="username" placeholder="Your name..." required />

  <label for="difficulty"><strong>Choose Difficulty:</strong></label>
  <select id="difficulty">
    <option value="easy">Easy</option>
    <option value="medium" selected>Medium</option>
    <option value="hard">Hard</option>
  </select>

  <button id="start-btn">Start Game</button>
  <button id="restart-btn" style="display: none;">Play Again</button>

  <h2>Time Left: <span id="timer">60</span> seconds</h2>
  <div id="message-box"></div>
  <div id="question-container"></div>

  <div id="loader">
    <div class="spinner"></div>
    <div class="loading-text">Loading questions...</div>
  </div>

  <h2>Leaderboard 🏆</h2>
  <ul id="leaderboard"></ul>

  <script type="module">
    import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';

    let username = "";
    let score = 0;
    let timer;
    let timeLeft = 60;
    let currentQuestionIndex = 0;
    let allQuestions = [];

    function startGame() {
        let nameInput = document.getElementById("username").value.trim();
        if (!nameInput) {
            showMessage("Please enter your name to start.", "error");
            return;
        }

        username = nameInput;
        score = 0;
        timeLeft = 60;
        currentQuestionIndex = 0;
        allQuestions = [];

        document.getElementById("start-btn").style.display = "none";
        document.getElementById("restart-btn").style.display = "none";
        document.getElementById("username").disabled = true;
        document.getElementById("difficulty").disabled = true;
        document.getElementById("timer").textContent = timeLeft;
        document.getElementById("loader").style.display = "block";
        document.getElementById("question-container").innerHTML = "";

        fetch(`${pythonURI}/api/get_questions`, fetchOptions)
            .then(res => res.json())
            .then(data => {
                allQuestions = data;
                document.getElementById("loader").style.display = "none";
                startTimer();
                fetchQuestion();
            })
            .catch(() => {
                showMessage("Failed to load questions. Try again.", "error");
                document.getElementById("loader").style.display = "none";
                document.getElementById("start-btn").style.display = "inline-block";
            });
    }

    function startTimer() {
        clearInterval(timer);
        timer = setInterval(() => {
            timeLeft--;
            document.getElementById("timer").textContent = timeLeft;
            if (timeLeft <= 0) {
                clearInterval(timer);
                endGame();
            }
        }, 1000);
    }

    function fetchQuestion() {
        if (currentQuestionIndex >= allQuestions.length) {
            endGame();
            return;
        }

        displayQuestion(allQuestions[currentQuestionIndex]);
        currentQuestionIndex++;
    }

    function displayQuestion(data) {
        let container = document.getElementById("question-container");
        container.innerHTML = `
            <div class="question-box">
                <p><strong>${data.question}</strong></p>
            </div>
        `;
        data.options.forEach(option => {
            let button = document.createElement("button");
            button.textContent = option;
            button.className = "answer-btn";
            button.onclick = () => checkAnswer(option, data.correct_answer);
            container.appendChild(button);
        });
    }

    function checkAnswer(selected, correct) {
        if (selected === correct) {
            score += 10;
            showMessage("✅ Correct!", "success");
        } else {
            showMessage(`❌ Wrong! Correct answer: ${correct}`, "error");
        }

        setTimeout(() => {
            if (timeLeft > 0) fetchQuestion();
        }, 500);
    }

    function endGame() {
        showMessage(`🎉 Congratulations, ${username}! You scored ${score} points!`, "info");
        submitScore();
        document.getElementById("restart-btn").style.display = "inline-block";
        document.getElementById("username").disabled = false;
        document.getElementById("difficulty").disabled = false;
    }

    function submitScore() {
        fetch(`${pythonURI}/api/submit_scores`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username: username, score: score })
        }).then(res => res.json())
          .then(() => loadLeaderboard());
    }

    function loadLeaderboard() {
        fetch(`${pythonURI}/api/get_scores`, fetchOptions)
            .then(res => res.json())
            .then(data => {
                let leaderboard = document.getElementById("leaderboard");
                leaderboard.innerHTML = "";
                data.forEach(entry => {
                    let li = document.createElement("li");
                    li.textContent = `${entry.username}: ${entry.score} pts`;
                    leaderboard.appendChild(li);
                });
            });
    }

    function showMessage(message, type) {
        let messageBox = document.getElementById("message-box");
        messageBox.textContent = message;
        messageBox.className = type;
        setTimeout(() => messageBox.textContent = "", 2000);
    }

    document.getElementById("start-btn").addEventListener("click", startGame);
    document.getElementById("restart-btn").addEventListener("click", () => {
        document.getElementById("restart-btn").style.display = "none";
        document.getElementById("start-btn").style.display = "inline-block";
        document.getElementById("username").disabled = false;
        document.getElementById("difficulty").disabled = false;
        document.getElementById("question-container").innerHTML = "";
        document.getElementById("message-box").textContent = "";
        document.getElementById("timer").textContent = "60";
    });

    loadLeaderboard();
  </script>
</body>
</html>
