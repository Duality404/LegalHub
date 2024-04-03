document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.querySelector('.job-search');
    const jobs = document.querySelectorAll('.job');

    searchInput.addEventListener('input', function () {
        const searchTerm = searchInput.value.toLowerCase().trim();

        jobs.forEach(job => {
            console.log(job);
            const title = job.querySelector('.job-title').textContent.toLowerCase();
            const specialization = job.querySelector('.job-specialization').textContent.toLowerCase();

            if (title.includes(searchTerm) || specialization.includes(searchTerm)) {
                job.style.display = 'block';
            } else {
                job.style.display = 'none';
            }
        });
    });
});
