---
layout: tailwind
title: DNA Animation
permalink: /dnasimulation/
show_reading_time: false
---

```jsx
import React, { useState } from 'react';
import axios from 'axios';
import Confetti from 'react-confetti';

function App() {
  const [organism, setOrganism] = useState('');
  const [gene, setGene] = useState('');
  const [result, setResult] = useState(null);
  const [confetti, setConfetti] = useState(false);

  // Dropdown preset options
  const commonOrganisms = [
    { label: 'Human', value: 'homo_sapiens' },
    { label: 'Mouse', value: 'mus_musculus' },
    { label: 'Zebrafish', value: 'danio_rerio' },
    { label: 'Fruit Fly', value: 'drosophila_melanogaster' },
    { label: 'Yeast', value: 'saccharomyces_cerevisiae' },
  ];

  const commonGenes = [
    'TP53',
    'BRCA1',
    'EGFR',
    'ACTB',
    'GAPDH',
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!organism || !gene) {
      alert('Please provide both organism and gene.');
      return;
    }

    try {
      const response = await axios.post('http://127.0.0.1:5024/api/sequence', {
        organism,
        gene,
      }, { withCredentials: true });

      setResult(response.data);
      setConfetti(true);
      setTimeout(() => setConfetti(false), 3000);
    } catch (error) {
      setResult({ error: error.response?.data?.error || 'An error occurred' });
      setConfetti(false);
    }
  };

  const handleDropdownSelect = (type, value) => {
    if (type === 'organism') setOrganism(value);
    if (type === 'gene') setGene(value);
  };

  return (
    <div className="App" style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>DNA Sequence Finder</h1>

      {confetti && <Confetti />}

      <form onSubmit={handleSubmit} style={{ marginBottom: '2rem' }}>
        {/* Dropdown selectors */}
        <div style={{ display: 'flex', gap: '1rem', marginBottom: '1rem' }}>
          <div>
            <label>Choose an organism:</label>
            <select
              value={organism}
              onChange={(e) => handleDropdownSelect('organism', e.target.value)}
            >
              <option value="">-- Select Organism --</option>
              {commonOrganisms.map((o) => (
                <option key={o.value} value={o.value}>{o.label}</option>
              ))}
            </select>
          </div>

          <div>
            <label>Choose a gene:</label>
            <select
              value={gene}
              onChange={(e) => handleDropdownSelect('gene', e.target.value)}
            >
              <option value="">-- Select Gene --</option>
              {commonGenes.map((g) => (
                <option key={g} value={g}>{g}</option>
              ))}
            </select>
          </div>
        </div>

        {/* Manual input fallback */}
        <div style={{ marginBottom: '1rem' }}>
          <label>Or type organism manually:</label><br />
          <input
            type="text"
            placeholder="e.g., homo_sapiens"
            value={organism}
            onChange={(e) => setOrganism(e.target.value)}
            style={{ width: '250px' }}
          />
        </div>

        <div style={{ marginBottom: '1rem' }}>
          <label>Or type gene manually:</label><br />
          <input
            type="text"
            placeholder="e.g., TP53"
            value={gene}
            onChange={(e) => setGene(e.target.value)}
            style={{ width: '250px' }}
          />
        </div>

        <button type="submit">Get DNA Sequence</button>
      </form>

      {/* Results display */}
      {result && (
        <div style={{ marginTop: '2rem' }}>
          {result.error ? (
            <div style={{ color: 'red' }}>{result.error}</div>
          ) : (
            <div style={{ border: '1px solid #ccc', padding: '1rem', borderRadius: '8px' }}>
              <h2>Sequence Info</h2>
              <p><strong>Gene:</strong> {result.gene}</p>
              <p><strong>Organism:</strong> {result.organism}</p>
              <p><strong>Ensembl ID:</strong> {result.ensembl_id}</p>
              <p><strong>Sequence (first 30 bases):</strong><br /><code>{result.sequence}</code></p>
            </div>
          )}
        </div>
      )}

      {/* Example suggestions - trimmed down to 3-4 */}
      <div style={{ marginTop: '3rem' }}>
        <h3>Popular Queries:</h3>
        <div style={{ display: 'flex', gap: '1rem' }}>
          {[
            { organism: 'homo_sapiens', gene: 'TP53' },
            { organism: 'mus_musculus', gene: 'BRCA1' },
            { organism: 'danio_rerio', gene: 'EGFR' },
            { organism: 'drosophila_melanogaster', gene: 'GAPDH' },
          ].map((example, idx) => (
            <div
              key={idx}
              onClick={() => {
                setOrganism(example.organism);
                setGene(example.gene);
              }}
              style={{
                padding: '1rem',
                border: '1px solid #ccc',
                borderRadius: '8px',
                cursor: 'pointer',
                background: '#f9f9f9',
              }}
            >
              <strong>{example.gene}</strong><br />
              <em>{example.organism}</em>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
