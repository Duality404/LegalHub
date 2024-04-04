document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('.search-bar');
    const documents = document.querySelectorAll('.document');

    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase().trim();

        documents.forEach(document => {
            const title = document.querySelector('.doc-title').textContent.toLowerCase();
            const desc = document.querySelector('.doc-desc').textContent.toLowerCase();
            const tag = document.querySelector('.tag').textContent.toLowerCase();
            if (title.includes(searchTerm) || desc.includes(searchTerm) || tag.includes(searchTerm)) {
                document.style.display = 'block';
            } else {
                document.style.display = 'none';
            }
        });
    });
});
