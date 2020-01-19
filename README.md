# Planificación y Diseño de Sistemas Computacionales
## Grado en Ingeniería Informática 

Para ejecutar el proyecto hace falta instalar Docker y Docker Compose.

Una vez instalado y clonado el repositorio, ejecutar lo siguiente:

```
docker-compose up --build
```

Y acceder al navegador localhost:8080

Estructura del proyecto:

Democrazy: Ficheros de configuración de Django y conexión con el servidor wsgi

Docs: Diferentes documentos entregados a lo largo del transcurso de la asignatura.

Main: Código de la aplicación.  
|  
|- Models: Clases usadas por Django para la interacción con la base de datos.  
|  
|- Services: Módulos usados por las vistas.  
|  
|- Views: Vistas de Django  
|  
|- Templates: Plantillas HTML  
|  
|- Static: Imágenes, CSS y JavaScript, ficheros de prueba con elecciones, schema  
           para la validación de elecciones.

Uml-models: Ficheros .asta