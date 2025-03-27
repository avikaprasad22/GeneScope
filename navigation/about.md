---
layout: post
# title: About Us
permalink: /about/
show_reading_time: false
menu: nav/home.html
---

<!-- Tailwind CSS CDN (for testing purposes, remove in production and install via npm or yarn) -->
<script src="https://cdn.tailwindcss.com"></script>
<!-- About Us Section -->
<div class="text-center text-black bg-gradient-to-b from-blue-100 to-white py-20 px-6">
  <h1 class="text-5xl font-extrabold text-blue-900">🚀 About Us</h1>
  <p class="mt-6 text-xl text-gray-700 max-w-4xl mx-auto">
    The Illumina Biotech Education Game is an innovative initiative designed to engage students and the community in the fascinating world of biotechnology. Through interactive gameplay and real-world challenges, participants explore DNA, genetics, and cutting-edge scientific advancements in a fun and immersive way.
  </p>
</div>

<!-- Mission & Vision Section -->
<div class="max-w-5xl mx-auto text-center py-16 px-6">
  <h2 class="text-4xl font-bold text-blue-900">🌍 Our Mission & Vision</h2>
  <p class="mt-6 text-lg text-gray-700">
    Our mission is to inspire the next generation of scientists and innovators by making biotechnology accessible and engaging. We envision a world where learning is interactive, inclusive, and drives curiosity in STEM fields.
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
    <br>
  </p>
</div>

<!-- Team & Journey Section -->
<div class="text-center mt-12 space-y-8 mb-10">
  <!-- Meet Our Team -->
  <button class="bg-blue-600 text-white py-3 px-8 rounded-full text-lg font-semibold shadow-lg transition duration-300 hover:bg-blue-500"
    onclick="openPopup('teamPopup')">Meet Our Team</button>

  <!-- Our Journey -->
  <button class="bg-blue-600 text-white py-3 px-8 rounded-full text-lg font-semibold shadow-lg transition duration-300 hover:bg-blue-500"
    onclick="openPopup('historyPopup')">Our Journey</button>

  <!-- Contact Us -->
  <button class="bg-blue-600 text-white py-3 px-8 rounded-full text-lg font-semibold shadow-lg transition duration-300 hover:bg-blue-500"
    onclick="openPopup('contactPopup')">Contact Us</button>
</div>


<p class="text-center text-white-700 max-w-2xl mx-auto">
    ...
</p>


<!-- Popups -->
<div id="teamPopup" class="fixed inset-0 hidden bg-black/60 flex items-center justify-center"
  onclick="closePopup(event, 'teamPopup')">
  <div class="bg-white text-black p-8 rounded-lg w-96 relative shadow-xl">
    <button class="absolute top-3 right-3 text-gray-600 text-2xl font-bold"
      onclick="closePopup(event, 'teamPopup')">&times;</button>
    <h2 class="text-3xl font-bold text-blue-900 mb-6">👨‍💻 Our Team</h2>
    <ul class="text-left space-y-4 text-gray-700">
      <li><strong>Avika</strong> - Scrum Master</li>
      <li><strong>Nora</strong> - Assistant Scrum Master</li>
      <li><strong>Soni</strong> - Lead Developer</li>
      <li><strong>Katherine</strong> - UX Designer</li>
      <li><strong>Gabi</strong> - Research Specialist</li>
      <li><strong>Zoe</strong> - Content Strategist</li>
    </ul>
  </div>
</div>

<div id="historyPopup" class="fixed inset-0 hidden bg-black/60 flex items-center justify-center"
  onclick="closePopup(event, 'historyPopup')">
  <div class="bg-white text-black p-8 rounded-lg w-96 relative shadow-xl">
    <button class="absolute top-3 right-3 text-gray-600 text-2xl font-bold"
      onclick="closePopup(event, 'historyPopup')">&times;</button>
    <h2 class="text-3xl font-bold text-blue-900 mb-6">📜 Our History</h2>
    <ul class="text-left space-y-4 text-gray-700">
      <li><strong>2015</strong> - Conceptualized the biotech education platform</li>
      <li><strong>2018</strong> - Launched first interactive game prototype</li>
      <li><strong>2021</strong> - Partnered with top research institutions</li>
      <li><strong>2024</strong> - Expanded globally with 50,000+ users</li>
    </ul>
  </div>
</div>

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