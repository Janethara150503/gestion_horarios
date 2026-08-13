FASE 1: ANALISIS DEL PROBLEMA



PROBLEMA IDENTIFICADO



Instituciones educativas que operan fines de semana (sabado y domingo) gestionan horarios y espacios con herramientas informales (Excel, WhatsApp, carteleras fisicas), lo que genera: choques de horario y aula descubiertos tarde, informacion desactualizada entre coordinacion, docentes y estudiantes, falta de una fuente unica de verdad, y dificultad para orientar a estudiantes y personal dentro de la institucion.



REGLAS DE NEGOCIO



Uno. Horarios con rangos de hora libres, validados por solapamiento de tiempo.

Dos. Horario oficial mas excepciones puntuales, siendo el oficial la fuente de verdad permanente.

Tres. Actualizaciones via polling mas notificaciones in app.

Cuatro. Una institucion por instalacion, con parametros configurables.

Cinco. No puede haber doble asignacion de aula ni docente en horarios que se solapen.

Seis. Cada clase es grupo mas materia mas docente mas aula mas horario.

Siete. Las aulas tienen caracteristicas usables como criterio de asignacion.

Ocho. Los dias de operacion son configurables, siendo sabado y domingo el caso de uso actual.



ALCANCE DEL MVP



Incluido: roles y autenticacion JWT, CRUD academico completo, asignacion de horarios con validacion de choques en doble capa, consulta de horario por rol, notificaciones in app, excepciones puntuales, solicitud de cambio, gestion de usuarios y configuracion institucional.



Fuera del MVP: multi tenancy, WebSockets, push notifications nativas, reportes avanzados.

