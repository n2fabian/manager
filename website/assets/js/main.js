// Combine Harvester - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add active class to current nav item
    const currentPage = window.location.pathname.split('/').pop();
    document.querySelectorAll('.site-nav a').forEach(link => {
        if (link.getAttribute('href').includes(currentPage)) {
            link.style.backgroundColor = 'var(--primary-color)';
        }
    });
});
