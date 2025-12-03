document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    
    // Validación del formulario
    if (form) {
        form.addEventListener('submit', function(e) {
            const titulo = document.getElementById('titulo').value.trim();
            const categoria = document.getElementById('categoria').value;
            const descripcion = document.getElementById('descripcion').value.trim();
            const ubicacion = document.getElementById('ubicacion').value.trim();
            const urgencia = document.getElementById('urgencia').value;
            
            if (!titulo || !categoria || !descripcion || !ubicacion || !urgencia) {
                e.preventDefault();
                alert('Por favor complete todos los campos');
                return false;
            }
            
            if (descripcion.length < 10) {
                e.preventDefault();
                alert('La descripción debe tener al menos 10 caracteres');
                return false;
            }
        });
    }
    
    // Contador de caracteres para descripción
    const descripcionTextarea = document.getElementById('descripcion');
    if (descripcionTextarea) {
        const counter = document.createElement('small');
        counter.style.color = '#666';
        counter.style.float = 'right';
        counter.style.marginTop = '5px';
        
        descripcionTextarea.addEventListener('input', function() {
            const length = this.value.length;
            counter.textContent = `${length} caracteres`;
            
            if (length < 10) {
                counter.style.color = '#dc3545';
            } else {
                counter.style.color = '#28a745';
            }
        });
        
        descripcionTextarea.parentNode.appendChild(counter);
    }
    
    // Confirmación para limpiar formulario
    const resetButton = document.querySelector('button[type="reset"]');
    if (resetButton) {
        resetButton.addEventListener('click', function(e) {
            if (!confirm('¿Estás seguro que deseas limpiar el formulario?')) {
                e.preventDefault();
            }
        });
    }
});
