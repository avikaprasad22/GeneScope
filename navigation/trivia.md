---
layout: page 
title: DNA Trivia
permalink: /trivia/
---
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trivia Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 600px;
            width: 100%;
            text-align: center;
        }

        .question {
            font-size: 1.2em;
            margin-bottom: 20px;
        }

        .options button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 10px;
            font-size: 1em;
            border: 1px solid #ccc;
            border-radius: 5px;
            cursor: pointer;
            background-color: #f1f1f1;
        }

        .options button:hover {
            background-color: #ddd;
        }

        .score {
            font-size: 1.5em;
            margin-top: 20px;
        }

        .result {
            font-size: 1.2em;
            margin-top: 10px;
            color: green;
        }

        .btn {
            padding: 10px 20px;
            font-size: 1em;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
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
        let username = "John Doe";  // Replace with actual username or prompt for input

        // Fetch a random trivia question
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

        // Display the current question and options
        function displayQuestion() {
            document.getElementById("question").textContent = currentQuestion.question;
            document.getElementById("optionA").textContent = `A: ${currentQuestion.options.A}`;
            document.getElementById("optionB").textContent = `B: ${currentQuestion.options.B}`;
            document.getElementById("optionC").textContent = `C: ${currentQuestion.options.C}`;
            document.getElementById("optionD").textContent = `D: ${currentQuestion.options.D}`;
        }

        // Submit the selected answer
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

        // Move to the next question
        function nextQuestion() {
            fetchQuestion();
            document.getElementById("result").textContent = "";
        }

        // Start the game by fetching the first question
        fetchQuestion();
    </script>
</body>

</html>
