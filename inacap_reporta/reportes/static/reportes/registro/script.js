document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.registro-form');
    const password1 = document.getElementById('password1');
    const password2 = document.getElementById('password2');
    
    form.addEventListener('submit', function(e) {
        // Validar que las contraseñas coincidan
        if (password1.value !== password2.value) {
            e.preventDefault();
            alert('Las contraseñas no coinciden');
            return false;
        }
        
        // Validar longitud mínima
        if (password1.value.length < 4) {
            e.preventDefault();
            alert('La contraseña debe tener al menos 4 caracteres');
            return false;
        }
    });
    
    // Validación en tiempo real
    password2.addEventListener('input', function() {
        if (password1.value !== password2.value) {
            password2.style.borderColor = '#dc3545';
        } else if (password1.value === password2.value && password1.value.length > 0) {
            password2.style.borderColor = '#28a745';
        } else {
            password2.style.borderColor = '#ddd';
        }
    });
});
