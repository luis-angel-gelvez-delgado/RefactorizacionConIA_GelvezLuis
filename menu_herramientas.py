from validaciones import validar_menu
from gestionar_herramienta import (
    guardar_herramienta,
    actualizar_herramienta,
    listar_herramienta,
    buscar_herramienta,
    eliminar_herramienta
)
from logs import historial


def menu_herramienta():
    """Menú de gestión de herramientas del inventario."""
    while True:
        op = validar_menu('''
            __________________________________________
            /                                          \\
            |    INVENTARIO: GESTIÓN DE HERRAMIENTAS  |
            |__________________________________________/
            
            Panel de Control - Selecciona una acción:
            
                [1] Registrar nueva herramienta
                [2] Actualizar datos existentes
                [3] Listar inventario completo
                [4] Buscar herramienta específica
                [5] Eliminar del sistema
                [6] Volver al menú anterior
                
            __________________________________________
            >>> Digita tu opción (1-6): ''', 1, 6)
        
        match op:
            case 1:
                guardar_herramienta()
                historial('Se ha registrado una herramienta nueva.')
            case 2:
                actualizar_herramienta()
                historial('Se ha actualizado una herramienta.')
            case 3:
                listar_herramienta()
            case 4:
                buscar_herramienta()
            case 5:
                eliminar_herramienta()
                historial('Se ha eliminado una herramienta.')
            case 6:
                break
