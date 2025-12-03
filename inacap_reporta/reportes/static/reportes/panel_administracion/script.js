document.addEventListener('DOMContentLoaded', function () {
    // Puedes agregar aquí el manejo dinámico de la administración
    // Por ahora solo muestra alerts en los botones de menú
    document.querySelectorAll('nav a').forEach(function(el){
        el.addEventListener('click', function(e){
            e.preventDefault();
            alert('Funcionalidad en desarrollo: ' + el.textContent);
        });
    });
});
