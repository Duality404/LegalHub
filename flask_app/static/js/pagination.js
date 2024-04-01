const articlesPerPage = 6;
let currentPage = 1;

const newsArticles = document.querySelectorAll('.subsec');

// Function to show articles for the current page
const showPage = (pageNumber) => {
    const startIndex = (pageNumber - 1) * articlesPerPage;
    const endIndex = pageNumber * articlesPerPage;

    newsArticles.forEach((article, index) => {
        if (index >= startIndex && index < endIndex) {
            article.style.display = 'block';
        } else {
            article.style.display = 'none';
        }
    });
};

// Function to update pagination links
const updatePagination = () => {
    const totalArticles = newsArticles.length;
    const totalPages = Math.ceil(totalArticles / articlesPerPage);

    const paginationContainer = document.querySelector('.pagination');
    paginationContainer.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
        const li = document.createElement('li');
        li.classList.add('page-item');
        if (i === currentPage) {
            li.classList.add('active');
        }
        const a = document.createElement('a');
        a.classList.add('page-link');
        a.href = '#';
        a.textContent = i;
        a.addEventListener('click', () => {
            currentPage = i;
            showPage(currentPage);
            updatePagination();
        });
        li.appendChild(a);
        paginationContainer.appendChild(li);
    }
};

// Show the initial page
showPage(currentPage);
updatePagination();
