const MENU_POR_ROL = {
    admin: [
        { texto: "Usuarios", href: "admin-usuarios.html" },
        { texto: "Configuracion", href: "admin-configuracion.html" },
    ],
    coordinador: [
        { texto: "Academico", href: "coordinador-academico.html" },
        { texto: "Espacios", href: "coordinador-espacios.html" },
        { texto: "Horarios", href: "coordinador-horarios.html" },
        { texto: "Docentes/Estudiantes", href: "coordinador-personas.html" },
        { texto: "Solicitudes", href: "coordinador-solicitudes.html" },
    ],
    docente: [
        { texto: "Mi horario", href: "docente-horario.html" },
        { texto: "Solicitar cambio", href: "docente-solicitar.html" },
        { texto: "Mis solicitudes", href: "docente-solicitudes.html" },
    ],
    estudiante: [
        { texto: "Mi horario", href: "estudiante-horario.html" },
    ],
    personal_admin: [
        { texto: "Buscar horarios", href: "buscador-horarios.html" },
    ],
};

function renderizarLayout(usuario, paginaActual) {
    const opcionesMenu = MENU_POR_ROL[usuario.rol.nombre] || [];

    const enlacesMenu = opcionesMenu
        .map((opcion) => {
            const clase = opcion.href === paginaActual ? "activo" : "";
            return `<a href="${opcion.href}" class="${clase}">${opcion.texto}</a>`;
        })
        .join("");

    const html = `
        <div class="navbar">
            <div class="marca">Sistema de Horarios</div>
            <div class="usuario-info">
                <span id="contador-notificaciones"></span>
                <a href="notificaciones.html" style="color: white;">Notificaciones</a>
                <span>${usuario.nombre_completo} (${usuario.rol.nombre})</span>
                <button id="btn-cerrar-sesion">Cerrar sesion</button>
            </div>
        </div>
        <div class="menu-lateral">
            ${enlacesMenu}
        </div>
    `;

    document.getElementById("layout-contenedor").innerHTML = html;

    document.getElementById("btn-cerrar-sesion").addEventListener("click", cerrarSesion);

    actualizarContadorNotificaciones();
}

async function actualizarContadorNotificaciones() {
    try {
        const noLeidas = await api.listarNotificacionesNoLeidas();
        const contador = document.getElementById("contador-notificaciones");
        if (contador && noLeidas.length > 0) {
            contador.textContent = `(${noLeidas.length})`;
            contador.style.color = "#f39c12";
            contador.style.fontWeight = "bold";
        }
    } catch (error) {
        console.error("No se pudo actualizar el contador de notificaciones", error);
    }
}

function iniciarPolling() {
    setInterval(actualizarContadorNotificaciones, 20000);
}