---
layout: page 
title: DNA Trivia
permalink: /trivia/
---

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trivia Game</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
            max-width: 700px;
            width: 100%;
            text-align: center;
        }
        .question {
            font-size: 1.5em;
            font-weight: 600;
            margin-bottom: 25px;
        }
        .options button {
            display: block;
            width: 90%;
            margin: 15px auto;
            padding: 15px;
            font-size: 1.2em;
            border: 2px solid #ccc;
            border-radius: 8px;
            cursor: pointer;
            background-color: #f1f1f1;
            transition: all 0.3s ease;
        }
        .options button:hover {
            background-color: #ddd;
            transform: scale(1.05);
        }
        .score {
            font-size: 1.8em;
            font-weight: 600;
            margin-top: 20px;
            color: #333;
        }
        .result {
            font-size: 1.4em;
            margin-top: 15px;
            font-weight: bold;
            color: green;
        }
        .btn {
            padding: 12px 25px;
            font-size: 1.2em;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            margin-top: 15px;
            transition: background 0.3s ease;
        }
        .btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Trivia Challenge</h1>
        <div class="question-container">
            <div class="question" id="question"></div>
            <div class="options">
                <button id="optionA" onclick="submitAnswer('A')">A</button>
                <button id="optionB" onclick="submitAnswer('B')">B</button>
                <button id="optionC" onclick="submitAnswer('C')">C</button>
                <button id="optionD" onclick="submitAnswer('D')">D</button>
            </div>
        </div>
        <div class="score" id="score"></div>
        <div class="result" id="result"></div>
        <button class="btn" onclick="nextQuestion()">Next Question</button>
    </div>
    <script>
        let currentQuestion = null;
        let userScore = 0;
        let username = "John Doe";
        function fetchQuestion() {
            fetch("http://localhost:5000/api/trivia/question")
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        document.getElementById("question").textContent = "No questions available.";
                    } else {
                        currentQuestion = data;
                        displayQuestion();
                    }
                })
                .catch(error => {
                    console.error("Error fetching question:", error);
                    document.getElementById("question").textContent = "Error fetching question.";
                });
        }
        function displayQuestion() {
            document.getElementById("question").textContent = currentQuestion.question;
            document.getElementById("optionA").textContent = `A: ${currentQuestion.options.A}`;
            document.getElementById("optionB").textContent = `B: ${currentQuestion.options.B}`;
            document.getElementById("optionC").textContent = `C: ${currentQuestion.options.C}`;
            document.getElementById("optionD").textContent = `D: ${currentQuestion.options.D}`;
        }
        function submitAnswer(selectedOption) {
            const selectedAnswer = currentQuestion.options[selectedOption];
            const questionId = currentQuestion.id;
            const payload = {
                name: username,
                question_id: questionId,
                selected_answer: selectedAnswer
            };
            fetch("http://localhost:5000/api/trivia/answer", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            })
                .then(response => response.json())
                .then(data => {
                    if (data.correct) {
                        userScore += 10;
                        document.getElementById("result").textContent = "Correct!";
                    } else {
                        document.getElementById("result").textContent = "Incorrect. The correct answer was: " + currentQuestion.correct_answer;
                    }
                    document.getElementById("score").textContent = "Score: " + userScore;
                })
                .catch(error => {
                    console.error("Error submitting answer:", error);
                });
        }
        function nextQuestion() {
            fetchQuestion();
            document.getElementById("result").textContent = "";
        }
        fetchQuestion();
    </script>
</body>

