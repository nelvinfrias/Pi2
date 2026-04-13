// Toggle tema claro y oscuro con iconos dinámicos
document.addEventListener('DOMContentLoaded', function() {
    const btnTema = document.getElementById("toggleTema");
    const html = document.documentElement;
    
    // Cargar tema guardado
    const temaGuardado = localStorage.getItem("tema") || "dark";
    html.setAttribute("data-theme", temaGuardado);
    actualizarIcono(temaGuardado);
    
    // Evento click
    btnTema.addEventListener("click", function() {
        const temaActual = html.getAttribute("data-theme");
        const nuevoTema = temaActual === "light" ? "dark" : "light";
        
        // Cambiar tema con transición suave
        html.style.transition = 'all 0.3s ease';
        html.setAttribute("data-theme", nuevoTema);
        localStorage.setItem("tema", nuevoTema);
        
        // Actualizar icono
        actualizarIcono(nuevoTema);
        
        // Animación botón
        this.style.transform = 'rotate(180deg) scale(1.2)';
        setTimeout(() => {
            this.style.transform = 'scale(1)';
        }, 200);
    });
    
    function actualizarIcono(tema) {
        const icono = btnTema.querySelector('i');
        icono.className = tema === "light" ? 'fa-solid fa-sun' : 'fa-solid fa-moon';
    }
});