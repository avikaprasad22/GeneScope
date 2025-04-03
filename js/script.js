document.addEventListener("DOMContentLoaded", function () {
    // Fade-in effect for elements
    const fadeInElements = document.querySelectorAll('.fade-in');
    window.addEventListener('scroll', function () {
        fadeInElements.forEach(function (element) {
            if (element.getBoundingClientRect().top < window.innerHeight) {
                element.classList.add('visible');
            }
        });
    });
});
