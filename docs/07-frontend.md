FASE 7: FRONTEND



RESUMEN



El frontend se construyo con HTML, CSS y JavaScript vanilla, sin framework, en arquitectura multi pagina, tal como se decidio en la Fase 7 para reforzar fundamentos antes de introducir herramientas adicionales. El sistema completo abarca dieciseis pantallas, todas probadas con datos reales contra el backend.



ARQUITECTURA DEL FRONTEND



api.js centraliza todas las llamadas al backend, agregando automaticamente el token JWT a cada peticion y manejando errores de forma uniforme, incluyendo la extraccion del mensaje de error especifico del backend para mostrarlo al usuario.



auth.js maneja el flujo de autenticacion: login, logout, y proteccion de paginas segun el rol permitido, con limpieza automatica de sesion en cada carga de la pantalla de login para evitar arrastre de datos de un usuario anterior.



layout.js genera dinamicamente la barra de navegacion y el menu lateral segun el rol del usuario autenticado, e incluye el nombre y logo de la institucion cargados desde la configuracion del backend, ademas de un contador de solicitudes pendientes visible para el rol coordinador en forma de insignia numerica sobre el menu.



INVENTARIO DE PANTALLAS



Compartidas para todos los roles: inicio de sesion, notificaciones con distincion vista y leida, y perfil propio de solo lectura.



Rol estudiante: consulta de su horario, filtrado por el grupo al que pertenece.



Rol docente: consulta de su horario propio, formulario para solicitar cambio de horario indicando solo el motivo, y listado del estado de sus solicitudes enviadas con codigo de color segun el estado.



Rol personal administrativo: buscador de horarios con filtro por grupo, docente o aula, y contador de resultados visible.



Rol coordinador: gestion academica con pestanas para periodos, programas, materias y grupos; gestion de espacios con pestanas para edificios y aulas; gestion de horarios con formulario de creacion y manejo claro del error de choque devuelto por el backend; gestion combinada de registro de docentes y estudiantes; y bandeja de solicitudes pendientes con formulario de aprobacion o rechazo por cada solicitud.



Rol administrador: gestion de usuarios con cambio de rol y activacion o desactivacion de cuentas; y configuracion institucional con nombre, direccion, contacto, dias de operacion, duracion de sesion, y logo institucional mediante subida de archivo.



DECISIONES TECNICAS RELEVANTES



Se agrego CORS al backend para permitir que el frontend, abierto como archivos locales bajo el protocolo file, pudiera comunicarse con la API en localhost.



Se corrigio un patron de rutas absolutas que rompian bajo el protocolo file al redirigir al login, reemplazandolas por rutas relativas.



Se mejoraron endpoints del backend durante la integracion para incluir datos anidados completos, como nombre de materia, docente y aula, en vez de solo identificadores numericos, evitando así construir esa logica repetidamente en el frontend.



PRUEBAS REALIZADAS



Cada pantalla fue probada con usuarios reales de cada rol, incluyendo casos limite como el registro de un usuario y su vinculo automatico a un registro de docente o estudiante, y la generacion automatica de una excepcion de horario al aprobar una solicitud de cambio.

