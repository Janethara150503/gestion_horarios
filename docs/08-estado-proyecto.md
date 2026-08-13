ESTADO GENERAL DEL PROYECTO



FASES COMPLETADAS



Fase uno, analisis del problema: cerrada. Problema, reglas de negocio y alcance del MVP definidos y documentados.



Fase dos, usuarios y permisos: cerrada. Cinco roles definidos con matriz de permisos completa.



Fase tres, arquitectura del sistema: cerrada. Monolito modular con FastAPI y PostgreSQL para el backend, HTML CSS y JavaScript vanilla para el frontend.



Fase cuatro, modelo de datos: cerrada. Dieciseis tablas disenadas e implementadas, con validacion de solapamiento de horarios en doble capa.



Fase cinco, diagramas: cerrada. Diagrama de clases y diagrama de casos de uso generados y validados.



Fase seis, backend: cerrada. Siete modulos completos, todos probados con peticiones reales antes de conectar el frontend.



Fase siete, frontend: cerrada. Dieciseis pantallas completas, cubriendo los cinco roles del sistema, todas probadas con datos reales contra el backend.



FASES PENDIENTES



Fase ocho, integracion: se realizo integracion continua durante toda la Fase siete, ya que cada pantalla del frontend se probo directamente contra el backend real conforme se construia. Queda pendiente una revision general de extremo a extremo, recorriendo el flujo completo de cada rol una vez mas para detectar cualquier detalle suelto antes del despliegue.



Fase nueve, despliegue: pendiente por completo. Incluye dockerizar la aplicacion, desplegar en Render, y probar el acceso real desde internet.



APRENDIZAJES Y DECISIONES TECNICAS DESTACADAS



El uso de restricciones EXCLUDE USING GIST en PostgreSQL como segunda capa de proteccion contra choques de horario, complementando la validacion en la aplicacion, resulto ser una decision de diseno solida y fue probada exitosamente de forma independiente.



La decision de construir el frontend sin framework permitio entender a fondo el manejo manual de estado, autenticacion y comunicacion con la API, aunque incremento el numero de archivos a mantener manualmente.



Durante la integracion surgieron necesidades no anticipadas en el diseno original del backend, como el endpoint de configuracion institucional y la inclusion de datos anidados completos en las respuestas de horarios, lo cual confirma el valor de probar cada pieza con datos reales en vez de solo disenar sobre el papel.



PROXIMOS PASOS INMEDIATOS



Revisar de extremo a extremo el flujo completo de cada uno de los cinco roles. Preparar el archivo Dockerfile y docker-compose para el backend. Configurar variables de entorno para produccion. Desplegar en Render y validar acceso publico.

