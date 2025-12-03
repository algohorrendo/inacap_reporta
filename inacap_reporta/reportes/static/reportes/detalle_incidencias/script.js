document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('responderForm');
    if (form) {
        form.addEventListener('submit', function(e) {
            let txt = form.comentario.value.trim();
            if (txt === "") {
                e.preventDefault();
                alert("El comentario no puede estar vacío.");
            }
        });
    }
});
