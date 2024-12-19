// Make the login button interactive
document.querySelector('.login-btn').addEventListener('click', () => {
  alert('Redirecting to the login page...');
});

// Add hover interaction feedback for the login button (optional, visual)
document.querySelector('.login-btn').addEventListener('mouseenter', () => {
  console.log('Login button hovered!');
});

document.querySelector('.login-btn').addEventListener('mouseleave', () => {
  console.log('Mouse left the login button!');
});

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
    var dropdown = document.getElementById('dropdown-menu');
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
}