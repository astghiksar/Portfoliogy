document.addEventListener('DOMContentLoaded', () => {
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const full_name = document.getElementById('full_name').value.trim();
      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value.trim();
      const confirm_password = document.getElementById('confirm_password').value.trim();

      if (!full_name || !email || !password || !confirm_password) {
        alert('All fields are required.');
        return;
      }

      if (password !== confirm_password) {
        alert('Passwords do not match.');
        return;
      }

      try {
        const response = await fetch('/signup', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ full_name, email, password, confirm_password }),
        });

        if (!response.ok) {
          const error = await response.json();
          throw new Error(error.message || 'Server Error');
        }

        const data = await response.json();
        alert(data.message || 'Registration successful!');
        window.location.href = '/login'; // Redirect to login page
      } catch (err) {
        console.error('Error:', err.message);
        alert(err.message || 'Registration failed.');
      }
    });
  }

  document.querySelector('.sign-in-form')?.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('Form submitted!');
  });
});
