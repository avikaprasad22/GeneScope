---
layout: tailwind
permalink: /news/
author: Katherine Chen
show_reading_time: false
menu: nav/home.html
---

<div style="padding-top: 40px;"></div>

<!-- Filters Section -->
<form id="filter-form" class="max-w-4xl mx-auto p-4 bg-white rounded-xl shadow-md space-y-4 text-black">
  <h2 class="text-xl font-semibold">Filter News</h2>

  <!-- Endpoint Selection -->
  <div class="flex flex-col md:flex-row md:items-center md:space-x-6 space-y-2 md:space-y-0">
    <label class="flex items-center space-x-2">
      <input type="radio" name="endpoint" value="science-news" checked />
      <span class="text-gray-700">Top Science Headlines</span>
    </label>
    <label class="flex items-center space-x-2">
      <input type="radio" name="endpoint" value="everything-news" />
      <span class="text-gray-700">Illumina News (Company + Genes, DNA, CRISPR)</span>
    </label>
  </div>

  <!-- Input Filters -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <input type="text" name="q" placeholder="Keyword (for science headlines)" class="border p-2 rounded text-black science-only" />
    <!-- <input type="date" name="from" class="border p-2 rounded text-black everything-only hidden" /> -->
    <select name="sortBy" class="border p-2 rounded bg-blue-800 text-white everything-only hidden">
      <option value="">Sort By</option>
      <option value="publishedAt">Published At (Date)</option>
      <option value="relevancy">Relevancy</option>
      <option value="popularity">Popularity</option>
    </select>
    <!-- <select name="searchIn" class="border p-2 rounded bg-blue-800 text-white everything-only hidden">
      <option value="">Search In</option>
      <option value="title">Title</option>
      <option value="description">Description</option>
      <option value="content">Content</option>
      <option value="title,description">Title + Description</option>
    </select> -->
  </div>

  <!-- Buttons -->
  <div class="flex space-x-4">
    <button type="submit" class="bg-blue-800 text-white px-4 py-2 rounded hover:bg-blue-700">Search</button>
    <button type="button" id="clear-button" class="bg-gray-400 text-white px-4 py-2 rounded hover:bg-gray-500">Clear</button>
  </div>
</form>

<!-- News Results -->
<div id="science-news" class="max-w-4xl mx-auto mt-6">
  <p>Loading news...</p>
</div>

<script type="module">
  import { pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

  async function fetchNews(params) {
    const container = document.getElementById("science-news");
    container.innerHTML = "<p>Loading news...</p>";

    try {
      let endpointPath = "/api/science-news";
      if (params.endpoint === "everything-news") {
        endpointPath = "/api/everything-news";
      }

      // Always use default page size
      params.pageSize = "10";

      // Expanded query for everything-news
      if (params.endpoint === "everything-news") {
        params.q = "Illumina Inc OR genes OR DNA OR genomics OR CRISPR OR biotech";
      }

      const queryParams = new URLSearchParams();
      for (const key in params) {
        if (key !== "endpoint" && params[key]) {
          queryParams.append(key, params[key]);
        }
      }

      const response = await fetch(pythonURI + `${endpointPath}?${queryParams.toString()}`);
      // const response = await fetch(`http://127.0.0.1:8504${endpointPath}?${queryParams.toString()}`);

      if (!response.ok) {
        const errData = await response.json().catch(() => null);
        throw new Error(errData?.error || response.statusText);
      }

      const data = await response.json();
      container.innerHTML = "";

      if (!data.articles || data.articles.length === 0) {
        container.innerHTML = "<p>No articles found.</p>";
        return;
      }

      data.articles.forEach(article => {
        const card = document.createElement("div");
        card.className = "bg-white rounded-lg shadow-md p-6 mb-6";

        card.innerHTML = `
          <h3 class="text-lg font-semibold mb-2">
            <a href="${article.url}" target="_blank" class="text-blue-700 hover:underline">${article.title}</a>
          </h3>
          ${article.urlToImage ? `<img src="${article.urlToImage}" class="w-full md:w-1/3 float-right ml-4 rounded mb-2" alt="News image">` : ""}
          <p class="text-gray-700 mb-3">${article.description || ""}</p>
          <div class="text-sm text-gray-500">
            <span><strong>Source:</strong> ${article.source.name}</span> &nbsp;|&nbsp;
            <span><strong>Published:</strong> ${new Date(article.publishedAt).toLocaleString()}</span>
          </div>
          <div class="clear-both"></div>
        `;

        container.appendChild(card);
      });
    } catch (err) {
      container.innerHTML = `<p class="text-red-600">Error loading news: ${err.message}</p>`;
    }
  }

  // Handle form submit
  document.getElementById("filter-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const params = {};

    for (const [key, value] of formData.entries()) {
      if (value.trim() !== "") {
        params[key] = value.trim();
      }
    }

    params.endpoint = form.querySelector('input[name="endpoint"]:checked').value;

    fetchNews(params);
  });

  // Clear filters but keep endpoint
  document.getElementById("clear-button").addEventListener("click", () => {
    const form = document.getElementById("filter-form");
    Array.from(form.elements).forEach(el => {
      if (el.name !== "endpoint" && el.type !== "radio") {
        el.value = "";
      }
    });

    const selectedEndpoint = form.querySelector('input[name="endpoint"]:checked').value;
    showFields(selectedEndpoint);

    fetchNews({
      endpoint: selectedEndpoint
    });
  });

  // Toggle filter field visibility
  function showFields(endpoint) {
    document.querySelectorAll(".everything-only").forEach(el => {
      el.classList.toggle("hidden", endpoint !== "everything-news");
    });
    document.querySelectorAll(".science-only").forEach(el => {
      el.classList.toggle("hidden", endpoint !== "science-news");
    });
  }

  // Change filters on endpoint switch
  document.querySelectorAll('input[name="endpoint"]').forEach(radio => {
    radio.addEventListener("change", () => {
      showFields(radio.value);
    });
  });

  // On page load
  window.addEventListener("DOMContentLoaded", () => {
    const selected = document.querySelector('input[name="endpoint"]:checked').value;
    showFields(selected);
    fetchNews({
      endpoint: selected,
      pageSize: "10"
    });
  });
</script>