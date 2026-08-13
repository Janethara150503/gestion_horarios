FASE 2: USUARIOS Y PERMISOS



ROLES DEL SISTEMA



Administrador del sistema, Coordinador academico, Docente, Estudiante, Personal administrativo.



MATRIZ DE PERMISOS



Crear, editar y desactivar usuarios y roles: solo Administrador.

Configurar parametros generales: solo Administrador.

CRUD de periodos, programas, materias y grupos: solo Coordinador.

CRUD de aulas y sus caracteristicas: solo Coordinador.

Asignar docentes: solo Coordinador.

Programar horarios con validacion de choques: solo Coordinador.

Crear excepciones puntuales: solo Coordinador.

Ver todos los horarios de forma global: Administrador en modo lectura, Coordinador, y Personal administrativo en modo lectura.

Ver el propio horario, que corresponde al horario del grupo: Coordinador, Docente y Estudiante.

Buscar horario por grupo, docente o aula: Administrador, Coordinador y Personal administrativo.

Ver detalle de aula: todos los roles.

Solicitar cambio de horario indicando solo el motivo, sin proponer aula: solo Docente.

Aprobar o rechazar solicitudes de cambio: solo Coordinador.

Recibir notificaciones: Coordinador, Docente y Estudiante.

Consultar reportes: Administrador y Coordinador.



MECANISMO DE SOLICITUD DE CAMBIO



El docente crea una solicitud indicando unicamente el motivo, sin proponer aula. El coordinador revisa la solicitud y decide: si aprueba, asigna el mismo la nueva aula u horario, lo cual genera automaticamente una excepcion puntual en el horario oficial. Si rechaza, puede incluir un motivo opcional. En ambos casos se genera una notificacion automatica para el docente, y si aplica, para los estudiantes del grupo afectado.



DECISIONES CLAVE



Todo el grupo comparte el mismo horario en el MVP, sin electivas individuales por estudiante dentro de un mismo grupo. Esto simplifica el modelo de datos: un estudiante pertenece a un grupo, y el grupo tiene un horario unico.

