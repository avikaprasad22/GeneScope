---
layout: tailwind
title: Illumina Biotech
search_exclude: true
hide: true
show_reading_time: false
menu: nav/home.html
---

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