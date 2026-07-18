# Mi Proyecto del Cine

Programa para guardar películas usando Python y MongoDB.

## Requisitos
Instala estas 3 cosas:
1. Python.
2. MongoDB (debe estar prendido en el puerto 27017).
3. Pymongo (librería de Python).

---

## ¿Cómo iniciar el programa?
1. Abre tu terminal.
2. Entra a la carpeta del proyecto usando el comando `cd`.
   Ejemplo:
   > `cd Desktop/proyectocine/Evaluacion3-BD-NoEstructuradas`
3. Instala lo que falta con este comando:
   > `pip install pymongo`
4. Ejecuta el programa con este comando:
   > `python cine_crud.py`

*(Nota: La primera vez se guardan solas 8 películas de prueba).*

---

## ¿Cómo usar el Menú?
Escribe el número de la opción que quieres y presiona **ENTER**.
- Si te equivocas, dice "Formato no válido" y te deja intentar de nuevo.
- Al terminar algo, presiona `1` para repetir o `2` para volver al inicio.

---

## Opciones del Menú

### 1. Crear película
Te pide escribir datos paso a paso:
- **Título:** Escribe letras (Ejemplo: Spiderman).
- **Género:** Escribe letras (Ejemplo: Acción).
- **Duración:** Escribe solo números (Ejemplo: 120).
- **Fecha de estreno:** Escribe Año-Mes-Día (Ejemplo: 2024-12-31).
- **Precio entrada general:** Escribe solo números (Ejemplo: 5000).
- **Precio entrada niño:** Escribe solo números (Ejemplo: 3000).
- **Sala:** Escribe letras (Ejemplo: Sala 1).
- **Horario:** Escribe la hora (Ejemplo: 15:00).
- **Idioma:** Escribe letras (Ejemplo: Doblada).

### 2. Listar películas
Solo muestra la lista de todas las películas guardadas (título, género, fecha y duración).

### 3. Buscar por duración
Te pide un número de minutos.
- Ejemplo: Escribe `130`.
- Resultado: Muestra películas que duran más de 130 minutos.

### 4. Buscar por título
Te pide letras.
- Ejemplo: Escribe `pad`.
- Resultado: Encuentra "El Padrino" (no importa si usas mayúsculas o minúsculas).

### 5. Buscar por fechas
Te pide dos fechas (Año-Mes-Día).
- Ejemplo inicio: `2000-01-01`
- Ejemplo fin: `2020-12-31`
- Resultado: Muestra películas que salieron en esos años.

### 6. Buscar por sala
Te pide el nombre de una sala.
- Ejemplo: Escribe `Sala 1`.
- Resultado: Muestra qué películas se ven en esa sala.

### 7. Actualizar Género
1. Escribe el título exacto de la película.
2. Escribe el género nuevo.
- Resultado: Se guarda el nuevo género.

### 8. Actualizar Precio
1. Escribe el título exacto de la película.
2. Escribe el nuevo precio (solo números).
- Resultado: Se guarda el nuevo precio.

### 9. Eliminar película
1. Escribe el título exacto de la película.
2. El programa pregunta si estás seguro.
3. Escribe `si` y presiona ENTER para borrarla.

### 10. Reporte por Género
No tienes que escribir nada. Agrupa las películas, te dice el promedio de tiempo y las ordena de mayor a menor.

### 0. Salir
Cierra el programa.
