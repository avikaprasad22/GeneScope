---
layout: tailwind
permalink: /news/
author: Katherine Chen
show_reading_time: false
menu: nav/home.html
---

<div style="padding-top: 40px;"></div>

<!-- Tabs -->
<div class="max-w-4xl mx-auto px-4">
  <div class="flex mx-auto rounded-lg overflow-hidden gap-x-14 justify-center">
    <button id="tab-science" class="tab-btn bg-blue-800 text-white text-xl font-semibold w-[500px] py-4 rounded-lg">Top Science Headlines</button>
    <button id="tab-illumina" class="tab-btn bg-blue-900 text-white text-xl font-semibold w-[500px] py-4 rounded-lg">Illumina & Genetics News</button>
  </div>
</div>

<!-- Filters Section -->
<form id="filter-form" class="max-w-4xl mx-auto p-4 bg-white rounded-xl shadow-md space-y-4 text-black">
  <input type="hidden" name="endpoint" id="endpoint" value="science-news" />

  <!-- Science Fields -->
  <div id="science-fields" class="space-y-2">
    <input type="text" name="q" placeholder="Keyword (e.g. NASA, brain, AI...)" class="border p-2 rounded w-full text-black" />
  </div>

  <!-- Everything (Illumina) Fields -->
  <div id="everything-fields" class="everything-only hidden space-y-2">
    <select name="sortBy" class="border p-2 rounded bg-blue-800 text-white">
      <option value="">Sort By</option>
      <option value="publishedAt">Published At (Date)</option>
      <option value="relevancy">Relevancy</option>
    </select>
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

  const tabs = {
    science: {
      endpoint: "science-news",
      showScienceFields: true,
      showEverythingFields: false
    },
    illumina: {
      endpoint: "everything-news",
      showScienceFields: false,
      showEverythingFields: true
    }
  };

  const tabButtons = {
    science: document.getElementById("tab-science"),
    illumina: document.getElementById("tab-illumina")
  };

  function setTab(tabKey) {
    const tab = tabs[tabKey];
    document.getElementById("endpoint").value = tab.endpoint;

    Object.keys(tabButtons).forEach(key => {
      tabButtons[key].classList.remove("bg-blue-800", "bg-blue-900", "hover:bg-blue-700", "border-b-4");
      tabButtons[key].classList.add("bg-blue-900", "hover:bg-blue-700"); // unselected = darker
    });

    tabButtons[tabKey].classList.remove("bg-blue-900");
    tabButtons[tabKey].classList.add("bg-blue-800", "border-b-4"); // selected = lighter
    document.getElementById("science-fields").classList.toggle("hidden", !tab.showScienceFields);
    document.getElementById("everything-fields").classList.toggle("hidden", !tab.showEverythingFields);

    fetchNews({
      endpoint: tab.endpoint,
      ...(tabKey === "illumina" ? {} : { q: "" }),
      pageSize: "10"
    });
  }

  async function fetchNews(params) {
    const container = document.getElementById("science-news");
    container.innerHTML = "<p>Loading news...</p>";

    try {
      let endpointPath = "/api/science-news";
      if (params.endpoint === "everything-news") {
        endpointPath = "/api/everything-news";
        params.q = "Illumina Inc OR genes OR DNA OR genomics OR CRISPR OR biotech";
      }

      const queryParams = new URLSearchParams();
      for (const key in params) {
        if (key !== "endpoint" && params[key]) {
          queryParams.append(key, params[key]);
        }
      }

      const response = await fetch(pythonURI + `${endpointPath}?${queryParams.toString()}`);
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

  // Form submission
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

    params.endpoint = document.getElementById("endpoint").value;
    fetchNews(params);
  });

  // Clear filters
  document.getElementById("clear-button").addEventListener("click", () => {
    const form = document.getElementById("filter-form");
    form.q.value = "";
    form.sortBy.value = "";
    fetchNews({ endpoint: document.getElementById("endpoint").value, pageSize: "10" });
  });

  // Tab listeners
  tabButtons.science.addEventListener("click", () => setTab("science"));
  tabButtons.illumina.addEventListener("click", () => setTab("illumina"));

  // Initial load
  window.addEventListener("DOMContentLoaded", () => {
    setTab("science");
  });
</script>