document.addEventListener('DOMContentLoaded', function () {
    const userId = sessionStorage.getItem('user_id'); 
    const loginBtn = document.getElementById('login-btn');

    if (userId) {
        const username = sessionStorage.getItem('username');
        loginBtn.innerHTML = `Welcome, ${username}`; 
        loginBtn.href = "#"; 
    }
});

function toggleDropdown() {
  const dropdownMenu = document.getElementById("dropdown-menu");
  dropdownMenu.classList.toggle("show");
}

window.addEventListener("click", function (event) {
  const dropdownMenu = document.getElementById("dropdown-menu");
  const loginBtn = document.querySelector(".login-btn");
  if (!loginBtn.contains(event.target) && !dropdownMenu.contains(event.target)) {
    dropdownMenu.classList.remove("show");
  }
});
