import sys
import builtins

# Lista de entradas simuladas para recorrer todo el menú
inputs = [
    # 1. Crear película
    "1", "Spiderman", "Acción", "120", "2024-12-31", "5000", "3000", "Sala 1", "15:00", "Doblada", "2",
    # 2. Listar películas
    "2", "2",
    # 3. Buscar por duración (> 140 min)
    "3", "140", "2",
    # 4. Buscar por título parcial ("pad")
    "4", "pad", "2",
    # 5. Buscar por rango de fechas (2000 a 2015)
    "5", "2000-01-01", "2015-12-31", "2",
    # 6. Buscar por sala ("Sala 1")
    "6", "Sala 1", "2",
    # 7. Actualizar Género ("Inception" -> "Acción y Suspenso")
    "7", "Inception", "Acción y Suspenso", "2",
    # 8. Actualizar Precio ("The Matrix" -> 4900)
    "8", "The Matrix", "4900", "2",
    # 9. Eliminar película ("Shrek" -> si)
    "9", "Shrek", "si", "2",
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
