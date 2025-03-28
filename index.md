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
    <title>Illumina Interactive Biotech Education</title>
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
            word-spacing: 0.2em; /* Adjusted word-spacing */
            line-height: 1.2;
        }
        .typewriter .text {
            display: inline-block;
            opacity: 0;
        }
        .second-line {
            display: block;
        }
        /* Slogan Styling */
        .slogan {
            font-size: 2rem;
            margin-top: 1rem;
            opacity: 0;
            transition: opacity 1s ease-out; /* Fade in transition */
        }
        /* Welcome Section BG IMG */
        #welcome {
            position: relative; /* Ensure positioning for the overlay */
            background: url(https://scitechdaily.com/images/DNA-Genetics.gif) no-repeat center center; 
            background-size: cover;
        }
        /* Overlay to dim the background */
        #welcome::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.5); /* Adjust opacity (0.5 = 50% dim) */
            z-index: 1; /* Ensures the overlay is on top */
        }
        /* Ensure text and content are above the overlay */
        #welcome > * {
            position: relative;
            z-index: 2;
        }
        /* Welcome Section BG IMG */
        #welcome {
            background: url(https://scitechdaily.com/images/DNA-Genetics.gif) no-repeat center center; 
            background-size: cover;
        }
        /* Neon Glow Animation */
        @keyframes neonGlow {
            0% {
                box-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
            }
            50% {
                box-shadow: 0 0 10px #00ff00, 0 0 20px #00ff00, 0 0 40px #00ff00, 0 0 80px #00ff00;
            }
            100% {
                box-shadow: 0 0 5px #ff00ff, 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 40px #ff00ff;
            }
        }
        .neon-glow {
            animation: neonGlow 2s ease-in-out infinite alternate;
            color: #fff;
        }
        /* AI Solutions Cards */
        .ai-card {
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .ai-card:hover {
            transform: scale(1.05);
            animation: neonGlow 1.5s ease-in-out infinite alternate;
            box-shadow: 0 0 10px #ff00ff, 0 0 20px #ff00ff, 0 0 30px #ff00ff;
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
    <!-- Welcome Section with Typewriter Effect -->
    <section id="welcome" class="h-screen flex flex-col items-center justify-center text-center bg-black text-white-200 ">
        <h1 class="typewriter"></h1>
        <h2 id="slogan" class="slogan text-4xl" style="color:rgb(255, 255, 255); text-shadow: 0 0 2px rgb(162, 188, 220), 0 0 2px rgb(77, 146, 207), 0 0 4px rgb(88, 77, 207), 0 0 4px rgb(77, 207, 168)">Illumina Biotech: Igniting Curiosity, Advancing Science</h2>
    </section>
    <!-- About Us Section -->
    <section id="about" class="h-screen flex flex-col items-center justify-center text-center bg-black text-white">
        <h2 class="text-7xl font-extrabold text-white-600 fade-in mb-6">About Us</h2>
        <p class="text-3xl text-white-900 max-w-5xl fade-in">
            The Illumina Biotech Education Game is an innovative initiative designed to engage students and the community in the fascinating world of biotechnology. Through interactive gameplay and real-world challenges, participants explore DNA, genetics, and cutting-edge scientific advancements in a fun and immersive way. 
        </p>
    </section>
    <!-- Our Mission Section -->
    <section id="mission" class="h-screen flex flex-col items-center justify-center text-center py-20 bg-gray-900 text-white">
        <h3 class="text-6xl font-bold mt-8 text-white-900 fade-in">Our Mission</h3>
        <p class="text-3xl text-white-700 mt-4 max-w-5xl fade-in">
            Our mission aims to spark curiosity, inspire future scientists, and make biotech education accessible to all.
        </p>
    </section>
    <!-- AI Solutions Section -->
    <section id="ai-solutions" class="py-20 bg-black">
        <h2 class="text-7xl font-bold text-center text-white mb-10 fade-in">Interactive Activities</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105 ai-card">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-black">Virtual Lab Simulation</h3>
                    <p class="text-xl text-black">Explore DNA sequencing processes.</p>
                </div>
            </div>
            <a href="{{site.baseurl}}/trivia" target="_self">
                <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105 ai-card">
                    <div class="p-6">
                        <h3 class="text-3xl font-bold mb-2 text-black">Trivia Challenge</h3>
                        <p class="text-xl text-black">Test your knowledge on genetic research breakthroughs.</p>
                    </div>
                </div>
            </a>
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105 ai-card">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-black">Puzzle Game</h3>
                    <p class="text-xl text-black">Illustrates the impact of personalized medicine.</p>
                </div>
            </div>
        </div>
    </section>
    <section id="choose-character" class="py-20 bg-gray-900 text-white text-center">
        <h2 class="text-6xl font-extrabold mb-10">Learn About the Technologies</h2>
        <div class="flex flex-wrap justify-center gap-8">
            <!-- Character Card 1 -->
            <div class="relative group bg-gray-800 rounded-2xl shadow-lg overflow-hidden transition-all duration-300 transform hover:scale-110 hover:shadow-2xl cursor-pointer w-60 h-80">
                <img src="https://media4.giphy.com/media/RB1gL2aMEsItG/giphy.gif?cid=6c09b952pmri47f54h2k16ft5y1m1qkrh96ru10d58isvwqf&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Scientist" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-300">
                <div class="absolute bottom-0 w-full bg-black bg-opacity-70 p-4 text-lg font-bold text-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    Trivia Game
                </div>
            </div>
            <!-- Character Card 2 -->
            <div class="relative group bg-gray-800 rounded-2xl shadow-lg overflow-hidden transition-all duration-300 transform hover:scale-110 hover:shadow-2xl cursor-pointer w-60 h-80">
                <img src="https://scitechdaily.com/images/DNA-Technology-Concept.gif" alt="Geneticist" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-300">
                <div class="absolute bottom-0 w-full bg-black bg-opacity-70 p-4 text-lg font-bold text-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    DNA Simulation
                </div>
            </div>
            <!-- Character Card 3 -->
            <div class="relative group bg-gray-800 rounded-2xl shadow-lg overflow-hidden transition-all duration-300 transform hover:scale-110 hover:shadow-2xl cursor-pointer w-60 h-80">
                <img src="https://media.tenor.com/TcSYAlWSHC0AAAAM/bioinformatics-market.gif" alt="Bioinformatician" class="w-full h-full object-cover opacity-80 group-hover:opacity-100 transition-opacity duration-300">
                <div class="absolute bottom-0 w-full bg-black bg-opacity-70 p-4 text-lg font-bold text-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    ML Risk Analysis
                </div>
            </div>
        </div>
    </section>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const loadingScreen = document.getElementById('loading-screen');
            window.addEventListener('load', function () {
                loadingScreen.style.display = 'none';
            });
            // Typewriter effect for the welcome message
            const text = "Welcome to Illumina Education";
            const typewriterElement = document.querySelector(".typewriter");
            const sloganElement = document.getElementById("slogan");
            let index = 0;
            function type() {
                if (index < text.length) {
                    const span = document.createElement('span');
                    span.textContent = text.charAt(index) === ' ' ? '\u00A0' : text.charAt(index); // Use non-breaking space for spaces
                    span.classList.add('text');
                    typewriterElement.appendChild(span);
                    setTimeout(() => {
                        span.style.opacity = 1;
                    }, 50 * index);
                    index++;
                    setTimeout(type, 80);
                } else {
                    // Once typing is finished, show the slogan
                    sloganElement.style.opacity = 1; // Make slogan visible
                }
            }
            type();
            // Fade in effect for other elements
            const fadeInElements = document.querySelectorAll('.fade-in');
            window.addEventListener('scroll', function () {
                fadeInElements.forEach(function (element) {
                    if (element.getBoundingClientRect().top < window.innerHeight) {
                        element.classList.add('visible');
                    }
                });
            });
        });
    </script>
</body>
</html>