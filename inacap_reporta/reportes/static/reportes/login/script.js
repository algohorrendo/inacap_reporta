document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loginForm');
    if(form){
        form.addEventListener('submit', function (e) {
            // Solo demostraremos el error en cliente, no autenticación real
            let user = form.username.value.trim();
            let pass = form.password.value.trim();
            if (user === "" || pass === "") {
                e.preventDefault();
                document.getElementById('login-error').textContent = "Rellena ambos campos.";
            }
        });
    }
});
