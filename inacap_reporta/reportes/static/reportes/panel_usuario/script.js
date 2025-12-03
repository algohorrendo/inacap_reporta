document.addEventListener('DOMContentLoaded', function() {
    // Función para actualizar la lista
    const updateButton = document.querySelector('.btn-secondary');
    if (updateButton) {
        updateButton.addEventListener('click', function(e) {
            e.preventDefault();
            location.reload();
        });
    }
    
    // Animaciones para los botones
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Confirmar antes de cerrar sesión
    const logoutLink = document.querySelector('a[href*="logout"]');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro que deseas cerrar sesión?')) {
                e.preventDefault();
            }
        });
    }
});
