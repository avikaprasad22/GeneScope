---
layout: tailwind
title: Illumina Biotech
search_exclude: true
hide: true
show_reading_time: false
---

<!-- Header -->
<header class="z-10 sticky justify-items-center w-full top-0 grid grid-cols-5 bg-white justify-center p-4 drop-shadow">
    <div class="col-span-2 flex gap-x-12 mt-3 justify-self-end" id="link-bar-1">
        <a href="{{site.baseurl}}/trivia" class="text-sm/6 font-semibold text-gray-900">Trivia</a>
        <a href="{{site.baseurl}}/dnasimulation" class="text-sm/6 font-semibold text-gray-900">DNA Simulation</a>
    </div>
    <div class="p-2" id="home-btn">
        <a href="{{site.baseurl}}/" class="text-sm/6 font-bold text-rose-600">
            <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="30" height="30" viewBox="0,0,256,256">
                <g fill="#2563EB" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10">
                    <g transform="scale(10.66667,10.66667)">
                        <path d="M12,2c-0.26712,0.00003 -0.52312,0.10694 -0.71094,0.29688l-10.08594,8.80078c-0.12774,0.09426 -0.20313,0.24359 -0.20312,0.40234c0,0.27614 0.22386,0.5 0.5,0.5h2.5v8c0,0.552 0.448,1 1,1h4c0.552,0 1,-0.448 1,-1v-6h4v6c0,0.552 0.448,1 1,1h4c0.552,0 1,-0.448 1,-1v-8h2.5c0.27614,0 0.5,-0.22386 0.5,-0.5c0.00001,-0.15876 -0.07538,-0.30808 -0.20312,-0.40234l-10.08008,-8.79492z"></path>
                    </g>
                </g>
            </svg>
        </a>
    </div>
    <div class="col-span-2 flex gap-x-12 mt-3 justify-self-start" id="link-bar-2">
        <a href="{{site.baseurl}}/about" class="text-sm/6 font-semibold text-gray-900">About Us</a>
        <a href="{{site.baseurl}}/search/" class="text-sm/6 font-semibold text-gray-900">Search</a>
        <a id="signup-login" href="{{ site.baseurl }}/login" class="text-blue-600 font-extrabold tracking-tight">Sign Up | Login</a>
        <a hidden id="profile" href="{{site.baseurl}}/bookworms_profile" class="text-rose-600 font-extrabold tracking-tight">Profile</a>
    </div>
</header>

<!-- Hero Section -->
<section id="welcome" class="h-screen flex flex-col items-center justify-center text-center bg-cover bg-center relative" style="background-image: url('https://scitechdaily.com/images/DNA-Genetics.gif');">
    <div class="absolute inset-0 bg-black opacity-50"></div>
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
        The Illumina Biotech Education Game is designed to immerse students in the world of biotechnology.
        Through interactive gameplay, students explore DNA, genetics, and scientific advancements.
    </p>
</section>

<!-- Our Mission Section -->
<section id="mission" class="py-20 text-center bg-black">
    <h3 class="text-5xl font-bold text-white fade-in">Our Mission</h3>
    <p class="text-xl text-gray-300 mt-4 max-w-4xl mx-auto fade-in">
        Our mission is to make biotech education fun, engaging, and accessible to all.
    </p>
</section>

<!-- Interactive Activities Section -->
<section id="ai-solutions" class="py-20 bg-gray-900">
    <h2 class="text-5xl font-bold text-center text-white mb-10 fade-in">Interactive Activities</h2>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mx-auto max-w-6xl">
        <div class="bg-white p-6 rounded-lg shadow-lg hover:scale-105 ai-card">
            <h3 class="text-3xl font-bold mb-2 text-black">Virtual Lab Simulation</h3>
            <p class="text-xl text-gray-700">Explore DNA sequencing processes.</p>
        </div>
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

<!-- Typewriter Effect Script -->
<script>
document.addEventListener("DOMContentLoaded", function () {
    const text = "Illumina Biotech";
    let index = 0;
    const speed = 100; // typing speed in milliseconds
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

<!-- Custom Styles -->
<style>
/* Blue Scrollbar */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background: #2563EB;
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: #1E40AF;
}
</style>