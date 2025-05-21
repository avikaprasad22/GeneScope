<div id="dna-app" style="font-family: Arial, sans-serif; max-width: 600px; margin: auto;">
  <h3>Select Organism and Gene</h3>
  <label for="organism-select">Organism:</label>
  <select id="organism-select">
    <option value="homo_sapiens">Homo sapiens</option>
    <option value="mus_musculus">Mus musculus</option>
    <option value="drosophila_melanogaster">Drosophila melanogaster</option>
    <option value="danio_rerio">Danio rerio</option>
    <option value="caenorhabditis_elegans">Caenorhabditis elegans</option>
  </select>

  <br><br>

  <label for="gene-select">Gene:</label>
  <select id="gene-select">
    <option value="BRCA1">BRCA1</option>
    <option value="TP53">TP53</option>
    <option value="EGFR">EGFR</option>
    <option value="MYC">MYC</option>
    <option value="CFTR">CFTR</option>
  </select>

  <br><br>
  <div>
    <strong>Or type custom organism and gene:</strong><br>
    Organism: <input type="text" id="organism-input" placeholder="e.g. homo_sapiens" style="width: 200px;"/><br><br>
    Gene: <input type="text" id="gene-input" placeholder="e.g. BRCA1" style="width: 200px;"/>
  </div>

  <br>
  <button id="fetch-sequence-btn">Fetch Sequence</button>

  <h4>Suggestions:</h4>
  <div id="suggestions" style="display: flex; gap: 10px;">
    <div style="border: 1px solid #ccc; padding: 10px; width: 120px; cursor: pointer;">BRCA1 - Homo sapiens</div>
    <div style="border: 1px solid #ccc; padding: 10px; width: 120px; cursor: pointer;">TP53 - Mus musculus</div>
    <div style="border: 1px solid #ccc; padding: 10px; width: 120px; cursor: pointer;">EGFR - Danio rerio</div>
    <div style="border: 1px solid #ccc; padding: 10px; width: 120px; cursor: pointer;">MYC - Drosophila melanogaster</div>
  </div>

  <br>
  <div id="result" style="padding: 10px; background: #f0f0f0; min-height: 50px;"></div>
</div>

<script>
  (function() {
    const organismSelect = document.getElementById('organism-select');
    const geneSelect = document.getElementById('gene-select');
    const organismInput = document.getElementById('organism-input');
    const geneInput = document.getElementById('gene-input');
    const fetchBtn = document.getElementById('fetch-sequence-btn');
    const resultDiv = document.getElementById('result');
    const suggestionsDiv = document.getElementById('suggestions');

    // When clicking suggestion, fill selects and inputs
    suggestionsDiv.querySelectorAll('div').forEach(sugg => {
      sugg.addEventListener('click', () => {
        const [gene, ...orgParts] = sugg.textContent.split(' - ');
        const organism = orgParts.join(' - ');
        // set selects if options available
        setSelectValue(organismSelect, organism.toLowerCase().replace(/ /g, '_'));
        setSelectValue(geneSelect, gene);
        // set inputs
        organismInput.value = organism.toLowerCase().replace(/ /g, '_');
        geneInput.value = gene;
        fetchSequence();
      });
    });

    function setSelectValue(selectElem, val) {
      for (let option of selectElem.options) {
        if (option.value.toLowerCase() === val.toLowerCase()) {
          selectElem.value = option.value;
          return;
        }
      }
      // If no option matches, clear selection
      selectElem.value = '';
    }

    function fetchSequence() {
      // Decide whether to use selects or inputs, prioritize selects if set
      let organism = organismInput.value.trim() || organismSelect.value;
      let gene = geneInput.value.trim() || geneSelect.value;

      if (!organism || !gene) {
        alert('Please select or type both organism and gene.');
        return;
      }

      resultDiv.textContent = 'Loading sequence...';

      fetch('http://127.0.0.1:5000/api/sequence', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ organism, gene }),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok: ' + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        if (data.error) {
          resultDiv.textContent = 'Error: ' + data.error;
          return;
        }
        animateResult(`Gene: ${data.gene}\nOrganism: ${data.organism}\nEnsembl ID: ${data.ensembl_id}\nSequence (first 30 chars): ${data.sequence}`);
      })
      .catch(err => {
        resultDiv.textContent = 'Fetch error: ' + err.message;
      });
    }

    function animateResult(text) {
      resultDiv.textContent = '';
      let i = 0;
      const speed = 30; // typing speed in ms

      function typeWriter() {
        if (i < text.length) {
          resultDiv.textContent += text.charAt(i);
          i++;
          setTimeout(typeWriter, speed);
        }
      }
      typeWriter();
    }

    fetchBtn.addEventListener('click', fetchSequence);
  })();
</script>