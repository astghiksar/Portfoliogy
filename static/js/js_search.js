// Handle the Continue button click
document.querySelector('.continue-btn').addEventListener('click', () => {
    const searchValue = document.querySelector('#portfolio-search').value;
    if (searchValue) {
        alert(`Searching: ${searchValue}`);
    } else {
        alert('Please enter a portfolio type to continue.');
    }
});