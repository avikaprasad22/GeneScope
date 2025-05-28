---
layout: tailwind
title: Welcome to GeneScope
search_exclude: false
hide: true
show_reading_time: false
menu: nav/home.html
---

<head>

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
    
    #output {
    margin-top: 20px;
    font-size: 20px;
    color: #333;
  }
  
  .pyramid-loader {
    position: relative;
    width: 150px;
    height: 150px;
    transform-style: preserve-3d;
    transform: rotateX(-20deg);
    margin: 20px auto;
    cursor: pointer;
  }
  
  .wrapper {
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
  }
  
  .wrapper.spinning {
    animation: spin 4s linear infinite;
  }
  
  @keyframes spin {
    100% {
      transform: rotateY(360deg);
    }
  }
  
  .pyramid-loader .wrapper .side {
    width: 70px;
    height: 70px;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    transform-origin: center top;
    clip-path: polygon(50% 0%, 0% 100%, 100% 100%);
  }
  
  .pyramid-loader .wrapper .side1 {
    transform: rotateZ(-30deg) rotateY(90deg);
    background: conic-gradient(#e0115f, #ff6f61, #e0115f);
  }
  
  .pyramid-loader .wrapper .side2 {
    transform: rotateZ(30deg) rotateY(90deg);
    background: conic-gradient(#ff6f61, #e0115f, #ff6f61);
  }
  
  .pyramid-loader .wrapper .side3 {
    transform: rotateX(30deg);
    background: conic-gradient(#e0115f, #ff6f61, #e0115f);
  }
  
  .pyramid-loader .wrapper .side4 {
    transform: rotateX(-30deg);
    background: conic-gradient(#ff6f61, #e0115f, #ff6f61);
  }
  
  .pyramid-loader .wrapper .shadow {
    width: 60px;
    height: 60px;
    background: #ff6f61;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    margin: auto;
    transform: rotateX(90deg) translateZ(-40px);
    filter: blur(12px);
  }
  #pyricmind-container {
  position: fixed;
  bottom: 100px;
  left: 20px;
  z-index: 1000;
  text-align: center;
  width: 150px; /* Optional: control width */
  }

  #pyricmind-container #output {
    font-size: 14px;
    color: white;
    margin-top: 10px;
  }
  /* Fullscreen Loading Screen */
  #hamster-loading-screen {
    position: fixed;
    top: -40;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: black;
    z-index: 9999;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    opacity: 1;
    transition: opacity 1s ease-out; /* Smooth fade out */
  }

  #hamster-loading-screen.hide {
    opacity: 0;
    visibility: hidden; /* Hides it completely after fade out */
  }

  @keyframes stay-visible {
    0% { opacity: 1; }
    100% { opacity: 1; }
  }

  .wheel-and-hamster {
      --dur: 1s;
      font-size: 14px;
      width: 12em;
      height: 12em;
      position: relative;
    }
    .wheel,
    .hamster,
    .hamster div,
    .spoke {
      position: absolute;
    }
    .wheel,
    .spoke {
      border-radius: 50%;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
    }
    .wheel {
      background: radial-gradient(100% 100% at center, hsla(0,0%,60%,0) 47.8%, hsl(0,0%,60%) 48%);
      z-index: 2;
    }
    .hamster {
      animation: hamster var(--dur) ease-in-out infinite;
      top: 50%;
      left: calc(50% - 3.5em);
      width: 7em;
      height: 3.75em;
      transform: rotate(4deg) translate(-0.8em,1.85em);
      transform-origin: 50% 0;
      z-index: 1;
    }
    .hamster__head {
      animation: hamsterHead var(--dur) ease-in-out infinite;
      background: hsl(30,90%,55%);
      border-radius: 70% 30% 0 100% / 40% 25% 25% 60%;
      box-shadow: 0 -0.25em 0 hsl(30,90%,80%) inset, 0.75em -1.55em 0 hsl(30,90%,90%) inset;
      top: 0;
      left: -2em;
      width: 2.75em;
      height: 2.5em;
      transform-origin: 100% 50%;
    }
    .hamster__ear {
      animation: hamsterEar var(--dur) ease-in-out infinite;
      background: hsl(0,90%,85%);
      border-radius: 50%;
      box-shadow: -0.25em 0 hsl(30,90%,55%) inset;
      top: -0.25em;
      right: -0.25em;
      width: 0.75em;
      height: 0.75em;
      transform-origin: 50% 75%;
    }
    .hamster__eye {
      animation: hamsterEye var(--dur) linear infinite;
      background-color: hsl(0,0%,0%);
      border-radius: 50%;
      top: 0.375em;
      left: 1.25em;
      width: 0.5em;
      height: 0.5em;
    }
    .hamster__nose {
      background: hsl(0,90%,75%);
      border-radius: 35% 65% 85% 15% / 70% 50% 50% 30%;
      top: 0.75em;
      left: 0;
      width: 0.2em;
      height: 0.25em;
    }
    .hamster__body {
      animation: hamsterBody var(--dur) ease-in-out infinite;
      background: hsl(30,90%,90%);
      border-radius: 50% 30% 50% 30% / 15% 60% 40% 40%;
      box-shadow: 0.1em 0.75em 0 hsl(30,90%,55%) inset, 0.15em -0.5em 0 hsl(30,90%,80%) inset;
      top: 0.25em;
      left: 2em;
      width: 4.5em;
      height: 3em;
      transform-origin: 17% 50%;
      transform-style: preserve-3d;
    }
    .hamster__limb--fr,
    .hamster__limb--fl {
      clip-path: polygon(0 0,100% 0,70% 80%,60% 100%,0% 100%,40% 80%);
      top: 2em;
      left: 0.5em;
      width: 1em;
      height: 1.5em;
      transform-origin: 50% 0;
    }
    .hamster__limb--fr {
      animation: hamsterFRLimb var(--dur) linear infinite;
      background: linear-gradient(hsl(30,90%,80%) 80%, hsl(0,90%,75%) 80%);
      transform: rotate(15deg) translateZ(-1px);
    }
    .hamster__limb--fl {
      animation: hamsterFLLimb var(--dur) linear infinite;
      background: linear-gradient(hsl(30,90%,90%) 80%, hsl(0,90%,85%) 80%);
      transform: rotate(15deg);
    }
    .hamster__limb--br,
    .hamster__limb--bl {
      border-radius: 0.75em 0.75em 0 0;
      clip-path: polygon(0 0,100% 0,100% 30%,70% 90%,70% 100%,30% 100%,40% 90%,0% 30%);
      top: 1em;
      left: 2.8em;
      width: 1.5em;
      height: 2.5em;
      transform-origin: 50% 30%;
    }
    .hamster__limb--br {
      animation: hamsterBRLimb var(--dur) linear infinite;
      background: linear-gradient(hsl(30,90%,80%) 90%, hsl(0,90%,75%) 90%); /*(hsl(198, 90.20%, 80.00%) 90%, hsl(242, 90.60%, 75.10%) 90%); */
      transform: rotate(-25deg) translateZ(-1px);
    }
    .hamster__limb--bl {
      animation: hamsterBLLimb var(--dur) linear infinite;
      background: linear-gradient(hsl(30,90%,90%) 90%, hsl(0,90%,85%) 90%);
      transform: rotate(-25deg);
    }
    .hamster__tail {
      animation: hamsterTail var(--dur) linear infinite;
      background: hsl(0,90%,85%);
      border-radius: 0.25em 50% 50% 0.25em;
      box-shadow: 0 -0.2em 0 hsl(0,90%,75%) inset;
      top: 1.5em;
      right: -0.5em;
      width: 1em;
      height: 0.5em;
      transform: rotate(30deg) translateZ(-1px);
      transform-origin: 0.25em 0.25em;
    }
    .spoke {
      animation: spoke var(--dur) linear infinite;
      background: radial-gradient(100% 100% at center,hsl(0,0%,60%) 4.8%,hsla(0,0%,60%,0) 5%), linear-gradient(hsla(0,0%,55%,0) 46.9%,hsl(0,0%,65%) 47% 52.9%,hsla(0,0%,65%,0) 53%) 50% 50% / 99% 99% no-repeat;
    }
    @keyframes hamster {
      0%, 100% { transform: rotate(4deg) translate(-0.8em,1.85em); }
      50% { transform: rotate(0) translate(-0.8em,1.85em); }
    }
    @keyframes hamsterHead {
      0%, 25%, 50%, 75%, 100% { transform: rotate(0); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(8deg); }
    }
    @keyframes hamsterEye {
      0%, 90%, 100% { transform: scaleY(1); }
      95% { transform: scaleY(0); }
    }
    @keyframes hamsterEar {
      0%, 25%, 50%, 75%, 100% { transform: rotate(0); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(12deg); }
    }
    @keyframes hamsterBody {
      0%, 25%, 50%, 75%, 100% { transform: rotate(0); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(-2deg); }
    }
    @keyframes hamsterFRLimb {
      0%, 25%, 50%, 75%, 100% { transform: rotate(50deg) translateZ(-1px); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(-30deg) translateZ(-1px); }
    }
    @keyframes hamsterFLLimb {
      0%, 25%, 50%, 75%, 100% { transform: rotate(-30deg); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(50deg); }
    }
    @keyframes hamsterBRLimb {
      0%, 25%, 50%, 75%, 100% { transform: rotate(-60deg) translateZ(-1px); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(20deg) translateZ(-1px); }
    }
    @keyframes hamsterBLLimb {
      0%, 25%, 50%, 75%, 100% { transform: rotate(20deg); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(-60deg); }
    }
    @keyframes hamsterTail {
      0%, 25%, 50%, 75%, 100% { transform: rotate(30deg) translateZ(-1px); }
      12.5%, 37.5%, 62.5%, 87.5% { transform: rotate(10deg) translateZ(-1px); }
    }
    @keyframes spoke {
      from { transform: rotate(0); }
      to { transform: rotate(-1turn); }
    }
    .card {
  position: relative;
  width: 300px;
  height: 254px;
  color: #fff;
  transition: 0.5s;
  cursor: pointer;
}
.card:hover {
  transform: translateY(-20px);
}
.card::before {
  content: '';
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background: linear-gradient(45deg,rgb(0, 255, 255),rgb(44, 32, 206));
  border-radius: 1.2em;
}
.card::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(45deg,rgb(0, 238, 255),rgb(17, 0, 255));
  filter: blur(30px);
}
.card span {
  position: absolute;
  top: 6px;
  left: 6px;
  right: 6px;
  bottom: 6px;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 2;
  border-radius: 1em;
}
.card span::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 50%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.1);
}
.card .content {
  position: relative;
  padding: 10px;
  z-index: 10;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 800;
  font-size: 1.5em;
}


  </style>
</head>

<body>
<div id="hamster-loading-screen">
<div aria-label="Orange and tan hamster running in a metal wheel" role="img" class="wheel-and-hamster">
    <div class="wheel"></div>
    <div class="hamster">
      <div class="hamster__body">
        <div class="hamster__head">
          <div class="hamster__ear"></div>
          <div class="hamster__eye"></div>
          <div class="hamster__nose"></div>
        </div>
        <div class="hamster__limb hamster__limb--fr"></div>
        <div class="hamster__limb hamster__limb--fl"></div>
        <div class="hamster__limb hamster__limb--br"></div>
        <div class="hamster__limb hamster__limb--bl"></div>
        <div class="hamster__tail"></div>
      </div>
    </div>
    <div class="spoke"></div>
  </div>
</div>

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

<!-- Interactive Activities Section -->
<section id="ai-solutions" class="py-20 bg-gray-900">
  <h2 class="text-5xl font-bold text-center text-white mb-10 fade-in">Interactive Activities</h2>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mx-auto max-w-6xl place-items-center">
    <a href="{{ site.baseurl }}/risk-quiz/" class="block">
      <div class="card">
        <span></span>
        <div class="content flex flex-col items-center justify-center text-center">
          <div class="text-2xl">Risk Quiz</div>
          <p class="text-sm font-normal mt-2 px-4">Explore DNA sequencing processes.</p>
        </div>
      </div>
    </a>
    <a href="{{ site.baseurl }}/trivia" class="block">
      <div class="card">
        <span></span>
        <div class="content flex flex-col items-center justify-center text-center">
          <div class="text-2xl">Trivia Challenge</div>
          <p class="text-sm font-normal mt-2 px-4">Test your knowledge on genetic research breakthroughs.</p>
        </div>
      </div>
    </a>
    <a href="{{ site.baseurl }}/genes" class="block">
      <div class="card">
        <span></span>
        <div class="content flex flex-col items-center justify-center text-center">
          <div class="text-2xl">Gene Explorer</div>
          <p class="text-sm font-normal mt-2 px-4">Learn about the effects of different gene mutations on the body.</p>
        </div>
      </div>
    </a>
  </div>
</section>



<!-- Chatbot -->
<button id="help-button">Need Help?</button>

<div id="chat-container">
  <div id="chat-header">
    <h4>Annie</h4>
    <button id="close-chat">×</button>
  </div>
  <div id="chat-box"></div>
  <div id="input-container">
    <input type="text" id="user-input" placeholder="Type your message..." />
    <button id="send-message-button">Send</button>
  </div>
</div>

<!-- ANNIE--->

<div id="pyricmind-container">
  <div id="loader" class="pyramid-loader">
    <div class="wrapper" id="pyramidWrapper">
      <span class="side side1"></span>
      <span class="side side2"></span>
      <span class="side side3"></span>
      <span class="side side4"></span>
      <span class="shadow"></span>
    </div>
  </div>
  <p>Click the pyramid to speak with ANNIE</p>
  <button id="stopSpeakingBtn">🛑 Stop Speaking</button>

</div>


<!-- HAMASTER LOADING CODE -->
<script>
    window.addEventListener('load', function() {
    const loadingScreen = document.getElementById('hamster-loading-screen');
    if (loadingScreen) {
      loadingScreen.style.transition = 'opacity 3.0s ease';
      loadingScreen.style.opacity = '0';
      setTimeout(() => loadingScreen.style.display = 'none', 500);
    }
  });

  window.onload = function () {
  // Trigger fade out after 3 seconds or when loading is done
  setTimeout(function() {
    document.getElementById('hamster-loading-screen').classList.add('hide');
  }, 1000); // Customize delay as per your need
  };

  function updateTime() {
  const outputElement = document.getElementById("output");
  const date = new Date();
  const formattedTime = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`;
  outputElement.innerHTML = formattedTime;
}

// Update the time every second
setInterval(updateTime, 1000);
</script>

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

<!-- DNABOT Script -->
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

async function sendMessage(inputMessage) {
  // If inputMessage is undefined (i.e., user typed something), get it from the input box
  const message = inputMessage !== undefined ? inputMessage.trim() : userInput.value.trim();
  if (!message) return;

  appendMessage('user', message);

  if (!inputMessage) {
    userInput.value = ""; // Clear the input box only if typed manually
  }

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
      console.log('DNA Bot response:', data.response);
      console.log("⏯️ About to speak:", data.response)
      speakText(data.response); // 🔊 Annie speaks here
    } else {
      console.error('Error from backend:', data.error);
      appendMessage('assistant', `Error: ${data.error}`);
    }
  } catch (error) {
    console.error('Network or server error:', error.message);
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

<!-- ANNIES CODE -->
<script>

let currentUtterance = null
function speakText(text) {
  if (speechSynthesis.speaking){
    speechSynthesis.cancel();
  }


  const utterance = new SpeechSynthesisUtterance(text);
  currentUtterance = utterance
  utterance.lang = 'en-US';
  utterance.pitch = 1;
  utterance.rate = 1;

  // Wait for voices to be loaded
  const voices = speechSynthesis.getVoices();
  const femaleVoice = voices.find(voice =>
    voice.lang === 'en-US' && voice.name.toLowerCase().includes("female")
  ) || voices.find(voice =>
    voice.lang === 'en-US' && (voice.name.includes("Google") || voice.name.includes("Samantha") || voice.name.includes("Jenny"))
  );

  if (femaleVoice) {
    utterance.voice = femaleVoice;
  }

  speechSynthesis.speak(utterance);
}

// Ensure voices are loaded
if (speechSynthesis.onvoiceschanged !== undefined) {
  speechSynthesis.onvoiceschanged = () => {
    setTimeout(() => {
      speechSynthesis.getVoices(); // Ensure loading
    }, 100);
  };
}


  let recognition;
  let isListening = false;
  let heardText = "";  // This will save what ANNIE hears

  if ('webkitSpeechRecognition' in window) {
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    recognition.onresult = function(event) {
      for (let i = event.resultIndex; i < event.results.length; ++i) {
        if (event.results[i].isFinal) {
          heardText = event.results[i][0].transcript.trim();
          console.log("ANNIE heard:", heardText);  // Print to console
          // Optional: also display it on the page
          sendMessage(heardText);
          document.getElementById("output").textContent = "Heard: " + heardText;
        }
      }
    };

    recognition.onerror = function(event) {
      console.error("Recognition error:", event.error);
    };
  } else {
    console.error("Speech recognition not supported in this browser.");
  }

document.getElementById("stopSpeakingBtn").addEventListener("click", function() {
  if (speechSynthesis.speaking) {
    speechSynthesis.cancel();
    console.log("ANNIE's current speech stopped.");
  }
});

  
  // Click the pyramid to start/stop listening
  const pyramidWrapper = document.getElementById("pyramidWrapper");
  pyramidWrapper.addEventListener("click", function() {
    if (!isListening) {
      recognition.start();
      pyramidWrapper.classList.add("spinning");
      console.log("ANNIE started listening...");
    } else {
      recognition.stop();
      pyramidWrapper.classList.remove("spinning");
      console.log("ANNIE stopped listening.");
    }
    isListening = !isListening;
  });
</script>

</body>