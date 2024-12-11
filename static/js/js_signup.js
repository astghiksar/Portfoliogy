document.querySelector('.signup-form').addEventListener('submit', (e) => {
    e.preventDefault();

    const fullName = e.target.querySelector('input[type="text"]').value;
    const email = e.target.querySelector('input[type="email"]').value;
    const password = e.target.querySelector('input[type="password"]').value;

    if (fullName && email && password) {
        alert(`Thank you for signing up, ${fullName}!`); // Corrected string interpolation
    } else {
        alert('Please fill in all fields.');
    }
});
