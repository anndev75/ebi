window.addEventListener('scroll', function() {
    const header = document.getElementById('script-main-header');
    
    // Detectar cuando el usuario ha hecho scroll por debajo del header
    if (window.scrollY > (window.innerHeight - 150)) {
        header.classList.add('sticky-top');
    } else {
        header.classList.remove('sticky-top');
    }
    if (window.scrollY > 100) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});