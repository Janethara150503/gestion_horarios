FASE 6: BACKEND



RESUMEN



El backend se construyo con FastAPI y PostgreSQL, siguiendo la arquitectura de monolito modular definida en la Fase 3. Se completaron siete modulos: usuarios, academico, espacios, horarios, solicitudes, notificaciones y configuracion, cada uno con sus capas de modelos, esquemas, servicios y rutas.



MODULO USUARIOS



Incluye registro y login con JWT, hash de contrasenas con bcrypt via passlib, un endpoint protegido para consultar el perfil propio, y las tablas de herencia docentes y estudiantes. Se agrego ademas gestion completa de usuarios para el administrador: listar todos, cambiar rol, y activar o desactivar cuentas.



MODULO ACADEMICO



CRUD completo de periodos academicos, programas, materias y grupos, con la creacion protegida exclusivamente para el rol coordinador, y la lectura abierta a cualquier usuario autenticado.



MODULO ESPACIOS



CRUD de edificios y aulas, mismo patron de proteccion que el modulo academico.



MODULO HORARIOS



El modulo mas critico del sistema. Implementa el modelo HorarioClase con validacion de solapamiento en doble capa: en la logica de la aplicacion, y como restriccion EXCLUDE USING GIST en PostgreSQL. Ambas capas fueron probadas de forma independiente con exito.



MODULO SOLICITUDES



Implementa el flujo completo de solicitud de cambio: el docente crea la solicitud, el coordinador la aprueba o rechaza, y al aprobarla se genera automaticamente un registro en excepciones\_horario, enlazado a la solicitud original.



MODULO NOTIFICACIONES



Notificaciones con distincion vista y leida, generadas automaticamente cuando se resuelve una solicitud de cambio, y consultables por el usuario via polling desde el frontend.



MODULO CONFIGURACION



Agregado durante la integracion con el frontend en la Fase 7, para soportar la pantalla de configuracion institucional: nombre, direccion, contacto, dias de operacion, duracion de sesion, y logo institucional subido como archivo, servido como archivo estatico por el propio backend.



SEGURIDAD Y AUTORIZACION



Autenticacion JWT sin estado en el servidor. Una dependencia central requiere\_rol verifica el rol del usuario contra la matriz de permisos de la Fase 2 en cada endpoint protegido. CORS habilitado para permitir que el frontend, servido como archivos locales, pueda comunicarse con la API.



MIGRACIONES



Todas las tablas se gestionan mediante Alembic, con una migracion por cada cambio de esquema, incluyendo la migracion especial que agrega la restriccion EXCLUDE USING GIST mediante SQL crudo, ya que Alembic no genera este tipo de restriccion automaticamente.



PRUEBAS REALIZADAS



Cada endpoint del backend fue probado con peticiones reales via curl antes de conectarse al frontend, incluyendo casos de exito, casos de rechazo por rol incorrecto, y el caso especifico de choque de horario en ambas capas de proteccion.

