---
layout: post
title: Business
search_exclude: true
hide: true
menu: nav/home.html
show_reading_time: false
---
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Business Efficiency</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Loading Screen */
        .loader {
            border-top-color: #1E3A8A;
            animation: spin 1s infinite linear;
        }
        @keyframes spin {
            0% {
                transform: rotate(0deg);
            }
            100% {
                transform: rotate(360deg);
            }
        }
        /* Fade-in animation */
        .fade-in {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 1s ease-out, transform 1s ease-out;
        }
        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }
        /* Gradient Animation */
        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        .animate-gradient {
            background-size: 200% 200%;
            animation: gradient 10s ease infinite;
        }
        /* Typewriter effect */
        .typewriter {
            font-size: 6rem;
            font-weight: 900;
            overflow: hidden;
            white-space: nowrap;
            margin: 0 auto;
            word-spacing: 1em;
            line-height: 1.2;
        }
        .typewriter .text {
            display: inline-block;
            opacity: 0;
        }
        .second-line {
            display: block;
        }
    </style>
</head>

<body class="bg-black text-white relative">
    <!-- Loading Screen -->
    <div id="loading-screen" class="fixed inset-0 bg-blue-200 flex items-center justify-center z-50">
        <div class="text-center">
            <div class="loader ease-linear rounded-full border-8 border-t-8 border-blue-500 h-32 w-32 mb-4"></div>
            <h2 class="text-4xl font-semibold text-blue-900">Loading...</h2>
        </div>
    </div>
    <!-- Background Animation -->
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden -z-10">
        <div class="bg-gradient-to-r from-blue-400 via-yellow-400 to-blue-500 w-full h-full opacity-50 animate-gradient"></div>
    </div>
    <!-- Welcome Section with Typewriter Effect -->
    <section id="welcome" class="h-screen flex items-center justify-center text-center bg-black text-blue-200">
        <h1 class="typewriter"></h1>
    </section>
    <!-- About Us Section -->
    <section id="about" class="h-screen flex flex-col items-center justify-center text-center bg-blue-100 text-black">
        <h2 class="text-7xl font-extrabold text-blue-600 fade-in mb-6">About Us</h2>
        <p class="text-3xl text-green-900 max-w-5xl fade-in">
            AI Business Efficiency is a leading platform dedicated to optimizing workflows and enhancing decision-making through AI-driven insights. We empower businesses with automation, analytics, and innovative AI solutions.
        </p>
    </section>
    <!-- Our Mission Section -->
    <section id="mission" class="h-screen flex flex-col items-center justify-center text-center bg-green-100 text-black">
        <h3 class="text-6xl font-bold mt-8 text-green-900 fade-in">Our Mission</h3>
        <p class="text-3xl text-green-700 mt-4 max-w-5xl fade-in">
            Our mission is to drive business success through AI, streamlining processes, boosting productivity, and enabling data-driven decision-making. We bring AI-powered solutions to businesses of all sizes.
        </p>
    </section>
    <!-- AI Solutions Section -->
    <section id="ai-solutions" class="py-20 bg-yellow-100">
        <h2 class="text-7xl font-bold text-center text-yellow-900 mb-10 fade-in">Our AI Solutions</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-blue-900">Automation</h3>
                    <p class="text-xl text-yellow-800">Optimize workflows and reduce manual tasks with AI-driven automation tools.</p>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-blue-900">Predictive Analytics</h3>
                    <p class="text-xl text-yellow-800">Leverage AI-powered insights to anticipate trends and make informed decisions.</p>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-blue-900">AI Consultation</h3>
                    <p class="text-xl text-yellow-800">Get expert guidance on integrating AI into your business for maximum efficiency.</p>
                </div>
            </div>
        </div>
    </section>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const loadingScreen = document.getElementById('loading-screen');
            window.addEventListener('load', function() {
                loadingScreen.style.display = 'none';
            });
            // Typewriter effect for the welcome message
            const text = "Welcome to\nAI Business\nEfficiency";
            const typewriterElement = document.querySelector(".typewriter");
            let index = 0;
            function type() {
                if (index < text.length) {
                    const span = document.createElement('span');
                    span.textContent = text.charAt(index);
                    span.classList.add('text');
                    typewriterElement.appendChild(span);
                    setTimeout(() => {
                        span.style.opacity = 1;
                    }, 50 * index);
                    index++;
                    setTimeout(type, 80);
                }
            }
            type();
            // Fade in effect
            const fadeInElements = document.querySelectorAll('.fade-in');
            window.addEventListener('scroll', function() {
                fadeInElements.forEach(function(element) {
                    if (element.getBoundingClientRect().top < window.innerHeight) {
                        element.classList.add('visible');
                    }
                });
            });
        });
    </script>
</body>

<style>
    #help-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    padding: 10px 20px;
    background-color: #B22222 !important;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

#help-button:hover {
    background-color: #63b6e3;
}

#chat-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 350px;
    max-height: 500px;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    display: none;
    flex-direction: column;
    overflow: hidden;
}

#chat-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background-color: #333;
    color: white;
    border-bottom: 1px solid #ddd;
}

#chat-header h4 {
    margin: 0;
    font-size: 16px;
}

#close-chat {
    background: none;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
}

#close-chat:hover {
    color: #ff6666;
}

#chat-box {
    flex-grow: 1;
    padding: 10px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
}

.message {
    margin: 10px;
    padding: 10px;
    border-radius: 10px;
    max-width: 75%;
    word-wrap: break-word;
    display: inline-block;
}

.assistant {
    background-color: #333;
    color: white;
    align-self: flex-start;
    text-align: left;
}

.user {
    background-color: #2f4f4f;
    color: white;
    align-self: flex-end;
    text-align: right;
}

#input-container {
    display: flex;
    padding: 10px;
    border-top: 1px solid #ddd;
}

input[type="text"] {
    flex-grow: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 14px;
}

button {
    margin-left: 5px;
    padding: 10px;
    background-color: #333;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
}

button:hover {
    background-color: #555;
}
</style>
<html>
    <button id="help-button">Need Help?</button>
        <div id="chat-container">
            <div id="chat-header">
                <h4>Giftinator 3000</h4>
                <button id="close-chat">×</button>
            </div>
            <div id="chat-box"></div>
            <div id="input-container">
                <input type="text" id="user-input" placeholder="Type your message..." />
                <button id="send-message-button">Send</button>
            </div>
        </div>
</html>
<script>
    const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const chatContainer = document.getElementById('chat-container');
const sendMessageButton = document.getElementById('send-message-button');
// Adding event listeners for the help button, close chat button, and send message button
document.getElementById('help-button').addEventListener('click', toggleChat);
document.getElementById('close-chat').addEventListener('click', toggleChat);
sendMessageButton.addEventListener('click', sendMessage); // Event listener for send message button
function toggleChat() {
    chatContainer.style.display = chatContainer.style.display === 'flex' ? 'none' : 'flex';
}
async function sendMessage() {
    const message = userInput.value;
    if (!message) return;
    appendMessage('user', message);
    userInput.value = '';
    try {
        const response = await fetch(`${pythonURI}/chat`, {
            ...fetchOptions,
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_input: message }),
            credentials: 'include' // Ensures cookies/auth headers work
        });
        const data = await response.json();
        if (response.ok) {
            appendMessage('assistant', data.response);
        } else {
            appendMessage('assistant', `Error: ${data.error}`);
        }
    } catch (error) {
        appendMessage('assistant', `Error: ${error.message}`);
    }
}
function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.className = `message ${sender}`;
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}

</script>