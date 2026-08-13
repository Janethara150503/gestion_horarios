FASE 5: DIAGRAMAS



DIAGRAMA DE CLASES



Se genero un diagrama UML de clases que representa las trece tablas originales del diseno y sus relaciones: roles hacia usuarios hacia docentes o estudiantes; la estructura academica con programas hacia grupos y materias, y periodos hacia grupos y horarios; la ubicacion fisica con edificios hacia aulas; y el nucleo del sistema en horarios\_clase, con sus derivados excepciones\_horario y solicitudes\_cambio, terminando en notificaciones.



DIAGRAMA DE CASOS DE USO



Se genero un diagrama que agrupa las acciones principales por rol. El Administrador gestiona usuarios y roles, y configura parametros. El Coordinador gestiona la estructura academica, programa horarios, y aprueba o rechaza solicitudes. El Docente consulta su horario propio y solicita cambios. El Estudiante consulta el horario de su grupo. El Personal administrativo busca horarios por grupo, docente o aula.



El diagrama incluye el flujo cruzado entre Docente y Coordinador en el proceso de solicitar y luego aprobar o rechazar, y el receptor comun de notificaciones entre coordinador, docente y estudiante.



VALIDACION



Ambos diagramas fueron revisados y confirmados como fiel representacion del diseno acordado en las Fases 2 y 4, antes de iniciar la construccion del backend en la Fase 6.

