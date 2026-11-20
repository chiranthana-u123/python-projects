
// Mobile Navigation Menu

const menuBtn = document.getElementById("menuBtn");

const navLinks = document.querySelector(".nav-links");

menuBtn.addEventListener("click", function() {

    navLinks.classList.toggle("active");

});

// Close Menu After Clicking a Link

document.querySelectorAll(".nav-links a").forEach(link => {

    link.addEventListener("click", function() {

        navLinks.classList.remove("active");

    });

});

// Welcome Message

console.log("Welcome to Chiranthana's Portfolio!");