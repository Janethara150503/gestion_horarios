async function iniciarSesion(correo, password) {
    localStorage.removeItem("usuario");
    const respuesta = await api.login(correo, password);
    guardarToken(respuesta.access_token);
    return respuesta;
}

function cerrarSesion() {
    eliminarToken();
    localStorage.removeItem("usuario");
    window.location.href = "login.html";
}

async function obtenerUsuarioActual() {
    const usuarioGuardado = localStorage.getItem("usuario");
    if (usuarioGuardado) {
        return JSON.parse(usuarioGuardado);
    }
    const usuario = await api.obtenerMiPerfil();
    localStorage.setItem("usuario", JSON.stringify(usuario));
    return usuario;
}

async function protegerPagina(rolesPermitidos = null) {
    const token = obtenerToken();
    if (!token) {
        window.location.href = "login.html";
        return null;
    }

    try {
        const usuario = await obtenerUsuarioActual();

        if (rolesPermitidos && !rolesPermitidos.includes(usuario.rol.nombre)) {
            alert("No tienes permiso para ver esta pagina");
            window.location.href = "login.html";
            return null;
        }

        return usuario;
    } catch (error) {
        window.location.href = "login.html";
        return null;
    }
}