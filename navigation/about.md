---
layout: page 
title: About Us
permalink: /about/
menu: nav/home.html
---
<!-- Tailwind CSS CDN (for testing purposes, remove in production and install via npm or yarn) -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- About Us Section -->
<div class="text-center text-black bg-gradient-to-b from-blue-100 to-white py-16 px-6">
  <h1 class="text-5xl font-extrabold text-blue-900">🚀 About Us</h1>
  <p class="mt-6 text-xl text-gray-700 max-w-4xl mx-auto">
    The Illumina Biotech Education Game is an innovative initiative designed to engage students and the community in the fascinating world of biotechnology. Through interactive gameplay and real-world challenges, participants explore DNA, genetics, and cutting-edge scientific advancements in a fun and immersive way.
  </p>
</div>

<!-- More Information Section -->
<div class="text-center mt-16 space-y-12">

  <!-- Meet Our Team -->
  <div>
    <button class="bg-blue-600 text-white py-3 px-8 rounded-full text-lg font-semibold shadow-lg transition duration-300 hover:bg-blue-500"
      onclick="openPopup('teamPopup')">Meet Our Team</button>
    <div id="teamPopup" class="fixed inset-0 hidden bg-black/60 flex items-center justify-center"
      onclick="closePopup(event, 'teamPopup')">
      <div class="bg-white text-black p-8 rounded-lg w-96 relative shadow-xl">
        <button class="absolute top-3 right-3 text-gray-600 text-2xl font-bold"
          onclick="closePopup(event, 'teamPopup')">&times;</button>
        <h2 class="text-3xl font-bold text-blue-900 mb-6">👨‍💻 Our Team</h2>
        <ul class="text-left space-y-4 text-gray-700">
          <li><strong>Avika</strong> - Scrum Master</li>
          <li><strong>Nora</strong> - Assistant Scrum Master</li>
          <li><strong>Soni</strong> - x</li>
          <li><strong>Katherine</strong> - x</li>
          <li><strong>Gabi</strong> - x</li>
          <li><strong>Zoe</strong> - x</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- Our History -->
  <div>
    <button class="bg-blue-600 text-white py-3 px-8 rounded-full text-lg font-semibold shadow-lg transition duration-300 hover:bg-blue-500"
      onclick="openPopup('historyPopup')">Our Journey</button>
     <div id="historyPopup" class="fixed inset-0 hidden bg-black/60 flex items-center justify-center"
      onclick="closePopup(event, 'historyPopup')">
      <div class="bg-white text-black p-8 rounded-lg w-96 relative shadow-xl">
        <button class="absolute top-3 right-3 text-gray-600 text-2xl font-bold"
          onclick="closePopup(event, 'historyPopup')">&times;</button>
        <h2 class="text-3xl font-bold text-blue-900 mb-6">📜 Our History</h2>
        <ul class="text-left space-y-4 text-gray-700">
          <li><strong>2010</strong> - Founded as an AI research startup</li>
          <li><strong>2015</strong> - Pioneered blockchain solutions</li>
          <li><strong>2020</strong> - Reached 10M+ global users</li>
          <li><strong>2025</strong> - Expanding into quantum computing</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<!-- Contact Us Section -->
<div class="text-center mt-16">
  <button class="bg-blue-600 text-white py-3 px-8 rounded-full text-lg font-semibold shadow-lg transition duration-300 hover:bg-blue-500"
    onclick="openPopup('contactPopup')">Contact Us</button>

  <div id="contactPopup" class="fixed inset-0 hidden bg-black/60 flex items-center justify-center"
    onclick="closePopup(event, 'contactPopup')">
    <div class="bg-white text-black p-8 rounded-lg w-96 relative shadow-xl">
      <button class="absolute top-3 right-3 text-gray-600 text-2xl font-bold"
        onclick="closePopup(event, 'contactPopup')">&times;</button>
      <h2 class="text-3xl font-bold text-blue-900 mb-6">📩 Get in Touch</h2>
      <p class="text-lg text-gray-700">
        Email: <a href="mailto:contact@yourcompany.com" class="text-blue-600 underline">contact@yourcompany.com</a>
      </p>
      <p class="text-lg text-gray-700">Phone: +1 (123) 456-7890</p>
      <p class="mt-4 text-gray-700">We are excited to collaborate with you!</p>
    </div>
  </div>
</div>

<!-- JavaScript for Popups -->
<script>
  function openPopup(id) {
    document.getElementById(id).classList.remove("hidden");
  }

  function closePopup(event, id) {
    if (event.target.classList.contains("fixed") || event.target.classList.contains("text-gray-600")) {
      document.getElementById(id).classList.add("hidden");
    }
  }

  // Close with ESC key
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      document.querySelectorAll(".fixed").forEach(popup => popup.classList.add("hidden"));
    }
  });
</script>