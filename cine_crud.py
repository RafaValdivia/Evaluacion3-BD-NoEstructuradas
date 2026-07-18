from pymongo import MongoClient
from datetime import datetime

# Conexión a MongoDB local
client = MongoClient('mongodb://localhost:27017/')
db = client['cine_db']
collection = db['peliculas']

# Aquí se agregan los 8 documentos de películas para no empezar vacío y poder probar.
def inicializar_datos():
    collection.drop()
    peliculas_data = [
        {
            "titulo": "Inception",
            "genero": "Ciencia Ficción",
            "duracion_minutos": 148,
            "fecha_estreno": datetime(2010, 7, 16),
            "entradas": {"precio_general": 5000, "precio_nino": 3500, "vendidas": 120},
            "funciones": [{"sala": "Sala 1", "horario": "18:00", "idioma": "Subtitulada"}, {"sala": "Sala 3", "horario": "21:30", "idioma": "Doblada"}]
        },
        {
            "titulo": "The Matrix",
            "genero": "Ciencia Ficción",
            "duracion_minutos": 136,
            "fecha_estreno": datetime(1999, 3, 31),
            "entradas": {"precio_general": 4500, "precio_nino": 3000, "vendidas": 200},
            "funciones": [{"sala": "Sala 2", "horario": "19:00", "idioma": "Subtitulada"}]
        },
        {
            "titulo": "Toy Story",
            "genero": "Animación",
            "duracion_minutos": 81,
            "fecha_estreno": datetime(1995, 11, 22),
            "entradas": {"precio_general": 4000, "precio_nino": 2500, "vendidas": 350},
            "funciones": [{"sala": "Sala 4", "horario": "15:00", "idioma": "Doblada"}, {"sala": "Sala 4", "horario": "17:00", "idioma": "Doblada"}]
        },
        {
            "titulo": "Avengers: Endgame",
            "genero": "Acción",
            "duracion_minutos": 181,
            "fecha_estreno": datetime(2019, 4, 26),
            "entradas": {"precio_general": 6000, "precio_nino": 4500, "vendidas": 500},
            "funciones": [{"sala": "Sala 1", "horario": "14:00", "idioma": "Doblada"}, {"sala": "Sala 2", "horario": "20:00", "idioma": "Subtitulada"}]
        },
        {
            "titulo": "El Padrino",
            "genero": "Drama",
            "duracion_minutos": 175,
            "fecha_estreno": datetime(1972, 3, 24),
            "entradas": {"precio_general": 5500, "precio_nino": 0, "vendidas": 80},
            "funciones": [{"sala": "Sala 5", "horario": "22:00", "idioma": "Subtitulada"}]
        },
        {
            "titulo": "Jurassic Park",
            "genero": "Aventura",
            "duracion_minutos": 127,
            "fecha_estreno": datetime(1993, 6, 11),
            "entradas": {"precio_general": 4800, "precio_nino": 3200, "vendidas": 150},
            "funciones": [{"sala": "Sala 3", "horario": "16:00", "idioma": "Doblada"}, {"sala": "Sala 3", "horario": "18:30", "idioma": "Subtitulada"}]
        },
        {
            "titulo": "Interstellar",
            "genero": "Ciencia Ficción",
            "duracion_minutos": 169,
            "fecha_estreno": datetime(2014, 11, 7),
            "entradas": {"precio_general": 5200, "precio_nino": 3800, "vendidas": 110},
            "funciones": [{"sala": "Sala 1", "horario": "21:00", "idioma": "Subtitulada"}]
        },
        {
            "titulo": "Shrek",
            "genero": "Animación",
            "duracion_minutos": 90,
            "fecha_estreno": datetime(2001, 5, 18),
            "entradas": {"precio_general": 4200, "precio_nino": 2800, "vendidas": 300},
            "funciones": [{"sala": "Sala 2", "horario": "13:00", "idioma": "Doblada"}, {"sala": "Sala 4", "horario": "15:30", "idioma": "Doblada"}]
        }
    ]
    # Se usa insert_many cumpliendo con el criterio "Create" de la rúbrica
    collection.insert_many(peliculas_data)

# Aquí se pregunta si quieres hacer lo mismo otra vez o salir al menú principal.
def preguntar_continuar(accion_repetir):
    # Función auxiliar para preguntar con menú numérico si desea repetir
    
    # El 'while True' hace que el código repita la pregunta por siempre hasta que respondas bien.
    while True:
        print(f"\n1. {accion_repetir}")
        print("2. Volver al menú principal")
        opcion = input("Selecciona la opción: ").strip()
        
        # El 'if' pregunta si escribiste "1".
        if opcion == "1":
            return True
        # El 'elif' pregunta si escribiste "2", pero solo si falló el 'if' de arriba.
        elif opcion == "2":
            return False
        # El 'else' atrapa cualquier otra cosa equivocada que hayas escrito (letras, otros números).
        else:
            print("Opción inválida. Intenta nuevamente.")

# --- OPERACIONES CRUD ---

# Aquí se crea y guarda una película nueva con los datos que tú escribes.
def crear_pelicula():
    while True:
        print("\n--- 1. CREAR NUEVA PELÍCULA ---")
        
        # El 'try' intenta ejecutar el código sin problemas.
        # Si algo falla, pasará automáticamente al 'except' más abajo.
        try:
            titulo = input("Título (ej. 'Spiderman', no debe estar vacío): ").strip()
            # El 'if not' revisa si dejaste el texto completamente vacío.
            if not titulo:
                print("Formato no válido, respete las indicaciones.")
                continue

            genero = input("Género (ej. 'Acción', no debe estar vacío): ").strip()
            if not genero:
                print("Formato no válido, respete las indicaciones.")
                continue

            duracion = int(input("Duración (solo ingresa los minutos, ej. 120): "))
            fecha_str = input("Fecha de estreno (YYYY-MM-DD, ej. 2024-12-31): ")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            
            precio_gen = int(input("Precio entrada general (solo números, ej. 5000): "))
            precio_nino = int(input("Precio entrada niño (solo números, ej. 3000): "))
            
            sala = input("Sala (ej. 'Sala 1', no debe estar vacío): ").strip()
            horario = input("Horario (ej. '15:00', no debe estar vacío): ").strip()
            idioma = input("Idioma (ej. 'Doblada', no debe estar vacío): ").strip()
            
            if not sala or not horario or not idioma:
                print("Formato no válido, respete las indicaciones.")
                continue

            nueva_pelicula = {
                "titulo": titulo,
                "genero": genero,
                "duracion_minutos": duracion,
                "fecha_estreno": fecha,
                "entradas": {
                    "precio_general": precio_gen,
                    "precio_nino": precio_nino,
                    "vendidas": 0
                },
                "funciones": [
                    {"sala": sala, "horario": horario, "idioma": idioma}
                ]
            }
            
            # Se usa insert_one cumpliendo con el criterio "Create" de la rúbrica
            collection.insert_one(nueva_pelicula)
            print(f"¡Película '{titulo}' insertada exitosamente!")
        except ValueError:
            # Si alguien escribió letras en donde iban números (como el precio), cae aquí y no se rompe.
            print("Formato no válido, respete las indicaciones.")
        
        # El 'if not' revisa si elegiste NO continuar (opción 2) para romper el ciclo usando 'break'.
        if not preguntar_continuar("Crear otra película"):
            break

# Aquí se busca la lista de todas las películas guardadas y se muestran en pantalla.
def listar_peliculas():
    while True:
        print("\n--- 2. LISTAR PELÍCULAS ---")
        # Se aplica PROYECCIÓN limitando los campos, cumpliendo con la rúbrica
        proyeccion = {"_id": 0, "titulo": 1, "genero": 1, "fecha_estreno": 1, "duracion_minutos": 1}
        peliculas = collection.find({}, proyeccion)
        
        # El 'for' significa "por cada película que encontraste, haz lo siguiente:"
        for p in peliculas:
            fecha_str = p['fecha_estreno'].strftime('%Y-%m-%d')
            print(f"- {p['titulo']} | Género: {p['genero']} | Estreno: {fecha_str} | Duración: {p['duracion_minutos']} min")
        
        if not preguntar_continuar("Listar nuevamente"):
            break

# Aquí se buscan las películas que duren más tiempo del que tú le pidas.
def buscar_por_comparacion():
    while True:
        print("\n--- 3. BUSCAR POR DURACIÓN MAYOR A ($gt) ---")
        try:
            minutos = int(input("Ingresa la duración mínima en minutos (ej. 130): "))
            # Se aplica PROYECCIÓN
            proyeccion = {"_id": 0, "titulo": 1, "duracion_minutos": 1}
            peliculas = collection.find({"duracion_minutos": {"$gt": minutos}}, proyeccion)
            encontradas = list(peliculas)
            
            # El 'if encontradas' revisa si la lista tiene por lo menos un resultado adentro.
            if encontradas:
                for p in encontradas:
                    print(f"- {p['titulo']} dura {p['duracion_minutos']} minutos.")
            else:
                print("No se encontraron películas con esa duración.")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
        
        if not preguntar_continuar("Realizar otra búsqueda por duración"):
            break

# Aquí se busca una película escribiendo solo un pedacito de su nombre.
def buscar_por_regex():
    while True:
        print("\n--- 4. BUSCAR POR TÍTULO PARCIAL (Regex) ---")
        texto = input("Ingresa parte del título (ej. 'pad' para El Padrino): ")
        # Se aplica PROYECCIÓN
        proyeccion = {"_id": 0, "titulo": 1, "genero": 1}
        peliculas = collection.find({"titulo": {"$regex": texto, "$options": "i"}}, proyeccion)
        encontradas = list(peliculas)
        if encontradas:
            for p in encontradas:
                print(f"- {p['titulo']} ({p['genero']})")
        else:
            print("No se encontraron resultados.")
            
        if not preguntar_continuar("Realizar otra búsqueda por título"):
            break

# Aquí se buscan películas que salieron entre dos fechas que tú elijas.
def buscar_por_fecha():
    while True:
        print("\n--- 5. BUSCAR POR RANGO DE FECHAS ---")
        try:
            inicio_str = input("Fecha de inicio (YYYY-MM-DD, ej. 2000-01-01): ")
            fin_str = input("Fecha de fin (YYYY-MM-DD, ej. 2020-12-31): ")
            fecha_inicio = datetime.strptime(inicio_str, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fin_str, "%Y-%m-%d")
            
            # Se aplica PROYECCIÓN
            proyeccion = {"_id": 0, "titulo": 1, "fecha_estreno": 1}
            peliculas = collection.find({"fecha_estreno": {"$gte": fecha_inicio, "$lte": fecha_fin}}, proyeccion)
            encontradas = list(peliculas)
            if encontradas:
                for p in encontradas:
                    print(f"- {p['titulo']} | Estreno: {p['fecha_estreno'].strftime('%Y-%m-%d')}")
            else:
                print("No hay películas estrenadas en ese rango de fechas.")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
            
        if not preguntar_continuar("Realizar otra búsqueda por fechas"):
            break

# Aquí se busca qué películas se van a pasar en una sala específica (ej. Sala 1).
def buscar_en_subdocumento():
    while True:
        print("\n--- 6. BUSCAR POR SALA (Dentro del Array) ---")
        sala_buscar = input("Ingresa la sala a buscar (ej. Sala 1): ")
        # Se aplica PROYECCIÓN
        proyeccion = {"_id": 0, "titulo": 1, "funciones": 1}
        peliculas = collection.find({"funciones.sala": sala_buscar}, proyeccion)
        encontradas = list(peliculas)
        if encontradas:
            for p in encontradas:
                print(f"- {p['titulo']} tiene funciones en {sala_buscar}.")
        else:
            print("Ninguna película se proyecta en esa sala.")
            
        if not preguntar_continuar("Realizar otra búsqueda por sala"):
            break

# Aquí se cambia el género de una película usando su nombre exacto.
def actualizar_raiz():
    while True:
        print("\n--- 7. ACTUALIZAR CAMPO RAÍZ (Género) ---")
        titulo = input("Ingresa el título exacto de la película a actualizar: ")
        nuevo_genero = input("Ingresa el nuevo género: ")
        
        resultado = collection.update_one({"titulo": titulo}, {"$set": {"genero": nuevo_genero}})
        
        # Revisa si realmente se modificó alguna película o si nadie cambió de género.
        if resultado.modified_count > 0:
            print(f"¡El género de '{titulo}' ha sido actualizado a '{nuevo_genero}'!")
        else:
            print("No se encontró la película o ya tenía ese género.")
            
        if not preguntar_continuar("Actualizar el género de otra película"):
            break

# Aquí se cambia el precio escondido en los datos de una película usando su nombre.
def actualizar_subdocumento():
    while True:
        print("\n--- 8. ACTUALIZAR SUBDOCUMENTO (Precio General) ---")
        titulo = input("Ingresa el título exacto de la película: ")
        try:
            nuevo_precio = int(input("Ingresa el nuevo precio general (solo números): "))
            resultado = collection.update_one({"titulo": titulo}, {"$set": {"entradas.precio_general": nuevo_precio}})
            if resultado.modified_count > 0:
                print(f"¡Precio general de '{titulo}' actualizado a {nuevo_precio}!")
            else:
                print("No se encontró la película o el precio era el mismo.")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
            
        if not preguntar_continuar("Actualizar el precio de otra película"):
            break

# Aquí se borra una película para siempre usando su nombre exacto.
def eliminar_documento():
    while True:
        print("\n--- 9. ELIMINAR PELÍCULA ---")
        titulo = input("Ingresa el título exacto de la película a eliminar: ")
        confirmacion = input(f"¿Estás seguro de eliminar '{titulo}'? (si/no): ").lower()
        
        if confirmacion == "si":
            resultado = collection.delete_one({"titulo": titulo})
            if resultado.deleted_count > 0:
                print("Película eliminada correctamente.")
            else:
                print("No se encontró ninguna película con ese título.")
        else:
            print("Operación cancelada.")
            
        if not preguntar_continuar("Eliminar otra película"):
            break

# Aquí la base de datos hace los cálculos sola y ordena las películas por género.
def reporte_agrupacion():
    while True:
        print("\n--- 10. REPORTE (Pipeline de Agregación) ---")
        print("Mostrando promedio de duración de las películas agrupadas por Género, ordenadas de mayor a menor:")
        
        pipeline = [
            {"$group": {
                "_id": "$genero", 
                "duracion_promedio": {"$avg": "$duracion_minutos"},
                "cantidad_peliculas": {"$sum": 1}
            }},
            {"$sort": {"duracion_promedio": -1}}
        ]
        
        resultados = collection.aggregate(pipeline)
        for r in resultados:
            print(f"Género: {r['_id']} | Promedio: {round(r['duracion_promedio'], 1)} min | Películas: {r['cantidad_peliculas']}")
            
        if not preguntar_continuar("Generar reporte nuevamente"):
            break

# Aquí se dibuja el menú principal y se revisa qué número elegiste para llamar a la función correcta.
def menu_principal():
    if collection.count_documents({}) == 0:
        inicializar_datos()

    # El 'while True' mantiene el menú pegado en la pantalla hasta que elijas la opción de "0" (Salir).
    while True:
        print("\n" + "="*45)
        print("          BASE DE DATOS DE CINE")
        print("="*45)
        print(" 1. Crear película")
        print(" 2. Listar películas")
        print(" 3. Buscar por duración (> min)")
        print(" 4. Buscar por título (Regex)")
        print(" 5. Buscar por rango de fechas")
        print(" 6. Buscar por sala")
        print(" 7. Actualizar Género (Campo raíz)")
        print(" 8. Actualizar Precio (Subdocumento)")
        print(" 9. Eliminar película")
        print("10. Reporte por Género (Agregación)")
        print(" 0. Salir")
        print("="*45)
        
        opcion = input("Elige una opción: ")
        
        # Aquí hay varios 'if' y 'elif' en escalera para ver qué botón tocaste y mandarte allí.
        if opcion == "1":
            crear_pelicula()
        elif opcion == "2":
            listar_peliculas()
        elif opcion == "3":
            buscar_por_comparacion()
        elif opcion == "4":
            buscar_por_regex()
        elif opcion == "5":
            buscar_por_fecha()
        elif opcion == "6":
            buscar_en_subdocumento()
        elif opcion == "7":
            actualizar_raiz()
        elif opcion == "8":
            actualizar_subdocumento()
        elif opcion == "9":
            eliminar_documento()
        elif opcion == "10":
            reporte_agrupacion()
        elif opcion == "0":
            # El 'break' sirve para romper el ciclo infinito del 'while True' y salir del programa.
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    try:
        menu_principal()
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
