from validaciones import validar_menu
from gestionar_categoria import (
    guardar_categoria,
    actualizar_categoria,
    listar_categoria,
    buscar_categoria,
    eliminar_categoria
)
from logs import historial


def menu_categoria():
    """Menú de gestión de categorías de herramientas."""
    while True:
        op = validar_menu('''
            __________________________________________
            /                                          \\
            |        CONFIGURACIÓN: CATEGORÍAS         |
            |__________________________________________/
            
            Organización de Herramientas del Barrio:
            
                [1] Registrar nueva categoría
                [2] Actualizar datos existentes
                [3] Listar todas las categorías
                [4] Buscar categoría específica
                [5] Eliminar categoría
                [6] Volver al menú anterior
            __________________________________________
            >>> Selecciona una opción (1-6): ''', 1, 6)
        
        match op:
            case 1:
                guardar_categoria()
                historial('Se ha creado una nueva categoría.')
            case 2:
                actualizar_categoria()
                historial('Se ha actualizado una categoría.')
            case 3:
                listar_categoria()
            case 4:
                buscar_categoria()
            case 5:
                eliminar_categoria()
                historial('Se ha eliminado una categoría.')
            case 6:
                break
