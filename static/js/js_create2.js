// Form submission
document.querySelector('.cv-form').addEventListener('submit', (e) => {
  e.preventDefault();
  alert('Your CV has been saved successfully!');
});

// Add More functionality
document.querySelectorAll('.add-more').forEach((button) => {
  button.addEventListener('click', () => {
    const newField = document.createElement('div');
    newField.className = 'form-group';
    newField.innerHTML = `
      <input type="text" placeholder="New Field" />
      <input type="text" placeholder="Additional Detail" />
    `;
    button.parentElement.appendChild(newField);
  });
});

// Skill selection toggle
document.querySelectorAll('.skill').forEach((skill) => {
  skill.addEventListener('click', () => {
    skill.classList.toggle('selected');
    if (skill.classList.contains('selected')) {
      skill.style.backgroundColor = '#00d084';
    } else {
      skill.style.backgroundColor = '#6e44ff';
    }
  });
});