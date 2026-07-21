from pymongo import MongoClient
import pymongo.errors
from datetime import datetime

# Intentar conectar a MongoDB local; si no está activo, usar mongomock (emulador en memoria)
try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=2000)
    # Validar conexión
    client.server_info()
    db = client['cine_db']
    collection = db['peliculas']
    print("-> [SISTEMA] Conectado exitosamente al servidor MongoDB local.")
except (pymongo.errors.ServerSelectionTimeoutError, Exception):
    print("-> [SISTEMA] El servidor local de MongoDB no está activo o no es compatible con el procesador.")
    print("-> [SISTEMA] Iniciando emulador de MongoDB en memoria (mongomock)...")
    import mongomock
    client = mongomock.MongoClient()
    db = client['cine_db']
    collection = db['peliculas']

# Inicializar base de datos con documentos de prueba (Mínimo 8 documentos)
def inicializar_datos(): 
    # solo inserta si la colección está vacía
    if collection.count_documents({}) == 0:
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
        collection.insert_many(peliculas_data)
        print("-> Precarga de 8 documentos completada con éxito.")

def preguntar_continuar(accion_repetir):
    while True:
        print(f"\n1. {accion_repetir}")
        print("2. Volver al menú principal")
        opcion = input("Selecciona la opción: ").strip()
        
        if opcion == "1":
            return True
        elif opcion == "2":
            return False
        else:
            print("Opción inválida. Intenta nuevamente.")

# --- OPERACIONES CRUD ---

def crear_pelicula():
    while True:
        print("\n--- 1. CREAR NUEVA PELÍCULA ---")
        try:
            titulo = input("Título [EJ: 'Spiderman'] (no debe estar vacío): ").strip()
            if not titulo:
                print("Formato no válido, respete las indicaciones.")
                continue

            genero = input("Género [EJ: 'Acción'] (no debe estar vacío): ").strip()
            if not genero:
                print("Formato no válido, respete las indicaciones.")
                continue

            duracion = int(input("Duración (minutos) [EJ: 120]: "))
            fecha_str = input("Fecha de estreno (AAAA-MM-DD) [EJ: '2024-12-31'] (no debe estar vacío): ")
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d")
            
            precio_gen = int(input("Precio entrada general [EJ: 5000]: "))
            precio_nino = int(input("Precio entrada niño [EJ: 3000]: "))
            
            sala = input("Sala [EJ: 'Sala 1'] (no debe estar vacío): ").strip()
            horario = input("Horario (HH:MM) [EJ: '15:00'] (no debe estar vacío): ").strip()
            idioma = input("Idioma [EJ: 'Doblada'] (no debe estar vacío): ").strip()
            
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
            
            collection.insert_one(nueva_pelicula)
            print(f"¡Película '{titulo}' insertada exitosamente!")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
        
        if not preguntar_continuar("Crear otra película"):
            break

def listar_peliculas():
    while True:
        print("\n--- 2. LISTAR PELÍCULAS ---")
        proyeccion = {"_id": 0, "titulo": 1, "genero": 1, "fecha_estreno": 1, "duracion_minutos": 1}
        peliculas = collection.find({}, proyeccion)
        
        for p in peliculas:
            fecha_str = p['fecha_estreno'].strftime('%Y-%m-%d')
            print(f"- {p['titulo']} | Género: {p['genero']} | Estreno: {fecha_str} | Duración: {p['duracion_minutos']} min")
        
        if not preguntar_continuar("Listar nuevamente"):
            break

def buscar_por_comparacion():
    while True:
        print("\n--- 3. BUSCAR POR DURACIÓN MAYOR A ($gt) ---")
        try:
            minutos = int(input("Ingresa la duración mínima en minutos [EJ: 130]: "))
            proyeccion = {"_id": 0, "titulo": 1, "duracion_minutos": 1}
            peliculas = collection.find({"duracion_minutos": {"$gt": minutos}}, proyeccion)
            encontradas = list(peliculas)
            
            if encontradas:
                for p in encontradas:
                    print(f"- {p['titulo']} dura {p['duracion_minutos']} minutos.")
            else:
                print("No se encontraron películas con esa duración.")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
        
        if not preguntar_continuar("Realizar otra búsqueda por duración"):
            break

def buscar_por_regex():
    while True:
        print("\n--- 4. BUSCAR POR TÍTULO PARCIAL (Regex) ---")
        texto = input("Ingresa parte del título [EJ: 'pad']: ")
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

def buscar_por_fecha():
    while True:
        print("\n--- 5. BUSCAR POR RANGO DE FECHAS ---")
        try:
            inicio_str = input("Fecha de inicio (AAAA-MM-DD) [EJ: '2000-01-01']: ")
            fin_str = input("Fecha de fin (AAAA-MM-DD) [EJ: '2020-12-31']: ")
            fecha_inicio = datetime.strptime(inicio_str, "%Y-%m-%d")
            fecha_fin = datetime.strptime(fin_str, "%Y-%m-%d")
            
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

def buscar_en_subdocumento():
    while True:
        print("\n--- 6. BUSCAR POR SALA (Dentro del Array) ---")
        sala_buscar = input("Ingresa la sala a buscar [EJ: 'Sala 1']: ")
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

def actualizar_raiz():
    while True:
        print("\n--- 7. ACTUALIZAR CAMPO RAÍZ (Género) ---")
        titulo = input("Ingresa el título exacto de la película a actualizar [EJ: 'Inception']: ")
        
        # [REQUISITO DESTACADO] Buscar y mostrar el documento ANTES de modificar
        antes = collection.find_one({"titulo": titulo}, {"_id": 0, "titulo": 1, "genero": 1})
        if not antes:
            print("No se encontró la película.")
            if not preguntar_continuar("Intentar con otra película"):
                break
            continue
            
        print(f"[ESTADO ANTES]: {antes}")
        nuevo_genero = input("Ingresa el nuevo género [EJ: 'Acción y Suspenso']: ")
        
        collection.update_one({"titulo": titulo}, {"$set": {"genero": nuevo_genero}})
        
        # [REQUISITO DESTACADO] Buscar y mostrar el documento DESPUÉS de modificar
        despues = collection.find_one({"titulo": titulo}, {"_id": 0, "titulo": 1, "genero": 1})
        print(f"[ESTADO DESPUÉS]: {despues}")
        print("¡El género ha sido actualizado!")
            
        if not preguntar_continuar("Actualizar el género de otra película"):
            break

def actualizar_subdocumento():
    while True:
        print("\n--- 8. ACTUALIZAR SUBDOCUMENTO (Precio General) ---")
        titulo = input("Ingresa el título exacto de la película [EJ: 'The Matrix']: ")
        
        # [REQUISITO DESTACADO] Buscar y mostrar el documento ANTES de modificar
        antes = collection.find_one({"titulo": titulo}, {"_id": 0, "titulo": 1, "entradas.precio_general": 1})
        if not antes:
            print("No se encontró la película.")
            if not preguntar_continuar("Intentar con otra película"):
                break
            continue
            
        print(f"[ESTADO ANTES]: {antes}")
        try:
            nuevo_precio = int(input("Ingresa el nuevo precio general [EJ: 4900]: "))
            collection.update_one({"titulo": titulo}, {"$set": {"entradas.precio_general": nuevo_precio}})
            
            # [REQUISITO DESTACADO] Buscar y mostrar el documento DESPUÉS de modificar
            despues = collection.find_one({"titulo": titulo}, {"_id": 0, "titulo": 1, "entradas.precio_general": 1})
            print(f"[ESTADO DESPUÉS]: {despues}")
            print("¡Precio general actualizado!")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
            
        if not preguntar_continuar("Actualizar el precio de otra película"):
            break

def eliminar_documento():
    while True:
        print("\n--- 9. ELIMINAR PELÍCULA ---")
        titulo = input("Ingresa el título exacto de la película a eliminar [EJ: 'Shrek']: ")
        
        # [REQUISITO DESTACADO] Mostrar el documento que se va a eliminar antes de procesar
        pelicula_a_borrar = collection.find_one({"titulo": titulo}, {"_id": 0, "titulo": 1, "genero": 1, "duracion_minutos": 1})
        
        if pelicula_a_borrar:
            print(f"\n[DOCUMENTO ENCONTRADO]: {pelicula_a_borrar}")
            confirmacion = input(f"¿Estás seguro de eliminar '{titulo}'? (si/no) [EJ: 'si']: ").lower()
            
            if confirmacion == "si":
                collection.delete_one({"titulo": titulo})
                print("Película eliminada correctamente.")
            else:
                print("Operación cancelada.")
        else:
            print("No se encontró ninguna película con ese título.")
            
        if not preguntar_continuar("Eliminar otra película"):
            break

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
            {"$sort": {"duracion_promedio": -1}},
            {"$project": {
                "genero": "$_id",
                "duracion_promedio": 1,
                "cantidad_peliculas": 1,
                "_id": 0
            }}
        ]
        
        resultados = collection.aggregate(pipeline)
        for r in resultados:
            print(f"Género: {r['genero']} | Promedio: {round(r['duracion_promedio'], 1)} min | Películas: {r['cantidad_peliculas']}")
            
        if not preguntar_continuar("Generar reporte nuevamente"):
            break

# Menú principal de la aplicación
def menu_principal():
    inicializar_datos()

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
