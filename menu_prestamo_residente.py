from validaciones import validar_menu
from gestionar_prestamo import (
    guardar_prestamo,
    consultar_prestamo
)


def menu_prestamo_residente():
    """Menú de gestión de préstamos para residentes."""
    while True:
        op = validar_menu('''
            __________________________________________
            /                                          \\
            |       ÁREA RESIDENTE: MIS PRÉSTAMOS      |
            |__________________________________________/
            
            ¿En qué podemos ayudarte hoy?
            
                [1]  Solicitar un nuevo préstamo
                [2]  Consultar el estado de mis préstamos
                [3]  Volver al menú anterior
                
            __________________________________________
            >>> Selecciona una opción (1-3): ''', 1, 3)
        
        match op:
            case 1:
                guardar_prestamo()
            case 2:
                consultar_prestamo()
            case 3:
                break

