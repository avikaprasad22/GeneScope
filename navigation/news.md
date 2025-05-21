---
layout: tailwind
permalink: /news/
author: Katherine Chen
show_reading_time: false
menu: nav/home.html
---
<div style="padding-top: 40px;"></div>

<div id="science-news">
  <p>Loading science news...</p>
</div>

<script>
  async function loadScienceNews() {
    try {
      const response = await fetch('https://newsapi.org/v2/top-headlines?category=science&language=en&pageSize=5&apiKey=68a69dddbb9341d0a5f8fe2aa38967fd');
      const data = await response.json();

      const container = document.getElementById("science-news");
      container.innerHTML = "";

      if (!data.articles || data.articles.length === 0) {
        container.innerHTML = "<p>No science news available right now.</p>";
        return;
      }

      data.articles.forEach(article => {
        const item = document.createElement("div");
        item.style.border = "1px solid #ccc";
        item.style.borderRadius = "10px";
        item.style.padding = "15px";
        item.style.marginBottom = "20px";
        item.style.backgroundColor = "#f9f9f9";
        item.style.color = "#000";
        item.style.fontSize = "18px";

        item.innerHTML = `
          <h3 style="margin-top: 0;"><a href="${article.url}" target="_blank" rel="noopener noreferrer" style="color: #000; text-decoration: underline;">${article.title}</a></h3>
          ${article.urlToImage ? `<img src="${article.urlToImage}" alt="News image" style="max-width: 150px; height: auto; float: right; margin-left: 10px; border-radius: 8px;">` : ""}
          <p style="margin-top: 10px;">${article.description || ""}</p>
          <small><strong>Source:</strong> ${article.source.name} &nbsp; | &nbsp; <strong>Published:</strong> ${new Date(article.publishedAt).toLocaleString()}</small>
          <div style="clear: both;"></div>
        `;
        container.appendChild(item);
      });

    } catch (err) {
      document.getElementById("science-news").innerHTML = `<p>Error loading news: ${err.message}</p>`;
    }
  }

  loadScienceNews();
</script>