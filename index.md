---
layout: tailwind
title: Welcome to GeneScope
search_exclude: false
hide: true
show_reading_time: false
menu: nav/home.html
---

<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Welcome to GeneScope</title>
  <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">

  <style>
    /* Scrollbar Styling */
    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: #f1f1f1; }
    ::-webkit-scrollbar-thumb { background: #2563EB; border-radius: 5px; }
    ::-webkit-scrollbar-thumb:hover { background: #1E40AF; }

    /* Chatbot Styles */
    #help-button {
      position: fixed; bottom: 100px; right: 20px;
      padding: 10px 20px; background-color: #B22222;
      color: white; border: none; border-radius: 5px;
      cursor: pointer; font-size: 16px;
      box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
      z-index: 1000;
    }
    #help-button:hover { background-color: #63b6e3; }
    #chat-container {
      position: fixed; bottom: 100px; right: 20px;
      width: 350px; max-height: 500px;
      background-color: white; border: 1px solid #ddd;
      border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
      display: none; flex-direction: column; overflow: hidden;
      z-index: 1000;
    }
    #chat-header {
      display: flex; justify-content: space-between; align-items: center;
      padding: 10px; background-color: #333; color: white; border-bottom: 1px solid #ddd;
    }
    #chat-header h4 { margin: 0; font-size: 16px; }
    #close-chat { background: none; border: none; color: white; font-size: 18px; cursor: pointer; }
    #close-chat:hover { color: #ff6666; }
    #chat-box {
      flex-grow: 1; padding: 10px; overflow-y: auto;
      display: flex; flex-direction: column;
    }
    .message {
      margin: 10px; padding: 10px; border-radius: 10px;
      max-width: 75%; word-wrap: break-word; display: inline-block;
    }
    .assistant { background-color: #333; color: white; align-self: flex-start; text-align: left; }
    .user { background-color: #2f4f4f; color: white; align-self: flex-end; text-align: right; }
    #input-container {
      display: flex; padding: 10px; border-top: 1px solid #ddd;
    }
    input[type="text"] {
      flex-grow: 1; padding: 10px; border: 1px solid #ddd;
      border-radius: 5px; font-size: 14px; color: black !important;
    }
    button {
      margin-left: 5px; padding: 10px; background-color: #333;
      color: white; border: none; border-radius: 5px;
      cursor: pointer; font-size: 14px;
    }
    button:hover { background-color: #555; }
  </style>
</head>

<body>

<!-- Hero Section -->
<section id="welcome" class="h-screen flex flex-col items-center justify-center text-center bg-cover bg-center relative" style="background-image: url('https://scitechdaily.com/images/DNA-Genetics.gif');">
  <div class="absolute inset-0 bg-black opacity-50 pointer-events-none"></div>
  <div class="relative z-10">
    <h1 class="text-6xl font-bold text-white neon-glow">
      <span id="typewriter"></span>
    </h1>
    <h2 class="text-2xl mt-4 text-white opacity-80">Igniting Curiosity, Advancing Science</h2>
  </div>
</section>

<!-- About Us Section -->
<section id="about" class="py-20 text-center bg-gray-900">
  <h2 class="text-5xl font-bold text-white fade-in">About Us</h2>
  <p class="text-xl text-gray-300 mt-4 max-w-4xl mx-auto fade-in">
    The GeneScope Biotech Education Game is an innovative initiative designed to engage students and the community in the fascinating world of biotechnology. Through interactive gameplay and real-world challenges, participants explore DNA, genetics, and cutting-edge scientific advancements in a fun and immersive way.
  </p>
</section>

<!-- Our Mission Section -->
<section id="mission" class="py-20 text-center bg-black">
  <h3 class="text-5xl font-bold text-white fade-in">Our Mission</h3>
  <p class="text-xl text-gray-300 mt-4 max-w-4xl mx-auto fade-in">
    Our mission aims to spark curiosity, inspire future scientists, and make biotech education accessible to all.
  </p>
</section>

<!-- Interactive Activities Section -->
<section id="ai-solutions" class="py-20 bg-gray-900">
  <h2 class="text-5xl font-bold text-center text-white mb-10 fade-in">Interactive Activities</h2>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mx-auto max-w-6xl">
    <a href="{{ site.baseurl }}/risk-quiz/">
      <div class="bg-white p-6 rounded-lg shadow-lg hover:scale-105 ai-card">
        <h3 class="text-3xl font-bold mb-2 text-black">Risk Quiz Analysis</h3>
        <p class="text-xl text-gray-700">Explore DNA sequencing processes.</p>
      </div>
    </a>
    <a href="{{ site.baseurl }}/trivia">
      <div class="bg-white p-6 rounded-lg shadow-lg hover:scale-105 ai-card">
        <h3 class="text-3xl font-bold mb-2 text-black">Trivia Challenge</h3>
        <p class="text-xl text-gray-700">Test your knowledge on genetic research breakthroughs.</p>
      </div>
    </a>
    <a href="{{ site.baseurl }}/genes">
      <div class="bg-white p-6 rounded-lg shadow-lg hover:scale-105 ai-card">
        <h3 class="text-3xl font-bold mb-2 text-black">Gene Mutation Guessing Game</h3>
        <p class="text-xl text-gray-700">Learn about the effects of different gene mutations on the body.</p>
      </div>
    </a>
  </div>
</section>

<!-- Chatbot -->
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

<!-- Typewriter Script -->
<script>
document.addEventListener("DOMContentLoaded", function () {
  const text = "Welcome to GeneScope";
  let index = 0;
  const speed = 100;
  const typewriter = document.getElementById("typewriter");

  function type() {
    if (index < text.length) {
      typewriter.textContent += text.charAt(index);
      index++;
      setTimeout(type, speed);
    }
  }

  type();
});
</script>

<!-- Chatbot Script -->
<script>
const BACKEND_URL = "http://127.0.0.1:8504";
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const chatContainer = document.getElementById('chat-container');
const sendMessageButton = document.getElementById('send-message-button');

document.getElementById('help-button').addEventListener('click', toggleChat);
document.getElementById('close-chat').addEventListener('click', toggleChat);
sendMessageButton.addEventListener('click', sendMessage);

userInput.addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    sendMessage();
  }
});

function toggleChat() {
  chatContainer.style.display = chatContainer.style.display === 'flex' ? 'none' : 'flex';
  if (chatContainer.style.display === 'flex') {
    chatContainer.style.flexDirection = 'column';
  }
}

async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;
  appendMessage('user', message);
  userInput.value = '';

  try {
    const response = await fetch(`${BACKEND_URL}/dnabot/chat`, {
      method: 'POST',
      mode: 'cors',
      credentials: 'include',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_input: message })
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

</body>
</html>