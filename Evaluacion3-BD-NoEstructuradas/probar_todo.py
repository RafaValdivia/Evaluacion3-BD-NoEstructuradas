import sys
import builtins

# Lista de entradas simuladas para recorrer todo el menú
inputs = [
    # 1. Crear película
    "1", "Spiderman", "Acción", "120", "2024-12-31", "5000", "3000", "Sala 1", "15:00", "Doblada", "2",
    # 2. Listar películas
    "2", "2",
    # 3. Buscar por duración (> 140 min con operador $gt)
    "3", "140", "1", "2",
    # 4. Buscar por título parcial ("pad")
    "4", "pad", "2",
    # 5. Buscar por rango de fechas (2000 a 2015)
    "5", "2000-01-01", "2015-12-31", "2",
    # 6. Buscar por sala ("Sala 1")
    "6", "Sala 1", "2",
    # 7. Actualizar Género ("inception" en minúsculas -> "Acción y Suspenso")
    "7", "inception", "Acción y Suspenso", "2",
    # 8a. Actualizar Precio ($set en subdocumento para "the matrix" en minúsculas)
    "8", "the matrix", "1", "4900", "2",
    # 8b. Agregar Función ($push en array para "the matrix")
    "8", "the matrix", "2", "Sala 6", "20:00", "Subtitulada", "2",
    # 9. Eliminar película ("shrek" -> "sí" con tilde)
    "9", "shrek", "sí", "2",
    # 10. Reporte por Género (Agregación)
    "10", "2",
    # 0. Salir
    "0"
]

def mock_input(prompt=""):
    if not inputs:
        print(f"{prompt}0")
        return "0"
    val = inputs.pop(0)
    print(f"{prompt}{val}")
    return val

# Reemplazamos la función input nativa por nuestro mock
builtins.input = mock_input

# Importamos y ejecutamos la función menu_principal de tu proyecto
print("=== INICIANDO SIMULACIÓN COMPLETA DE PROYECTOCINE ===")
import ProyectoCine
ProyectoCine.menu_principal()
print("=== SIMULACIÓN FINALIZADA CON ÉXITO ===")
