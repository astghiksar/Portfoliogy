// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
  // Get all toggle buttons
  const toggleButtons = document.querySelectorAll('.toggle-button');

  // Loop through each toggle button
  toggleButtons.forEach(button => {
    button.addEventListener('click', function() {
      // Find the associated answer element
      const answer = this.closest('.faq-item').querySelector('.faq-answer');

      // Toggle the visibility of the answer
      answer.style.display = (answer.style.display === 'block') ? 'none' : 'block';

      // Change the + to - when the answer is visible, and vice versa
      this.textContent = (answer.style.display === 'block') ? '−' : '+';
    });
  });
});

document.getElementById("scrollButton").addEventListener("click", () => {
  const element = document.getElementById("templates");
  const headerOffset = 200; // Increase this value slightly if text is cut off
  const elementPosition = element.getBoundingClientRect().top;
  const offsetPosition = elementPosition + window.scrollY - headerOffset;

  window.scrollTo({
    top: offsetPosition,
    behavior: "smooth",
  });
});
