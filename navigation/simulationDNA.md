---
layout: tailwind
# title: DNA Animation
permalink: /dnasimulation/
show_reading_time: false
---
<div class="flex flex-col items-center justify-center min-h-screen bg-black text-white">
    <!-- Header and Buttons -->
    <div class="absolute bottom-10 left-10 z-10 flex flex-col gap-4">
        <button onclick="changeSequence('human')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Human</button>
        <button onclick="changeSequence('virus')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Virus</button>
        <button onclick="changeSequence('bacteria')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Bacteria</button>
        <button onclick="changeSequence('strawberry')" class="p-3 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg shadow-md transition duration-300">Strawberry</button>
        <button id="freezeButton" onclick="toggleFreeze()" class="p-3 bg-gray-700 hover:bg-gray-800 text-white rounded-lg shadow-md transition duration-300">Freeze</button>
    </div>


<!-- Canvas for Animation -->
<canvas id="dnaCanvas" ></canvas>
</div>


<script>
    const canvas = document.getElementById('dnaCanvas');
    const ctx = canvas.getContext('2d');
    const WIDTH = window.innerWidth;
    const HEIGHT = window.innerHeight;
    canvas.width = WIDTH;
    canvas.height = HEIGHT;

    let isFrozen = false;

    function toggleFreeze() {
        isFrozen = !isFrozen;
        document.getElementById('freezeButton').textContent = isFrozen ? 'Unfreeze' : 'Freeze';
    }

    const baseColors = {
        'A': '#99ff99', // Green
        'T': '#66b2ff', // Blue
        'C': '#ffff99', // Yellow
        'G': '#ff6666'  // Red
    };

    const complements = { 'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C' };

    let currentSequence = "ATCGATCGATCG"; // default fallback
    let angleOffset = 0;
    const baseSpacing = 40;
    const amplitude = 100;
    const speed = 0.02;

    async function changeSequence(organism) {
        try {
            const response = await fetch("http://127.0.0.1:8206/sequence", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ organism: organism })
            });

            const data = await response.json();
            currentSequence = data.sequence.toUpperCase().replace(/[^ATCG]/g, '');
            angleOffset = 0;
        } catch (err) {
            console.error("Failed to fetch DNA sequence:", err);
        }
    }

    function animateDNA() {
        ctx.clearRect(0, 0, WIDTH, HEIGHT);
        const centerX = WIDTH / 2;

        if (!isFrozen) {
            for (let i = 0; i < currentSequence.length; i++) {
                const angle = i * 0.4 + angleOffset;
                const y = 100 + i * baseSpacing;
                const x1 = centerX + amplitude * Math.sin(angle);
                const x2 = centerX - amplitude * Math.sin(angle);

                const base1 = currentSequence[i];
                const base2 = complements[base1] || 'A'; // Default fallback

                const color1 = baseColors[base1] || 'gray';
                const color2 = baseColors[base2] || 'gray';

                ctx.strokeStyle = 'white';
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.moveTo(x1, y);
                ctx.lineTo(x2, y);
                ctx.stroke();

                ctx.fillStyle = color1;
                ctx.beginPath();
                ctx.arc(x1, y, 8, 0, Math.PI * 2, false);
                ctx.fill();

                ctx.fillStyle = color2;
                ctx.beginPath();
                ctx.arc(x2, y, 8, 0, Math.PI * 2, false);
                ctx.fill();
            }
        }

        angleOffset += speed;
        requestAnimationFrame(animateDNA);
    }

    animateDNA();
</script>
