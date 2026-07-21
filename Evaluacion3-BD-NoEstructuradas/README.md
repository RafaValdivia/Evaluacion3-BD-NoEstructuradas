# Sistema de Gestión de Cine (ProyectoCine)

Sistema de gestión de cartelera y películas implementado en Python y MongoDB.

## Requisitos del Sistema
- Python 3.x
- MongoDB (ejecutándose en `localhost:27017`) o la librería `mongomock` (emulación en memoria si MongoDB no está activo).
- Librerías Python: `pymongo`, `mongomock`

## Instrucciones de Instalación
1. Clonar o acceder al directorio del proyecto:
   `cd Evaluacion3-BD-NoEstructuradas`
2. Instalar las dependencias necesarias:
   `pip install pymongo mongomock`
3. Ejecutar la aplicación:
   `python ProyectoCine.py`

*(Nota: En la primera ejecución, la base de datos se inicializará automáticamente con 8 registros de prueba).*

## Uso de la Aplicación
El sistema funciona a través de un menú interactivo por consola. 

### Opciones Disponibles:

1. **Crear película**: Permite ingresar un nuevo registro a la base de datos. Requiere completar los campos de título, género, duración, fecha de estreno, precios (general/niño) e información de la función (sala, horario e idioma). Usa `insertOne`.
2. **Listar películas**: Muestra todos los registros almacenados en la colección con proyección de campos relevantes.
3. **Buscar por duración**: Filtra películas permitiendo elegir entre distintos operadores de comparación (`$gt`, `$lt`, `$gte`, `$lte`, `$ne`).
4. **Buscar por título**: Realiza una búsqueda mediante expresiones regulares (`$regex`) insensibles a mayúsculas/minúsculas para encontrar coincidencias parciales.
5. **Buscar por fechas**: Muestra las películas estrenadas dentro de un rango de fechas especificado (`$gte` y `$lte`).
6. **Buscar por sala**: Busca coincidencias dentro del array de subdocumentos `funciones` para mostrar las películas proyectadas en una sala específica.
7. **Actualizar Género**: Modifica el campo raíz 'género' de un documento mediante `$set`, mostrando el estado antes y después.
8. **Actualizar Precio (Subdocumento)**: Permite actualizar el precio general en el subdocumento `entradas` (`$set`) o agregar una nueva función al array `funciones` (`$push`), mostrando el estado antes y después.
9. **Eliminar película**: Muestra el documento encontrado, solicita confirmación explícita (acepta *sí, si, s*) y elimina el documento mediante `deleteOne`.
10. **Reporte por Género**: Genera un reporte utilizando un pipeline de agregación (`$group` + `$sort` + `$project`), calculando el promedio de duración por género.
0. **Salir**: Finaliza la ejecución del programa.

