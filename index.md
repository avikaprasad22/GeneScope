---
layout: post
title: Business
search_exclude: true
hide: true
menu: nav/home.html
show_reading_time: false
---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Illumina Interactive Biotech Education Game</title>
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
            background: url(images/dnabanner.png) no-repeat center center;
            background-size: cover;
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
        <!-- Slogan added here, initially hidden -->
        <h2 id="slogan" class="slogan text-4xl" style="color:rgb(255, 255, 255); text-shadow: 0 0 2px rgb(162, 220, 202), 0 0 2px rgb(77, 207, 168), 0 0 4px rgb(77, 207, 168), 0 0 4px rgb(77, 207, 168)">Illumina Biotech: Igniting Curiosity, Advancing Science</h2>
    </section>
    <!-- About Us Section -->
    <section id="about" class="h-screen flex flex-col items-center justify-center text-center bg-orange-100 text-black">
        <h2 class="text-7xl font-extrabold text-orange-600 fade-in mb-6">About Us</h2>
        <p class="text-3xl text-orange-900 max-w-5xl fade-in">
            The Illumina Biotech Education Game is an innovative initiative designed to engage students and the community in the fascinating world of biotechnology. Through interactive gameplay and real-world challenges, participants explore DNA, genetics, and cutting-edge scientific advancements in a fun and immersive way. 
        </p>
    </section>
    <!-- Our Mission Section -->
    <section id="mission" class="h-screen flex flex-col items-center justify-center text-center bg-purple-100 text-black">
        <h3 class="text-6xl font-bold mt-8 text-purple-900 fade-in">Our Mission</h3>
        <p class="text-3xl text-purple-700 mt-4 max-w-5xl fade-in">
            Our mission aims to spark curiosity, inspire future scientists, and make biotech education accessible to all. .
        </p>
    </section>
    <!-- AI Solutions Section -->
    <section id="ai-solutions" class="py-20 bg-blue-100">
        <h2 class="text-7xl font-bold text-center text-blue-900 mb-10 fade-in">Interactive Activites</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-blue-900">Virtual Lab Stimulation</h3>
                    <p class="text-xl text-blue-800">Explore DNA sequencing processes.</p>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-blue-900">Trivia Challenge</h3>
                    <p class="text-xl text-blue-800">Test your knowledge on genetic research breakthroughs. </p>
                </div>
            </div>
            <div class="bg-white rounded-lg shadow-lg overflow-hidden transform transition-transform duration-500 hover:scale-105">
                <div class="p-6">
                    <h3 class="text-3xl font-bold mb-2 text-blue-900">Puzzle Game</h3>
                    <p class="text-xl text-blue-800">Illustrates the impact of personalized medicine.</p>
                    <!-- <img src="https://images.squarespace-cdn.com/content/v1/57e6f18eb3db2b1dd11a2a02/1525919934875-QZQ7GVBYZZJHMN8JG7BR/homo-DNA.gif" alt="GIF" class="w-32 h-32"> -->
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
            const text = "Welcome to Illumina Education Game";
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