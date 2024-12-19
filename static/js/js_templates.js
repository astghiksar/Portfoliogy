const filterButtons = document.querySelectorAll('.filter-btn');
const templateCards = document.querySelectorAll('.template-card');

filterButtons.forEach(button => {
  button.addEventListener('click', () => {
    filterButtons.forEach(btn => btn.classList.remove('active'));
    button.classList.add('active');

    const filter = button.dataset.filter;

    templateCards.forEach(card => {
      if (filter === 'all' || card.classList.contains(filter)) {
        card.style.display = 'block';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

document.querySelector('.load-more-btn').addEventListener('click', () => {
  alert('Loading more templates...');
});

