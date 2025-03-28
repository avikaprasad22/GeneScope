
---
layout: post
# title: DNA Animation
permalink: /dnasimulation/
show_reading_time: false
menu: nav/home.html
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DNA Animation</title>
    <script src="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.js"></script>
    <style>
        canvas {
            display: block;
            background-color: black;
        }
        /* Additional styles can be added here */
    </style>
</head>
<body class="bg-gray-900">

<!-- Header and Buttons -->
<div class="absolute bottom-10 left-10 z-10 flex flex-col gap-4">
    <button onclick="changeSequence('human')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Human</button>
    <button onclick="changeSequence('virus')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Virus</button>
    <button onclick="changeSequence('bacteria')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Bacteria</button>
    <button onclick="changeSequence('strawberry')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Strawberry</button>
    <button onclick="toggleFreeze()" class="p-3 bg-gray-700 hover:bg-gray-800 text-white rounded-lg shadow-md transition duration-300">Freeze</button>
</div>

<!-- Canvas for Animation -->
<canvas id="dnaCanvas"></canvas>

<script>
    // Set up canvas
    const canvas = document.getElementById('dnaCanvas');
    const ctx = canvas.getContext('2d');
    const WIDTH = window.innerWidth;
    const HEIGHT = window.innerHeight;
    canvas.width = WIDTH;
    canvas.height = HEIGHT;

    // Define colors
    const WHITE = 'white';
    const CYTOSINE = '#ffff99'; // Pastel Yellow
    const THYMINE = '#66b2ff'; // Pastel Blue
    const GUANINE = '#ff6666'; // Pastel Red
    const ADENINE = '#99ff99'; // Pastel Green

    // Base pair mapping
    const complements = { 'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C' };
    const baseColors = { 'A': ADENINE, 'T': THYMINE, 'C': CYTOSINE, 'G': GUANINE };

    // DNA sequences
    const sequences = {
        'human': "ATGCGTACGTTGACCTAGGCTAACCGTTCAGC",
        'virus': "TTAAGCGGCTGACCGAATTCCGGTAGCTTAGG",
        'bacteria': "GCTTAGGCCAATCGTTAAGGCCGATCCTAGGT",
        'strawberry': "ATGGTGAGCTCAGTTGGTGACCTGAGGCTTCA"
    };

    let currentSequence = sequences['human'];
    let isFrozen = false;
    let angleOffset = 0;
    const baseSpacing = 40;
    const amplitude = 100;
    const speed = 0.02;
    const numBasePairs = 16;

    // Change DNA sequence
    function changeSequence(sequence) {
        currentSequence = sequences[sequence];
        angleOffset = 0; // Reset rotation for new sequence
    }

    // Toggle freeze state
    function toggleFreeze() {
        isFrozen = !isFrozen;
    }

    // Draw base pairs
    function drawBasePair(x1, y, x2, color1, color2) {
        // Draw the glow effect for each base pair
        for (let i = 0; i < 3; i++) {
            ctx.fillStyle = `rgba(${color1.r}, ${color1.g}, ${color1.b}, ${(255 - i * 80) / 255})`;
            ctx.fillRect(Math.min(x1, x2) - i, y - 4 - i, Math.abs(x1 - x2) / 2 + 2 * i, 8 + 2 * i); // Left bar with glow
            ctx.fillStyle = `rgba(${color2.r}, ${color2.g}, ${color2.b}, ${(255 - i * 80) / 255})`;
            ctx.fillRect(Math.min(x1, x2) + Math.abs(x1 - x2) / 2 - i, y - 4 - i, Math.abs(x1 - x2) / 2 + 2 * i, 8 + 2 * i); // Right bar with glow
        }
    }

    // Animate the DNA
    function animateDNA() {
        ctx.clearRect(0, 0, WIDTH, HEIGHT);
        const centerX = WIDTH / 2;
        const centerY = HEIGHT / 2;

        if (!isFrozen) {
            // Normal animated helix
            for (let i = 0; i < currentSequence.length; i++) {
                const angle = i * 0.4 + angleOffset;
                const y = 100 + i * baseSpacing;
                const x1 = centerX + amplitude * Math.sin(angle);
                const x2 = centerX - amplitude * Math.sin(angle);

                const base1 = currentSequence[i];
                const base2 = complements[base1];
                const color1 = baseColors[base1];
                const color2 = baseColors[base2];

                // Draw connecting line between base pairs
                ctx.strokeStyle = WHITE;
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.moveTo(x1, y);
                ctx.lineTo(x2, y);
                ctx.stroke();

                // Draw the base pair rungs with glow effect
                drawBasePair(x1, y, x2, hexToRgb(color1), hexToRgb(color2));

                // Draw the "nucleotide" balls (circles)
                ctx.beginPath();
                ctx.arc(x1, y, 8, 0, Math.PI * 2, false);
                ctx.fillStyle = WHITE;
                ctx.fill();

                ctx.beginPath();
                ctx.arc(x2, y, 8, 0, Math.PI * 2, false);
                ctx.fillStyle = WHITE;
                ctx.fill();
            }
        } else {
            // Frozen ladder display
            const ladderX = centerX;
            for (let i = 0; i < currentSequence.length; i++) {
                const y = 100 + i * baseSpacing;
                const base1 = currentSequence[i];
                const base2 = complements[base1];
                const color1 = baseColors[base1];
                const color2 = baseColors[base2];

                // Draw vertical bars
                ctx.fillStyle = hexToRgb(color1);
                ctx.fillRect(ladderX - 50, y - 10, 100, 20);
                ctx.fillStyle = hexToRgb(color2);
                ctx.fillRect(ladderX + 60, y - 10, 100, 20);

                // Draw horizontal lines (rungs of the ladder)
                ctx.strokeStyle = WHITE;
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.moveTo(ladderX - 50, y);
                ctx.lineTo(ladderX + 60, y);
                ctx.stroke();
            }
        }

        angleOffset += speed;
        requestAnimationFrame(animateDNA);
    }

    // Convert hex color to RGB format
    function hexToRgb(hex) {
        const bigint = parseInt(hex.replace('#', ''), 16);
        return {
            r: (bigint >> 16) & 255,
            g: (bigint >> 8) & 255,
            b: bigint & 255
        };
    }

    // Start the animation
    animateDNA();
</script>

</body>
</html>

