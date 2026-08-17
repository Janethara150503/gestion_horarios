ESTADO GENERAL DEL PROYECTO



FASES COMPLETADAS



Fase uno, analisis del problema: cerrada.



Fase dos, usuarios y permisos: cerrada.



Fase tres, arquitectura del sistema: cerrada.



Fase cuatro, modelo de datos: cerrada.



Fase cinco, diagramas: cerrada.



Fase seis, backend: cerrada.



Fase siete, frontend: cerrada.



Fase ocho, integracion: cerrada. Se realizo integracion continua durante toda la Fase siete, con revision final de extremo a extremo de los cinco roles sin incidencias.



Fase nueve, despliegue: cerrada. Backend desplegado en Render como Web Service con Docker, base de datos PostgreSQL en Render, y frontend desplegado como Static Site en Render. Los datos de prueba se migraron desde el entorno local al entorno de produccion mediante pg\_dump. El backend acepta peticiones tanto del frontend en produccion como del entorno local, para permitir continuar el desarrollo despues del despliegue inicial.



URLS DE PRODUCCION



Backend: https://gestion-horarios-1475.onrender.com

Frontend: https://gestion-horarios-frontend.onrender.com/paginas/login.html

Repositorio: github.com/Janethara150503/gestion\_horarios



APRENDIZAJES Y DECISIONES TECNICAS DESTACADAS



El uso de restricciones EXCLUDE USING GIST en PostgreSQL como segunda capa de proteccion contra choques de horario resulto ser una decision de diseno solida.



Los servicios gratuitos de Render entran en reposo tras periodos de inactividad, lo que genera una demora de treinta a sesenta segundos en la primera peticion tras un tiempo sin uso. Esto es una limitacion conocida del plan gratuito, no un error del sistema.



Las bases de datos local y de produccion son independientes entre si. La migracion de datos entre ambas se realizo con pg\_dump en modo solo datos, seguido de una limpieza de tablas con TRUNCATE y CASCADE antes de la importacion, para evitar conflictos de llaves duplicadas.



PROYECTO COMPLETADO



Las nueve fases del proyecto quedan cerradas. El sistema esta accesible publicamente en internet, con los cinco roles funcionando de extremo a extremo contra datos reales en produccion.

