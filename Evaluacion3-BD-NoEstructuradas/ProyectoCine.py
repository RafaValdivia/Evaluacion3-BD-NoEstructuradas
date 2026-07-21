import re
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
except Exception:
    print("-> [SISTEMA] El servidor local de MongoDB no está activo o no es alcanzable.")
    try:
        import mongomock
        print("-> [SISTEMA] Iniciando emulador de MongoDB en memoria (mongomock)...")
        client = mongomock.MongoClient()
        db = client['cine_db']
        collection = db['peliculas']
    except ModuleNotFoundError:
        print("-> [ERROR] Para ejecutar sin un servidor MongoDB local activo, por favor instala 'mongomock':")
        print("->         pip install mongomock")
        raise

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

def buscar_pelicula_por_titulo(titulo, proyeccion=None):
    pattern = re.compile(f"^{re.escape(titulo)}$", re.IGNORECASE)
    if proyeccion:
        return collection.find_one({"titulo": pattern}, proyeccion)
    return collection.find_one({"titulo": pattern})

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
        print("\n--- 3. BUSCAR POR DURACIÓN (Operadores de Comparación) ---")
        try:
            minutos = int(input("Ingresa la duración en minutos [EJ: 130]: "))
            print("Operadores: 1. Mayor a ($gt) [defecto] | 2. Menor a ($lt) | 3. Mayor o igual ($gte) | 4. Menor o igual ($lte) | 5. Diferente ($ne)")
            op_sel = input("Selecciona operador (1-5) [Presiona Enter para 1]: ").strip()
            
            op_map = {
                "1": ("$gt", "mayor a"),
                "2": ("$lt", "menor a"),
                "3": ("$gte", "mayor o igual a"),
                "4": ("$lte", "menor o igual a"),
                "5": ("$ne", "diferente de")
            }
            op_mongo, op_desc = op_map.get(op_sel, ("$gt", "mayor a"))
            
            proyeccion = {"_id": 0, "titulo": 1, "duracion_minutos": 1}
            peliculas = collection.find({"duracion_minutos": {op_mongo: minutos}}, proyeccion)
            encontradas = list(peliculas)
            
            if encontradas:
                for p in encontradas:
                    print(f"- {p['titulo']} dura {p['duracion_minutos']} minutos.")
            else:
                print(f"No se encontraron películas con duración {op_desc} {minutos} minutos.")
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
        peliculas = collection.find({"funciones.sala": re.compile(f"^{re.escape(sala_buscar)}$", re.IGNORECASE)}, proyeccion)
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
        titulo = input("Ingresa el título de la película a actualizar [EJ: 'Inception']: ")
        
        # [REQUISITO DESTACADO] Buscar y mostrar el documento ANTES de modificar
        antes = buscar_pelicula_por_titulo(titulo, {"_id": 0, "titulo": 1, "genero": 1})
        if not antes:
            print("No se encontró la película.")
            if not preguntar_continuar("Intentar con otra película"):
                break
            continue
            
        titulo_exacto = antes['titulo']
        print(f"[ESTADO ANTES]: {antes}")
        nuevo_genero = input("Ingresa el nuevo género [EJ: 'Acción y Suspenso']: ")
        
        collection.update_one({"titulo": titulo_exacto}, {"$set": {"genero": nuevo_genero}})
        
        # [REQUISITO DESTACADO] Buscar y mostrar el documento DESPUÉS de modificar
        despues = collection.find_one({"titulo": titulo_exacto}, {"_id": 0, "titulo": 1, "genero": 1})
        print(f"[ESTADO DESPUÉS]: {despues}")
        print("¡El género ha sido actualizado!")
            
        if not preguntar_continuar("Actualizar el género de otra película"):
            break

def actualizar_subdocumento():
    while True:
        print("\n--- 8. ACTUALIZAR PRECIO (Subdocumento) ---")
        titulo = input("Ingresa el título de la película [EJ: 'The Matrix']: ")
        
        # [REQUISITO DESTACADO] Buscar y mostrar el documento ANTES de modificar
        antes = buscar_pelicula_por_titulo(titulo, {"_id": 0, "titulo": 1, "entradas": 1, "funciones": 1})
        if not antes:
            print("No se encontró la película.")
            if not preguntar_continuar("Intentar con otra película"):
                break
            continue
            
        print(f"[ESTADO ANTES]: {antes}")
        print("\nOpciones de actualización:")
        print("1. Modificar precio general ($set en subdocumento)")
        print("2. Agregar nueva función ($push en array)")
        sub_opcion = input("Selecciona opción (1 o 2) [Por defecto: 1]: ").strip()
        
        titulo_exacto = antes['titulo']
        
        try:
            if sub_opcion == "2":
                sala = input("Nombre de la sala [EJ: 'Sala 6']: ").strip()
                horario = input("Horario (HH:MM) [EJ: '20:00']: ").strip()
                idioma = input("Idioma [EJ: 'Subtitulada']: ").strip()
                nueva_funcion = {"sala": sala, "horario": horario, "idioma": idioma}
                
                collection.update_one({"titulo": titulo_exacto}, {"$push": {"funciones": nueva_funcion}})
                print(f"¡Nueva función agregada correctamente con $push a '{titulo_exacto}'!")
            else:
                nuevo_precio = int(input("Ingresa el nuevo precio general [EJ: 4900]: "))
                collection.update_one({"titulo": titulo_exacto}, {"$set": {"entradas.precio_general": nuevo_precio}})
                print(f"¡Precio general actualizado correctamente con $set!")
            
            # [REQUISITO DESTACADO] Buscar y mostrar el documento DESPUÉS de modificar
            despues = collection.find_one({"titulo": titulo_exacto}, {"_id": 0, "titulo": 1, "entradas": 1, "funciones": 1})
            print(f"[ESTADO DESPUÉS]: {despues}")
        except ValueError:
            print("Formato no válido, respete las indicaciones.")
            
        if not preguntar_continuar("Actualizar otra película"):
            break

def eliminar_documento():
    while True:
        print("\n--- 9. ELIMINAR PELÍCULA ---")
        titulo = input("Ingresa el título de la película a eliminar [EJ: 'Shrek']: ")
        
        # [REQUISITO DESTACADO] Mostrar el documento que se va a eliminar antes de procesar
        pelicula_a_borrar = buscar_pelicula_por_titulo(titulo, {"_id": 0, "titulo": 1, "genero": 1, "duracion_minutos": 1})
        
        if pelicula_a_borrar:
            titulo_exacto = pelicula_a_borrar['titulo']
            print(f"\n[DOCUMENTO ENCONTRADO]: {pelicula_a_borrar}")
            confirmacion = input(f"¿Estás seguro de eliminar '{titulo_exacto}'? (si/no) [EJ: 'si']: ").strip().lower()
            
            if confirmacion in ["si", "sí", "s", "y", "yes"]:
                collection.delete_one({"titulo": titulo_exacto})
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
        print(" 3. Buscar por duración (Operadores)")
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
