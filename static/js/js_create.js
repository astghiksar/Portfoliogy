document.querySelector('.login-btn').addEventListener('click', () => {
  alert('Redirecting to the login page...');
});

document.querySelector('.login-btn').addEventListener('mouseenter', () => {
  console.log('Login button hovered!');
});

document.querySelector('.login-btn').addEventListener('mouseleave', () => {
  console.log('Mouse left the login button!');
});

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
    var dropdown = document.getElementById('dropdown-menu');
    dropdown.style.display = (dropdown.style.display === 'block') ? 'none' : 'block';
}
