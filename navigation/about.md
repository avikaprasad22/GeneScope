---
layout: tailwind
permalink: /about/
show_reading_time: false 
menu: nav/home.html
---

<style>
  body {
    font-family: Arial, sans-serif;
  }
  
  .page-content {
    text-align: center;
  }

  .header {
    background: linear-gradient(to bottom, #cce4ff, white);
    padding: 20px 6px;
    color: black;
    text-align: center;
  }

  .header h1 {
    font-size: 40px;
    font-weight: bold;
    color: #1e3a8a;
  }

  .content {
    max-width: 800px;
    margin: 0 auto;
    font-size: 18px;
    color: #4b5563;
  }

  .section {
    max-width: 900px;
    margin: 40px auto;
    padding: 16px;
  }

  .section h2 {
    font-size: 30px;
    font-weight: bold;
    color: #1e3a8a;
  }

  .section-highlight {
    margin-bottom: 40px; /* Added for gap */
    background: linear-gradient(to bottom, #93c5fd, #3b82f6);
    padding: 20px 6px;
    color: white;
  }

  .section-highlight h2 {
    font-size: 40px;
    font-weight: bold;
    color: #1e3a8a;
    margin-bottom: 12px;
  }

  .section-highlight .content {
    max-width: 800px;
    margin: 0 auto;
    font-size: 18px;
    color: white;
  }

  .section-documentation {
    background: linear-gradient(to bottom, #1e3a8a, #0f172a);
    padding: 24px 6px;
    color: #e5e7eb;
  }

  .section-documentation h2 {
    font-size: 40px;
    font-weight: bold;
    color: #93c5fd;
    margin-bottom: 12px;
  }

  .section-documentation .content {
    max-width: 800px;
    margin: 0 auto;
    font-size: 18px;
    color: #e5e7eb;
  }

  .section-documentation a {
    color: #60a5fa;
    text-decoration: underline;
  }

  .section-documentation a:hover {
    color: #bfdbfe;
  }

  .buttons button {
    background-color: #2563eb;
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 25px;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    margin: 10px;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
  }

  .buttons button:hover {
    background-color: #1d4ed8;
  }

  .popup {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
    display: none;
    align-items: center;
    justify-content: center;
  }

  .popup-content {
    background: white;
    color: black; 
    padding: 20px;
    border-radius: 10px;
    width: 350px;
    position: relative;
    box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.3);
  }

  .popup-content button {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 20px;
    background: none;
    border: none;
    cursor: pointer;
  }

  .popup ul {
    text-align: left;
    color: #4b5563;
  }
</style>

<div class="header">
  <h1>About Us</h1>
  <p class="content">
    The GeneScope Biotech Education Game is an innovative initiative designed to engage students and the community in the fascinating world of biotechnology. Through interactive gameplay and real-world challenges, participants explore DNA, genetics, and cutting-edge scientific advancements in a fun and immersive way.
  </p>
</div>

<div class="page-content">
  <div class="section-highlight">
    <h2>Our Mission & Vision</h2>
    <p class="content">
      Our mission is to inspire the next generation of scientists and innovators by making biotechnology accessible and engaging. We envision a world where learning is interactive, inclusive, and drives curiosity in STEM fields. We aim to spark curiosity, inspire future scientists, and make biotech education accessible to all.
    </p>
  </div>

  <div class="section-documentation">
    <h2>Documentation</h2>
    <p class="content">
      We document each phase thoroughly, including decisions on tech stack, UI/UX principles, and data sourcing. Planning is tracked through milestones and feedback loops with educators and students. Upcoming improvements include multiplayer functionality, adaptive question difficulty, and expanded gene datasets. For detailed behind-the-scenes updates, visit our <a href="http://127.0.0.1:4504/genescope/blogs/" target="_blank">Project Blog</a>.
    </p>
  </div>

  <div class="buttons">
    <button onclick="openPopup('teamPopup')">Meet Our Team</button>
    <button onclick="openPopup('contactPopup')">Contact Us</button>
  </div>
</div>

<div id="teamPopup" class="popup" onclick="closePopup(event, 'teamPopup')">
  <div class="popup-content">
    <button onclick="closePopup(event, 'teamPopup')">&times;</button>
    <h2>Our Team</h2>
    <ul>
      <li><strong>Avika</strong> - Scrum Master</li>
      <li><strong>Nora</strong> - Assistant Scrum Master</li>
      <li><strong>Soni</strong> - DNA Sequencing Simulation and AI Voice Bot</li>
      <li><strong>Katherine</strong> - UI Design and Implementation</li>
      <li><strong>Gabi</strong> - Trivia Question System</li>
      <li><strong>Zoe</strong> - Matching Game and Additional Quizzes</li>
    </ul>
  </div>
</div>

<div id="contactPopup" class="popup" onclick="closePopup(event, 'contactPopup')">
  <div class="popup-content">
    <button onclick="closePopup(event, 'contactPopup')">&times;</button>
    <h2>Get in Touch</h2>
    <p>Email: <a href="mailto:katherine.yx.chen@gmail.com">katherine.yx.chen@gmail.com</a></p>
    <p>Phone: +1 (858) 456-7890</p>
    <p>We are excited to collaborate with you!</p>
  </div>
</div>

<script>
  function openPopup(id) {
    document.getElementById(id).style.display = "flex";
  }

  function closePopup(event, id) {
    if (event.target.classList.contains("popup") || event.target.tagName === "BUTTON") {
      document.getElementById(id).style.display = "none";
    }
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      document.querySelectorAll(".popup").forEach(popup => popup.style.display = "none");
    }
  });
</script>