FASE 3: ARQUITECTURA DEL SISTEMA



ESTILO GENERAL



Monolito modular: una sola aplicacion backend, organizada internamente en modulos independientes, con un solo despliegue y una sola base de datos. Se descarto microservicios por la complejidad de infraestructura que no se justifica al tamano de este proyecto, y porque la reutilizacion para distintas instituciones se resuelve con el modelo de una instalacion por institucion, no con separacion de servicios.



MODULOS DEL BACKEND



Usuarios: gestion de usuarios, roles, docentes y estudiantes.

Academico: periodos, programas, materias, grupos.

Espacios: edificios y aulas.

Horarios: asignacion de horarios y excepciones puntuales.

Solicitudes: flujo de solicitud de cambio entre docente y coordinador.

Notificaciones: notificaciones in app via polling.

Configuracion: parametros institucionales.

Core: seguridad JWT, permisos por rol, manejo de errores.



Cada modulo sigue el patron de capas: models para las tablas, schemas para la validacion de entrada y salida, routes como capa delgada de endpoints HTTP, y services con la logica de negocio real, testeable de forma aislada.



NOTIFICACIONES EN TIEMPO REAL



Se implementa mediante polling: el frontend consulta periodicamente un endpoint de notificaciones no leidas. Se descarto WebSockets para el MVP por la complejidad de infraestructura adicional que no se justifica a esta escala, dejandolo como posible mejora futura.



AUTENTICACION Y PERMISOS



JWT para autenticacion, sin estado en el servidor. La verificacion de rol se hace mediante dependencias de FastAPI, aplicando directamente la matriz de permisos de la Fase 2 en cada endpoint protegido.



PWA



manifest.json y Service Worker para cacheo basico de assets. Sin funcionalidad offline completa en el MVP. HTTPS provisto automaticamente en el entorno de despliegue.



STACK TECNOLOGICO



Backend: Python con FastAPI.

Base de datos: PostgreSQL.

ORM: SQLAlchemy, con migraciones via Alembic.

Frontend: HTML, CSS y JavaScript vanilla, sin framework, con arquitectura multi pagina.

Control de versiones: Git y GitHub.

Despliegue planificado: Docker y Render.

