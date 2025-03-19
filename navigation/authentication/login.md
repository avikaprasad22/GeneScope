---
layout: page 
title: Login
permalink: /login
search_exclude: true
show_reading_time: false 
menu: nav/home.html
---
<div class="flex flex-wrap justify-between">
    <!-- Python Login Form -->
    <div class="bg-[#E8C5A4] rounded-lg p-5 shadow-lg w-[45%] border border-gray-300 mb-5 overflow-x-auto">
        <h1 class="mb-5 text-[#4B4A40] text-xl font-bold">User Login (Python/Flask)</h1>
        <form id="pythonForm" onsubmit="pythonLogin(); return false;">
            <p class="mb-3">
                <label class="text-[#4B4A40] block">GitHub ID:</label>
                <input type="text" name="uid" id="uid" required class="w-full p-2 border border-gray-300 rounded">
            </p>
            <p class="mb-3">
                <label class="text-[#4B4A40] block">Password:</label>
                <input type="password" name="password" id="password" required class="w-full p-2 border border-gray-300 rounded">
            </p>
            <p>
                <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Login</button>
            </p>
            <p id="message" class="text-red-500"></p>
        </form>
    </div>
    <div class="bg-[#E8C5A4] rounded-lg p-5 shadow-lg w-[45%] border border-gray-300 mb-5 overflow-x-auto">
        <h1 class="mb-5 text-[#4B4A40] text-xl font-bold">Sign Up</h1>
        <form id="signupForm" onsubmit="signup(); return false;">
            <p class="mb-3">
                <label class="text-[#4B4A40] block">Name:</label>
                <input type="text" name="name" id="name" required class="w-full p-2 border border-gray-300 rounded">
            </p>
            <p class="mb-3">
                <label class="text-[#4B4A40] block">GitHub ID:</label>
                <input type="text" name="signupUid" id="signupUid" required class="w-full p-2 border border-gray-300 rounded">
            </p>
            <p class="mb-3">
                <label class="text-[#4B4A40] block">Password:</label>
                <input type="password" name="signupPassword" id="signupPassword" required class="w-full p-2 border border-gray-300 rounded">
            </p>
            <p>
                <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Sign Up</button>
            </p>
            <p id="signupMessage" class="text-green-500"></p>
        </form>
    </div>
</div>

<script type="module">
    import { login, pythonURI, fetchOptions } from '{{site.baseurl}}/assets/js/api/config.js';

    // Function to handle Python login
    window.pythonLogin = function() {
        const options = {
            URL: `${pythonURI}/api/authenticate`,
            callback: pythonDatabase,
            message: "message",
            method: "POST",
            cache: "no-cache",
            body: {
                uid: document.getElementById("uid").value,
                password: document.getElementById("password").value,
            }
        };
        login(options);
    }

    // Function to handle signup
    window.signup = function() {
        const signupButton = document.querySelector("#signupForm button");

        // Disable the button and change its color
        signupButton.disabled = true;
        signupButton.classList.add("bg-gray-400", "cursor-not-allowed");

        const signupOptions = {
            URL: `${pythonURI}/api/user`,
            method: "POST",
            cache: "no-cache",
            body: {
                name: document.getElementById("name").value,
                uid: document.getElementById("signupUid").value,
                password: document.getElementById("signupPassword").value,
            }
        };

        fetch(signupOptions.URL, {
            method: signupOptions.method,
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(signupOptions.body)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Signup failed: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            document.getElementById("signupMessage").textContent = "Signup successful!";
        })
        .catch(error => {
            console.error("Signup Error:", error);
            document.getElementById("signupMessage").textContent = `Signup Error: ${error.message}`;
            // Re-enable the button if there is an error
            signupButton.disabled = false;
            signupButton.classList.remove("bg-gray-400", "cursor-not-allowed");
        });
    }

    // Function to fetch and display Python data
    function pythonDatabase() {
        const URL = `${pythonURI}/api/id`;

        fetch(URL, fetchOptions)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Flask server response: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                window.location.href = '{{site.baseurl}}/profile';
            })
            .catch(error => {
                console.error("Python Database Error:", error);
            });
    }

    // Call relevant database functions on the page load
    window.onload = function() {
         pythonDatabase();
    };
</script>
