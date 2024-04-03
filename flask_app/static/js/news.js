
const searchInput = document.querySelector('.search_container input');
const newsArticles = document.querySelectorAll('.subsec');


const filterArticles = () => {
    const searchTerm = searchInput.value.toLowerCase();

    newsArticles.forEach(article => {
        const title = article.querySelector('.featured_title').textContent.toLowerCase();
        const body = article.querySelector('.featured_body').textContent.toLowerCase();
         
        if (title.includes(searchTerm) || body.includes(searchTerm)) {
            article.style.display = 'block';
        } else {
            article.style.display = 'none';
        }
    });
};

// Event listener for search input
searchInput.addEventListener('input', filterArticles);
