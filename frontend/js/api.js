const API_BASE_URL = "http://127.0.0.1:8000";

function obtenerToken() {
    return localStorage.getItem("token");
}

function guardarToken(token) {
    localStorage.setItem("token", token);
}

function eliminarToken() {
    localStorage.removeItem("token");
}

async function apiFetch(endpoint, opciones = {}) {
    const token = obtenerToken();

    const headers = {
        "Content-Type": "application/json",
        ...opciones.headers,
    };

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const respuesta = await fetch(`${API_BASE_URL}${endpoint}`, {
        ...opciones,
        headers,
    });

    if (respuesta.status === 401) {
        eliminarToken();
        window.location.href = "login.html";
        throw new Error("Sesion expirada, por favor inicia sesion de nuevo");
    }

    let datos = null;
    const contentType = respuesta.headers.get("content-type");
    if (contentType && contentType.includes("application/json")) {
        datos = await respuesta.json();
    }

    if (!respuesta.ok) {
        const mensaje = datos && datos.detail ? datos.detail : "Ocurrio un error inesperado";
        throw new Error(mensaje);
    }

    return datos;
}

const api = {
    login: (correo, password) =>
        apiFetch("/usuarios/login", {
            method: "POST",
            body: JSON.stringify({ correo, password }),
        }),

    obtenerMiPerfil: () => apiFetch("/usuarios/yo"),
    obtenerMiEstudiante: () => apiFetch("/usuarios/estudiantes/yo"),
    listarDocentes: () => apiFetch("/usuarios/docentes"),
    listarEstudiantes: () => apiFetch("/usuarios/estudiantes"),
    listarUsuarios: () => apiFetch("/usuarios/"),
    cambiarRolUsuario: (id, rolId) =>
        apiFetch(`/usuarios/${id}/rol`, { method: "PUT", body: JSON.stringify({ rol_id: rolId }) }),
    cambiarEstadoUsuario: (id, activo) =>
        apiFetch(`/usuarios/${id}/estado`, { method: "PUT", body: JSON.stringify({ activo: activo }) }),
    crearDocente: (datos) =>
        apiFetch("/usuarios/docentes", { method: "POST", body: JSON.stringify(datos) }),
    crearEstudiante: (datos) =>
        apiFetch("/usuarios/estudiantes", { method: "POST", body: JSON.stringify(datos) }),

    registrarUsuario: (datos) =>
        apiFetch("/usuarios/registro", {
            method: "POST",
            body: JSON.stringify(datos),
        }),

    listarPeriodos: () => apiFetch("/academico/periodos"),
    crearPeriodo: (datos) =>
        apiFetch("/academico/periodos", { method: "POST", body: JSON.stringify(datos) }),

    listarProgramas: () => apiFetch("/academico/programas"),
    crearPrograma: (datos) =>
        apiFetch("/academico/programas", { method: "POST", body: JSON.stringify(datos) }),

    listarMaterias: () => apiFetch("/academico/materias"),
    crearMateria: (datos) =>
        apiFetch("/academico/materias", { method: "POST", body: JSON.stringify(datos) }),

    listarGrupos: () => apiFetch("/academico/grupos"),
    crearGrupo: (datos) =>
        apiFetch("/academico/grupos", { method: "POST", body: JSON.stringify(datos) }),

    listarEdificios: () => apiFetch("/espacios/edificios"),
    crearEdificio: (datos) =>
        apiFetch("/espacios/edificios", { method: "POST", body: JSON.stringify(datos) }),

    listarAulas: () => apiFetch("/espacios/aulas"),
    crearAula: (datos) =>
        apiFetch("/espacios/aulas", { method: "POST", body: JSON.stringify(datos) }),

    listarHorarios: () => apiFetch("/horarios/"),
    crearHorario: (datos) =>
        apiFetch("/horarios/", { method: "POST", body: JSON.stringify(datos) }),

    crearSolicitud: (datos) =>
        apiFetch("/solicitudes/", { method: "POST", body: JSON.stringify(datos) }),
    listarMisSolicitudes: () => apiFetch("/solicitudes/mias"),
    listarSolicitudesPendientes: () => apiFetch("/solicitudes/pendientes"),
    resolverSolicitud: (id, datos) =>
        apiFetch(`/solicitudes/${id}/resolver`, { method: "PUT", body: JSON.stringify(datos) }),

    listarNotificaciones: () => apiFetch("/notificaciones/"),
    listarNotificacionesNoLeidas: () => apiFetch("/notificaciones/no-leidas"),
    marcarNotificacionVista: (id) =>
        apiFetch(`/notificaciones/${id}/vista`, { method: "PUT" }),
    marcarNotificacionLeida: (id) =>
        apiFetch(`/notificaciones/${id}/leida`, { method: "PUT" }),
};