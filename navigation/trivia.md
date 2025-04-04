---
layout: tailwind
title: Trivia Game
permalink: /trivia/
show_reading_time: false
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trivia Game</title>
    <link rel="stylesheet" href="{{ site.baseurl }}/assets/css/style.css">
</head>
<body>
    <h1>Biology Trivia Game 🎉</h1>
    <p>Test your knowledge of biotechnology! Answer as many questions as you can before time runs out.</p>
    <label for="username"><strong>Enter your name:</strong></label>
    <input type="text" id="username" placeholder="Your name..." required>
    <label for="difficulty"><strong>Choose Difficulty:</strong></label>
    <select id="difficulty">
        <option value="easy">Easy</option>
        <option value="medium" selected>Medium</option>
        <option value="hard">Hard</option>
    </select>
    <button id="start-btn">Start Game</button>
    <h2>Time Left: <span id="timer">60</span> seconds</h2>
    <div id="message-box"></div>
    <div id="question-container"></div>
    <h2>Leaderboard 🏆</h2>
    <ul id="leaderboard"></ul>
    <script type="module">
        // filepath: /home/gabrielac/nighthawk/illumina_dna/navigation/trivia.md
        import { pythonURI, fetchOptions } from '{{ site.baseurl }}/assets/js/api/config.js';
        let username = "";
        let score = 0;
        let timer;
        let timeLeft = 60; // Game duration in seconds
        function startGame() {
            let nameInput = document.getElementById("username").value.trim();
            if (!nameInput) {
                showMessage("Please enter your name to start.", "error");
                return;
            }
            username = nameInput;
            score = 0;
            timeLeft = 60;
            document.getElementById("timer").textContent = timeLeft;
            startTimer();
            fetchQuestion(); // Fetch the first question
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
            let difficulty = document.getElementById("difficulty").value;
            fetch(`${pythonURI}/api/get_question?difficulty=${difficulty}`, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    displayQuestion(data);
                })
                .catch(() => showMessage("Error loading question. Please try again.", "error"));
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
                if (timeLeft > 0) fetchQuestion(); // Fetch next question
            }, 500);
        }
        function endGame() {
            showMessage(`Game over! Final Score: ${score}`, "info");
            submitScore();
        }
        function submitScore() {
            fetch(`${pythonURI}/api/submit_scores`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username: username, score: score })
            }).then(response => response.json())
              .then(() => loadLeaderboard());
        }
        function loadLeaderboard() {
            fetch(`${pythonURI}/api/get_scores`, fetchOptions)
                .then(response => response.json())
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
        loadLeaderboard();
    </script>
</body>

<style>
/* filepath: /home/gabrielac/nighthawk/illumina_dna/navigation/trivia.md */
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
    transition: 0.3s;
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
</style>
