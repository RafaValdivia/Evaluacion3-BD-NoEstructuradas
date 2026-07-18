# Mi Proyecto del Cine

¡Hola! Este es mi programa para guardar películas en una computadora. Usamos una base de datos de verdad llamada **MongoDB**.

## Lo que necesitas tener instalado
Para que mi programa funcione, tienes que pedirle a alguien que instale estas 3 cosas en tu compu:
1. **Python** (el programa que lee el código).
2. **MongoDB** (donde se guardan los datos, debe estar prendido en `localhost:27017`).
3. **Pymongo** (esto sirve para que Python hable con MongoDB).

---

## ¿Cómo prender el programa?
1. Abre tu pantallita negra de comandos (la terminal).
2. Entra a la carpeta del proyecto.
3. Escribe esto para instalar lo que falta:
   > `pip install pymongo`
4. ¡Y para jugar con el programa escribe esto!
   > `python cine_crud.py`

*(Dato curioso: Si es la primera vez que lo abres y no tienes nada guardado, el programa va a meter 8 películas solitas para que tengas con qué probar).*

---

## ¿Cómo funciona el Menú?
Cuando el programa empieza, te sale una lista con opciones (del 0 al 10).
- Solo tienes que **escribir el número** que quieras y apretar **ENTER**.
- Si te equivocas o escribes letras cuando eran números, el programa te avisa diciendo *"Formato no válido"* y te deja intentar de nuevo. ¡No se rompe!
- Cuando terminas de hacer algo, te pregunta si quieres hacerlo otra vez (apretando el número `1`) o si quieres volver al inicio (apretando el número `2`).

---

## Esto hace cada botón del Menú

### 1. Crear película
Sirve para inventar y guardar una película nueva. Te va a ir pidiendo cosas una por una:
- **Título:** Cómo se llama (ejemplo: Spiderman).
- **Género:** De qué trata (ejemplo: Acción).
- **Duración:** Cuántos minutos dura, ¡solo pon números! (ejemplo: 120).
- **Fecha de estreno:** Tienes que escribir el año, mes y día separados con rayitas (ejemplo: 2024-12-31).
- **Precio entrada general:** Cuánto cuesta para los grandes (solo números).
- **Precio entrada niño:** Cuánto cuesta para los niños (solo números).
- **Sala:** Dónde se va a ver (ejemplo: Sala 1).
- **Horario:** A qué hora empieza (ejemplo: 15:00).
- **Idioma:** En qué idioma está.
*Magia:* Tú no pones cuántas entradas se vendieron, ¡el programa le pone un 0 solito! Y guarda todo ordenado por dentro.

### 2. Listar películas
Te muestra una lista rápida con todas las películas que tenemos guardadas. Solo ves el título, el género, cuándo salió y cuánto dura.

### 3. Buscar por duración
Si tienes ganas de ver una peli larga, el programa te pide un número. Si pones `130`, te buscará y mostrará solo las películas que duren más de 130 minutos.

### 4. Buscar por título
Es como el buscador de internet. Si pones un pedacito de la palabra como `pad`, el programa busca y te encuentra la película "El Padrino". No importa si escribes con letras grandes o chicas, ¡lo encuentra igual!

### 5. Buscar por rango de fechas
Si le das dos fechas, el programa busca en su calendario y te enseña todas las películas que nacieron en ese tiempo. Te pide primero la fecha de inicio y luego la fecha de fin (siempre usando el formato Año-Mes-Día).

### 6. Buscar por sala
Escribes el nombre exacto de una sala (como `Sala 1`) y el programa revisa y te dice todas las películas que se van a pasar ahí adentro.

### 7. Actualizar Género
Sirve para corregir si te equivocaste de género.
1. El programa te pide escribir el nombre **exacto** de la peli.
2. Luego te pide escribir el género nuevo.
¡Aprietas ENTER y listo, se cambia para siempre en la base de datos!

### 8. Actualizar Precio
Sirve para cambiar cuánto cuesta el boleto general.
1. Escribes el título exacto de la película.
2. Escribes el número del precio nuevo.
El programa se mete adentro de los datos ocultos del precio y lo cambia.

### 9. Eliminar película
¡Sirve para borrar películas! 
- Primero pones el nombre exacto.
- Luego, el programa te va a preguntar `¿Estás seguro?`. Tienes que escribir la palabra `si` para que se borre. ¡Es un seguro para no borrar cosas por accidente!

### 10. Reporte por Género
Este lo hace todo solo. Junta las películas parecidas y te dice, por ejemplo, cuántas películas de Acción hay y cuál es el promedio de tiempo de lo que duran. Y hace una lista ordenada de la más larga a la más corta.

### 0. Salir
Apaga el programa de forma segura y vuelves a ver las letras normales de tu computadora.
