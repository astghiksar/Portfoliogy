// Handle category filtering
const filterButtons = document.querySelectorAll('.filter-btn');
const templateCards = document.querySelectorAll('.template-card');

filterButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Remove active class from all buttons
    filterButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    const filter = button.dataset.filter;

    // Show/hide templates based on the filter
    templateCards.forEach(card => {
      if (filter === 'all' || card.classList.contains(filter)) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// Handle "Load More" button click
document.querySelector('.load-more-btn').addEventListener('click', () => {
  alert('Loading more templates...');
});

