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

const API_ORIGEN = "http://127.0.0.1:8000";

async function renderizarLayout(usuario, paginaActual) {
    const opcionesMenu = MENU_POR_ROL[usuario.rol.nombre] || [];

    let contadorSolicitudes = 0;
    if (usuario.rol.nombre === "coordinador") {
        try {
            const pendientes = await api.listarSolicitudesPendientes();
            contadorSolicitudes = pendientes.length;
        } catch (error) {
            console.error("No se pudo obtener el contador de solicitudes", error);
        }
    }

    let nombreInstitucion = "Sistema de Horarios";
    let logoUrl = null;
    try {
        const config = await api.obtenerConfiguracionPublica();
        nombreInstitucion = config.nombre_institucion;
        logoUrl = config.logo_url;
    } catch (error) {
        console.error("No se pudo cargar la configuracion de la institucion", error);
    }

    const enlacesMenu = opcionesMenu
        .map((opcion) => {
            const clase = opcion.href === paginaActual ? "activo" : "";
            const esSolicitudes = opcion.href === "coordinador-solicitudes.html";
            if (esSolicitudes && contadorSolicitudes > 0) {
                return `<a href="${opcion.href}" class="${clase} badge-notificacion" data-contador="${contadorSolicitudes}">${opcion.texto}</a>`;
            }
            return `<a href="${opcion.href}" class="${clase}">${opcion.texto}</a>`;
        })
        .join("");

    const logoHtml = logoUrl
        ? `<img src="${API_ORIGEN}${logoUrl}" alt="Logo" style="height: 32px; margin-right: 10px; border-radius: 4px; vertical-align: middle;">`
        : "";

    const html = `
        <div class="navbar">
            <div class="marca" style="display: flex; align-items: center;">${logoHtml}${nombreInstitucion}</div>
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