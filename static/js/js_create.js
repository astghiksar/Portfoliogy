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