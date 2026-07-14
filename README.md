# Base de Datos de Cine (CRUD MongoDB)

Este proyecto es una aplicación de consola en Python que permite gestionar una base de datos NoSQL de un Cine utilizando **MongoDB**. El sistema realiza operaciones CRUD y ejecuta búsquedas avanzadas y pipelines de agregación.

## Requisitos Previos
- Python 3.x instalado.
- Servidor de MongoDB local ejecutándose en el puerto por defecto (`localhost:27017`).
- Librería `pymongo` instalada.

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Abre una terminal en la carpeta del proyecto.
3. Instala la dependencia necesaria ejecutando:
   ```bash
   pip install pymongo
   ```

## Instrucciones de Ejecución
Para iniciar el sistema, asegúrate de tener tu servidor de MongoDB encendido y luego ejecuta el siguiente comando en la terminal:
```bash
python cine_crud.py
```
*(Nota: Al iniciar el programa por primera vez con la base de datos vacía, el sistema precargará automáticamente 8 películas de prueba para poder utilizar todas las funciones inmediatamente).*

## Opciones del Menú Principal
El sistema cuenta con un menú interactivo completamente a prueba de errores. Las opciones disponibles son:

- **1. Crear película:** Permite insertar un nuevo documento completo. Solicita todos los campos obligatorios, incluyendo un campo de fecha (Fecha de estreno), un subdocumento (precios de entradas) y un arreglo de subdocumentos (salas, horarios e idiomas de las funciones).
- **2. Listar películas:** Muestra un resumen (Título, Género, Fecha y Duración) de todos los documentos en la colección.
- **3. Buscar por duración (> min):** Realiza una consulta utilizando el operador de comparación `$gt` para encontrar películas que duren más de los minutos especificados por el usuario.
- **4. Buscar por título (Regex):** Utiliza una expresión regular (`$regex` con `$options: "i"`) para encontrar películas ingresando solo una parte de su título, sin importar mayúsculas o minúsculas.
- **5. Buscar por rango de fechas:** Permite ingresar una fecha de inicio y una de fin, utilizando los operadores `$gte` y `$lte` para encontrar los estrenos en ese lapso.
- **6. Buscar por sala:** Realiza una búsqueda dentro del arreglo de subdocumentos (`funciones.sala`) para encontrar qué películas se exhiben en una sala específica.
- **7. Actualizar Género (Campo raíz):** Utiliza `$set` para modificar un campo de texto directo del documento principal buscando por su título exacto.
- **8. Actualizar Precio (Subdocumento):** Utiliza `$set` para modificar un valor numérico (`entradas.precio_general`) que se encuentra anidado dentro de un subdocumento.
- **9. Eliminar película:** Permite borrar un documento completo de la base de datos buscando por su título. Solicita confirmación antes de proceder.
- **10. Reporte por Género (Agregación):** Ejecuta un pipeline de agregación usando `$group` (para calcular el promedio de duración y la cantidad de películas por género) y `$sort` (para ordenarlos de mayor a menor duración promedio).
- **0. Salir:** Termina la ejecución del programa.
