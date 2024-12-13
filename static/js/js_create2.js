// Form submission
document.querySelector('.cv-form').addEventListener('submit', (e) => {
  e.preventDefault();
  alert('Your CV has been saved successfully!');
});

// Add More functionality

//Employment
document.addEventListener('DOMContentLoaded', () => {
  // Employment Section
  const employmentSection = document.querySelector('section:nth-of-type(3)');
  const addEmploymentButton = employmentSection.querySelector('.add-more');
  let removeEmploymentButton = employmentSection.querySelector('.remove');

  function createEmploymentFields() {
    const newEmploymentGroup = document.createElement('div');
    newEmploymentGroup.className = 'dynamic-group'; // Identify dynamic groups
    newEmploymentGroup.innerHTML = `
      <div class="form-group">
        <input type="text" placeholder="Title/Position" required />
        <input type="text" placeholder="Company" required />
      </div>
      <div class="form-group">
        <input type="date" placeholder="Start date" required />
        <input type="date" placeholder="End date" required />
      </div>
      <div class="form-group">
        <input type="text" placeholder="Location" required />
      </div>
      <br>
      <br>
      
    `;

    employmentSection.appendChild(newEmploymentGroup);
    removeEmploymentButton.style.display = 'inline-block'; // Show the remove button
  }

  addEmploymentButton.addEventListener('click', () => {
    createEmploymentFields();
  });

  removeEmploymentButton.addEventListener('click', () => {
    const dynamicGroups = employmentSection.querySelectorAll('.dynamic-group');
    if (dynamicGroups.length > 0) {
      dynamicGroups[dynamicGroups.length - 1].remove();


      if (employmentSection.querySelectorAll('.dynamic-group').length === 0) {
        removeEmploymentButton.style.display = 'none';
      }
    }
  });

  if (!employmentSection.querySelector('.dynamic-group')) {
    removeEmploymentButton.style.display = 'none';
  }
});


// Education Section
  document.addEventListener('DOMContentLoaded', () => {

  const educationSection = document.querySelector('section:nth-of-type(4)');
  const addEducationButton = educationSection.querySelector('.add-more1');
  let removeEducationButton = educationSection.querySelector('.remove-education');


  function createEducationFields() {
    const newEducationGroup = document.createElement('div');
    newEducationGroup.className = 'dynamic-group';
    newEducationGroup.innerHTML = `
      <div class="form-group">
          <input type="text" placeholder="Degree(s)" />
          <input type="text" placeholder="Name of school/institution" />
        </div>
        <div class="form-group">
          <input type="date" placeholder="Start date" />
          <input type="date" placeholder="End date" />
        </div>
        <br>
          <br>
    `;

    educationSection.appendChild(newEducationGroup);
    removeEducationButton.style.display = 'inline-block'; // Show the remove button
  }

  addEducationButton.addEventListener('click', () => {
    createEducationFields();
  });

  removeEducationButton.addEventListener('click', () => {
    const dynamicGroups = educationSection.querySelectorAll('.dynamic-group');
    if (dynamicGroups.length > 0) {
      dynamicGroups[dynamicGroups.length - 1].remove();

      if (educationSection.querySelectorAll('.dynamic-group').length === 0) {
        removeEducationButton.style.display = 'none';
      }
    }
  });

  if (!educationSection.querySelector('.dynamic-group')) {
    removeEducationButton.style.display = 'none';
  }
});

//Language

document.addEventListener('DOMContentLoaded', () => {

  const languageSection = document.querySelector('section:nth-of-type(5)');
  const addLanguageButton = languageSection.querySelector('.add-more2');
  let removeLanguageButton = languageSection.querySelector('.remove-language');


  function createLanguageFields() {
    const newLanguageGroup = document.createElement('div');
    newLanguageGroup.className = 'dynamic-group';
    newLanguageGroup.innerHTML = `
        <div class="form-group">
          <input type="text" placeholder="Language" />
          <input type="text" placeholder="Level" />
        </div>
        <br>
    `;

    languageSection.appendChild(newLanguageGroup);
    removeLanguageButton.style.display = 'inline-block'; // Show the remove button
  }

  addLanguageButton.addEventListener('click', () => {
    createLanguageFields();
  });

  removeLanguageButton.addEventListener('click', () => {
    const dynamicGroups = languageSection.querySelectorAll('.dynamic-group');
    if (dynamicGroups.length > 0) {
      dynamicGroups[dynamicGroups.length - 1].remove();

      if (languageSection.querySelectorAll('.dynamic-group').length === 0) {
        removeLanguageButton.style.display = 'none';
      }
    }
  });

  if (!languageSection.querySelector('.dynamic-group')) {
    removeLanguageButton.style.display = 'none';
  }
});

//Skills
document.addEventListener('DOMContentLoaded', () => {

  const skillSection = document.querySelector('section:nth-of-type(6)');
  const addSkillButton = skillSection.querySelector('.add-more3');
  let removeSkillButton = skillSection.querySelector('.remove-skill');


  function createSkillFields() {
    const newSkillGroup = document.createElement('div');
    newSkillGroup.className = 'dynamic-group';
    newSkillGroup.innerHTML = `
        <div class="form-group">
          <input type="text" placeholder="Skill" />
          
        </div>
        <br>
    `;

    skillSection.appendChild(newSkillGroup);
    removeSkillButton.style.display = 'inline-block'; // Show the remove button
  }

  addSkillButton.addEventListener('click', () => {
    createSkillFields();
  });

  removeSkillButton.addEventListener('click', () => {
    const dynamicGroups = skillSection.querySelectorAll('.dynamic-group');
    if (dynamicGroups.length > 0) {
      dynamicGroups[dynamicGroups.length - 1].remove();

      if (skillSection.querySelectorAll('.dynamic-group').length === 0) {
        removeSkillButton.style.display = 'none';
      }
    }
  });

  if (!skillSection.querySelector('.dynamic-group')) {
    removeSkillButton.style.display = 'none';
  }
});

//link
document.addEventListener('DOMContentLoaded', () => {

  const linkSection = document.querySelector('section:nth-of-type(7)');
  const addLinkButton = linkSection.querySelector('.add-more4');
  let removeLinkButton = linkSection.querySelector('.remove-link');


  function createLinkFields() {
    const newLinkGroup = document.createElement('div');
    newLinkGroup.className = 'dynamic-group';
    newLinkGroup.innerHTML = `
        <div class="form-group">
          <input type="text" placeholder="Label (e.g., LinkedIn)" />
          <input type="url" placeholder="Link" />
        </div>
        <br>
    `;

    linkSection.appendChild(newLinkGroup);
    removeLinkButton.style.display = 'inline-block'; // Show the remove button
  }

  addLinkButton.addEventListener('click', () => {
    createLinkFields();
  });

  removeLinkButton.addEventListener('click', () => {
    const dynamicGroups = linkSection.querySelectorAll('.dynamic-group');
    if (dynamicGroups.length > 0) {
      dynamicGroups[dynamicGroups.length - 1].remove();

      if (linkSection.querySelectorAll('.dynamic-group').length === 0) {
        removeLinkButton.style.display = 'none';
      }
    }
  });

  if (!linkSection.querySelector('.dynamic-group')) {
    removeLinkButton.style.display = 'none';
  }
});

document.addEventListener("DOMContentLoaded", () => {
  // Select all skill buttons
  const skillButtons = document.querySelectorAll(".skill");

  skillButtons.forEach(button => {
    button.addEventListener("click", () => {
      // Toggle the "selected" class on click
      button.classList.toggle("selected");
    });
  });
});


