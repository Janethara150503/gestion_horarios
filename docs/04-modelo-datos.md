FASE 4: MODELO DE DATOS



RESUMEN



El sistema se sostiene sobre 16 tablas en PostgreSQL. El modelo sigue el principio de horario oficial mas excepciones puntuales: la tabla horarios\_clase es la fuente de verdad permanente, y excepciones\_horario es una capa temporal que se muestra solo en la fecha que le corresponde.



ENTIDADES PRINCIPALES



roles: los cinco roles del sistema.

usuarios: cuenta de acceso, datos comunes a todos los roles.

docentes: extiende usuarios en relacion uno a uno, con especialidad.

estudiantes: extiende usuarios en relacion uno a uno, vinculado a un grupo.

periodos\_academicos: por ejemplo 2026-1, con fechas de inicio y fin.

programas: por ejemplo Ingenieria de Sistemas.

materias: vinculada a un unico programa.

grupos: vinculado a programa y periodo.

edificios: ubicaciones fisicas.

aulas: vinculada a un edificio, con capacidad, tipo y equipo.

horarios\_clase: nucleo del sistema, combina grupo, materia, docente, aula y horario.

excepciones\_horario: cambios puntuales sobre un horario, para una fecha especifica.

solicitudes\_cambio: flujo docente a coordinador para pedir cambios.

notificaciones: con distincion entre vista y leida.

configuracion\_institucion: datos institucionales, fila unica.



DECISION DE DISENO CLAVE: HERENCIA DE USUARIOS



Se opto por tablas separadas docentes y estudiantes, en relacion uno a uno con usuarios, en vez de una sola tabla con columnas opcionales. Esto evita columnas vacias sin sentido segun el rol y refleja mejor la realidad, ya que un docente y un estudiante tienen datos genuinamente distintos.



VALIDACION DE SOLAPAMIENTO DE HORARIOS EN DOBLE CAPA



La regla de que no puede haber doble asignacion de aula ni docente en horarios que se solapen se protege en dos niveles independientes. En la aplicacion, antes de guardar se consulta si existe un horario que cumpla mismo dia, mismo periodo, misma aula o mismo docente, y que los rangos de hora se crucen; si existe, se rechaza con un mensaje claro. En la base de datos, se aplica una restriccion EXCLUDE USING GIST sobre horarios\_clase, usando la extension btree\_gist para combinar igualdad de aula, periodo y dia con solapamiento de rangos de tiempo. Esta capa actua incluso si se inserta directamente en la base de datos, sin pasar por la API.



Esta doble proteccion fue probada de forma explicita: un intento de choque via API fue rechazado por la aplicacion con codigo 409, y un intento de insercion directa en PostgreSQL fue rechazado por la restriccion de base de datos.



NOTIFICACIONES: VISTA VERSUS LEIDA



Se decidio una distincion de dos estados en vez de uno solo. Vista significa que el usuario abrio el panel de notificaciones, y se marca automaticamente. Leida es una accion explicita del usuario que indica que ya la atendio. Esto permite mostrar un contador de no leidas mas util que uno de no vistas, y diferenciar entre que el usuario se entero y que ya esta resuelto para el.



TOTAL DE TABLAS: DIECISEIS



Quince del diseno original de la Fase 4, mas configuracion\_institucion, agregada durante la Fase 7 para soportar la pantalla de configuracion institucional del administrador.

