document.querySelector('.login-form').addEventListener('submit', (e) => {
    e.preventDefault();

    const email = e.target.querySelector('input[type="email"]').value;
    const password = e.target.querySelector('input[type="password"]').value;

    if (email && password) {
        alert(`Logged in as ${email}`); // Corrected string interpolation
    } else {
        alert('Please fill in all fields');
    }
});
