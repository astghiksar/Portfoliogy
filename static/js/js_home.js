document.addEventListener('DOMContentLoaded', function () {
    // Check if the user is logged in
    const userId = sessionStorage.getItem('user_id'); // Use sessionStorage for session persistence
    const loginBtn = document.getElementById('login-btn');

    if (userId) {
        // Get the username from session or another place
        const username = sessionStorage.getItem('username');
        loginBtn.innerHTML = `Welcome, ${username}`; // Change button text
        loginBtn.href = "#"; // Disable further clicking
    }
});

function toggleDropdown() {
  const dropdownMenu = document.getElementById("dropdown-menu");
  dropdownMenu.classList.toggle("show");
}

// Close the dropdown if clicked outside
window.addEventListener("click", function (event) {
  const dropdownMenu = document.getElementById("dropdown-menu");
  const loginBtn = document.querySelector(".login-btn");
  if (!loginBtn.contains(event.target) && !dropdownMenu.contains(event.target)) {
    dropdownMenu.classList.remove("show");
  }
});
