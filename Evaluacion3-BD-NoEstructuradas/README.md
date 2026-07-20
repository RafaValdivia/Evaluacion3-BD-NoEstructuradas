# Sistema de Gestión de Cine (ProyectoCine)

Sistema de gestión de cartelera y películas implementado en Python y MongoDB.

## Requisitos del Sistema
- Python 3.x
- MongoDB (ejecutándose en `localhost:27017`)
- Librería `pymongo`

## Instrucciones de Instalación
1. Clonar o acceder al directorio del proyecto:
   `cd Desktop/proyectocine/Evaluacion3-BD-NoEstructuradas`
2. Instalar las dependencias necesarias:
   `pip install pymongo`
3. Ejecutar la aplicación:
   `python ProyectoCine.py`

*(Nota: En la primera ejecución, la base de datos se inicializará automáticamente con 8 registros de prueba).*

## Uso de la Aplicación
El sistema funciona a través de un menú interactivo por consola. 

### Opciones Disponibles:

1. **Crear película**: Permite ingresar un nuevo registro a la base de datos. Requiere completar los campos de título, género, duración, fecha de estreno, precios (general/niño) e información de la función (sala, horario e idioma).
2. **Listar películas**: Muestra todos los registros almacenados en la colección, incluyendo título, género, fecha de estreno y duración.
3. **Buscar por duración**: Filtra y muestra las películas cuya duración en minutos sea mayor al valor ingresado ($gt).
4. **Buscar por título**: Realiza una búsqueda mediante expresiones regulares (Regex) para encontrar coincidencias parciales en los títulos.
5. **Buscar por fechas**: Muestra las películas estrenadas dentro de un rango de fechas especificado.
6. **Buscar por sala**: Busca coincidencias dentro de los subdocumentos de funciones para mostrar qué películas se proyectan en una sala específica.
7. **Actualizar Género**: Modifica el campo raíz 'género' de un documento existente en base a su título exacto.
8. **Actualizar Precio**: Modifica un valor anidado (precio general) dentro del subdocumento 'entradas'.
9. **Eliminar película**: Elimina un documento completo de la colección de manera permanente.
10. **Reporte por Género**: Genera un reporte utilizando un pipeline de agregación de MongoDB, mostrando el promedio de duración agrupado por género y ordenando los resultados.
0. **Salir**: Finaliza la ejecución del programa.
