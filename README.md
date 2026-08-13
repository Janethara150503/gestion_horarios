SISTEMA DE GESTION DE HORARIOS Y ESPACIOS ACADEMICOS



DESCRIPCION



Sistema web tipo PWA para la gestion de horarios y espacios en instituciones educativas que operan fines de semana. Permite a coordinadores programar horarios con validacion automatica de choques, a docentes y estudiantes consultar sus horarios y recibir notificaciones, a docentes solicitar cambios de horario, y a personal administrativo buscar informacion de horarios de forma rapida.



STACK TECNOLOGICO



Backend: Python, FastAPI, PostgreSQL, SQLAlchemy, Alembic.

Frontend: HTML, CSS y JavaScript vanilla, arquitectura multi pagina, PWA.

Autenticacion: JWT.

Control de versiones: Git y GitHub.

Despliegue planificado: Docker y Render.



ROLES DEL SISTEMA



Administrador, Coordinador academico, Docente, Estudiante, Personal administrativo. La matriz de permisos completa esta documentada en docs/02-usuarios-permisos.md.



REGLA DE NEGOCIO CRITICA



No puede existir doble asignacion de aula ni de docente en horarios que se solapen. Esta regla se protege en dos capas independientes: validacion en la logica de la aplicacion, y una restriccion EXCLUDE USING GIST en PostgreSQL que actua incluso si se inserta directamente en la base de datos. Detalle completo en docs/04-modelo-datos.md.



ESTRUCTURA DEL REPOSITORIO



La carpeta app contiene el backend, organizado por modulos: usuarios, academico, espacios, horarios, solicitudes, notificaciones y configuracion.

La carpeta frontend contiene las dieciseis pantallas del sistema, organizadas por rol.

La carpeta alembic contiene el historial de migraciones de base de datos.

La carpeta docs contiene la documentacion completa del proyecto, fase por fase.



DOCUMENTACION POR FASE



docs/01-analisis-problema.md: problema, reglas de negocio y alcance del MVP.

docs/02-usuarios-permisos.md: roles y matriz de permisos completa.

docs/03-arquitectura.md: decisiones de arquitectura y stack tecnologico.

docs/04-modelo-datos.md: modelo de datos y decisiones de diseno de base de datos.

docs/05-diagramas.md: diagramas de clases y casos de uso.

docs/06-backend.md: modulos del backend y decisiones tecnicas.

docs/07-frontend.md: inventario de pantallas y decisiones del frontend.

docs/08-estado-proyecto.md: estado general del proyecto y proximos pasos.



ESTADO ACTUAL



Fases uno a siete completadas: analisis, permisos, arquitectura, modelo de datos, diagramas, backend y frontend. Pendientes: integracion final de extremo a extremo y despliegue en la nube.



COMO EJECUTAR EL PROYECTO LOCALMENTE



Backend: crear entorno virtual, instalar dependencias con pip install desde requirements.txt, configurar el archivo .env con la cadena de conexion a PostgreSQL, aplicar migraciones con alembic upgrade head, y levantar el servidor con uvicorn app.main:app --reload.



Frontend: abrir el archivo frontend/paginas/login.html directamente en el navegador, con el backend corriendo en paralelo en localhost puerto 8000.

