---
layout: page 
permalink: /trivia/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trivia Game</title>
    <script type="module">
        import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
        let username, difficulty;
        let currentQuestion = null;
        let questionCount = 0;
        let totalQuestions = 5;  // Fixed number of questions per game
        let score = 0;
        let answered = false;  // Track if the user has already answered the current question
        function startGame() {
            username = document.getElementById("username").value.trim();
            difficulty = document.getElementById("difficulty").value;
            if (!username) {
                alert("Please enter your name!");
                return;
            }
            document.getElementById("startScreen").classList.add("hidden");
            document.getElementById("gameScreen").classList.remove("hidden");
            fetchQuestion();
        }
        function fetchQuestion() {
            if (questionCount >= totalQuestions) {
                endGame();
                return;
            }
            fetch(`${pythonURI}/api/trivia/question`, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById("questionText").textContent = "No questions available.";
                    } else if (data.difficulty === difficulty) {  
                        currentQuestion = data;
                        answered = false;  // Reset answered flag for the new question
                        displayQuestion();
                    } else {
                        fetchQuestion(); // Get another question if difficulty doesn't match
                    }
                })
                .catch(error => console.error("Error fetching question:", error));
        }
        function displayQuestion() {
            document.getElementById("questionText").textContent = currentQuestion.question;
            document.getElementById("optionA").textContent = `A: ${currentQuestion.options.A}`;
            document.getElementById("optionB").textContent = `B: ${currentQuestion.options.B}`;
            document.getElementById("optionC").textContent = `C: ${currentQuestion.options.C}`;
            document.getElementById("optionD").textContent = `D: ${currentQuestion.options.D}`;
            document.querySelectorAll(".answer-button").forEach(button => button.disabled = false);
        }
        function submitAnswer(option) {
            if (answered) return;  // Prevent multiple attempts
            answered = true;
            const selectedAnswer = currentQuestion.options[option];
            fetch(`${pythonURI}/api/trivia/answer`, {
                ...fetchOptions,
                method: "POST",
                body: JSON.stringify({
                    name: username,
                    question_id: currentQuestion.id,
                    selected_answer: selectedAnswer
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.correct) {
                    score += 10;
                    document.getElementById("feedback").textContent = "Correct!";
                } else {
                    document.getElementById("feedback").textContent = `Incorrect! The correct answer was: ${currentQuestion.correct_answer}`;
                }
                document.getElementById("score").textContent = score;
                document.querySelectorAll(".answer-button").forEach(button => button.disabled = true);
            })
            .catch(error => console.error("Error submitting answer:", error));
            questionCount++;
        }
        function nextQuestion() {
            document.getElementById("feedback").textContent = "";
            fetchQuestion();
        }
        function endGame() {
            document.getElementById("gameScreen").classList.add("hidden");
            document.getElementById("resultScreen").classList.remove("hidden");
            document.getElementById("finalScore").textContent = score;
            fetchLeaderboard();
        }
        function fetchLeaderboard() {
            fetch(`${pythonURI}/api/trivia/leaderboard`, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    const leaderboardList = document.getElementById("leaderboard");
                    leaderboardList.innerHTML = "";
                    data.forEach(entry => {
                        let li = document.createElement("li");
                        li.textContent = `${entry.name}: ${entry.total_score}`;
                        leaderboardList.appendChild(li);
                    });
                })
                .catch(error => console.error("Error fetching leaderboard:", error));
        }
        function restartGame() {
            resource.reload();
        }
        window.startGame = startGame;
        window.submitAnswer = submitAnswer;
        window.nextQuestion = nextQuestion;
        window.restartGame = restartGame;
    </script>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trivia Game</title>
    <script type="module">
        import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';
        let username, difficulty;
        let currentQuestion = null;
        let questionCount = 0;
        let totalQuestions = 5;  // Fixed number of questions per game
        let score = 0;
        let answered = false;  // Track if the user has already answered the current question
        function startGame() {
            username = document.getElementById("username").value.trim();
            difficulty = document.getElementById("difficulty").value;
            if (!username) {
                alert("Please enter your name!");
                return;
            }
            document.getElementById("startScreen").classList.add("hidden");
            document.getElementById("gameScreen").classList.remove("hidden");
            fetchQuestion();
        }
        function fetchQuestion() {
            if (questionCount >= totalQuestions) {
                endGame();
                return;
            }
            fetch(`${pythonURI}/api/trivia/question`, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById("questionText").textContent = "No questions available.";
                    } else if (data.difficulty === difficulty) {  
                        currentQuestion = data;
                        answered = false;  // Reset answered flag for the new question
                        displayQuestion();
                    } else {
                        fetchQuestion(); // Get another question if difficulty doesn't match
                    }
                })
                .catch(error => console.error("Error fetching question:", error));
        }
        function displayQuestion() {
            document.getElementById("questionText").textContent = currentQuestion.question;
            document.getElementById("optionA").textContent = `A: ${currentQuestion.options.A}`;
            document.getElementById("optionB").textContent = `B: ${currentQuestion.options.B}`;
            document.getElementById("optionC").textContent = `C: ${currentQuestion.options.C}`;
            document.getElementById("optionD").textContent = `D: ${currentQuestion.options.D}`;
            document.querySelectorAll(".answer-button").forEach(button => button.disabled = false);
        }
        function submitAnswer(option) {
            if (answered) return;  // Prevent multiple attempts
            answered = true;
            const selectedAnswer = currentQuestion.options[option];
            fetch(`${pythonURI}/api/trivia/answer`, {
                ...fetchOptions,
                method: "POST",
                body: JSON.stringify({
                    name: username,
                    question_id: currentQuestion.id,
                    selected_answer: selectedAnswer
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.correct) {
                    score += 10;
                    document.getElementById("feedback").textContent = "Correct!";
                } else {
                    document.getElementById("feedback").textContent = `Incorrect! The correct answer was: ${currentQuestion.correct_answer}`;
                }
                document.getElementById("score").textContent = score;
                document.querySelectorAll(".answer-button").forEach(button => button.disabled = true);
            })
            .catch(error => console.error("Error submitting answer:", error));
            questionCount++;
        }
        function nextQuestion() {
            document.getElementById("feedback").textContent = "";
            fetchQuestion();
        }
        function endGame() {
            document.getElementById("gameScreen").classList.add("hidden");
            document.getElementById("resultScreen").classList.remove("hidden");
            document.getElementById("finalScore").textContent = score;
            document.getElementById("topicsTable").classList.remove("hidden");
            fetchLeaderboard();
        }
        function fetchLeaderboard() {
            fetch(`${pythonURI}/api/trivia/leaderboard`, fetchOptions)
                .then(response => response.json())
                .then(data => {
                    const leaderboardList = document.getElementById("leaderboard");
                    leaderboardList.innerHTML = "";
                    data.forEach(entry => {
                        let li = document.createElement("li");
                        li.textContent = `${entry.name}: ${entry.total_score}`;
                        leaderboardList.appendChild(li);
                    });
                })
                .catch(error => console.error("Error fetching leaderboard:", error));
        }
        function restartGame() {
            location.reload();
        }
        window.startGame = startGame;
        window.submitAnswer = submitAnswer;
        window.nextQuestion = nextQuestion;
        window.restartGame = restartGame;
    </script>
</head>
<body>
    <div id="topicsTable" class="container hidden">
        <table id="demo" class="table">
            <thead>
                <tr>
                    <th>Topics</th>
                    <th>Resources</th>
                </tr>
            </thead>
            <tbody id="topicsResult">
            </tbody>
        </table>
    </div>
    <script>
        let topicsResultContainer = document.getElementById("topicsResult");
        let topicsOptions = {
            method: 'GET',
            mode: 'cors',
            cache: 'default',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
        };
        fetch(topicsUrl, topicsOptions)
            .then(response => {
                if (response.status !== 200) {
                    console.error(response.status);
                    return;
                }
                response.json().then(data => {
                    console.log(data);
                    for (const row of data.topic) {
                        const tr = document.createElement("tr");
                        const name = document.createElement("td");
                        const resource = document.createElement("td");
                        name.innerHTML = row.name;
                        resource.innerHTML = row.resource;
                        tr.appendChild(name);
                        tr.appendChild(resource);
                        topicsResultContainer.appendChild(tr);
                    }
                })
            })
    </script>
</body>
     <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');
        body {
            font-family: 'Montserrat', sans-serif;
            text-align: center;
            padding: 20px;
            background: linear-gradient(135deg, #74ebd5, #acb6e5);
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            max-width: 5000px;
            width: 105%;
            padding: 50px;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.95);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease-in-out;
        }
        .container:hover {
            transform: scale(1.02);
        }
        .hidden {
            display: none;
        }
        button {
            padding: 16px 24px;
            margin: 14px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            background: #3498db;
            color: white;
            font-size: 22px;
            font-weight: bold;
            transition: all 0.3s ease;
            box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2);
            font-family: 'Montserrat', sans-serif;
        }
        button:hover {
            background: #2980b9;
            transform: translateY(-2px);
        }
        button:disabled {
            background: #bdc3c7;
            cursor: not-allowed;
        }
        .leaderboard {
            text-align: left;
            padding: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        #feedback {
            font-weight: bold;
            margin-top: 14px;
            font-size: 1.6em;
            color: #2c3e50;
            font-family: 'Montserrat', sans-serif;
        }
    </style>
</head>
<body>
    <div id="startScreen" class="container">
        <h2>Welcome to Trivia Challenge!</h2>
        <label for="username">Enter Your Name:</label>
        <input type="text" id="username" placeholder="Your Name">
        <br><br>
        <label for="difficulty">Choose Difficulty:</label>
        <select id="difficulty">
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
        </select>
        <br><br>
        <button onclick="startGame()">Start Game</button>
    </div>
    <div id="gameScreen" class="container hidden">
        <h2 id="questionText"></h2>
        <button class="answer-button" onclick="submitAnswer('A')" id="optionA"></button>
        <button class="answer-button" onclick="submitAnswer('B')" id="optionB"></button>
        <button class="answer-button" onclick="submitAnswer('C')" id="optionC"></button>
        <button class="answer-button" onclick="submitAnswer('D')" id="optionD"></button>
        <p id="feedback"></p>
        <p>Score: <span id="score">0</span></p>
        <button onclick="nextQuestion()">Next Question</button>
    </div>
    <div id="resultScreen" class="container hidden">
        <h2>Game Over!</h2>
        <p>Your Final Score: <span id="finalScore"></span></p>
        <h3>Leaderboard</h3>
        <ol id="leaderboard" class="leaderboard"></ol>
        <button onclick="restartGame()">Play Again</button>
    </div>

