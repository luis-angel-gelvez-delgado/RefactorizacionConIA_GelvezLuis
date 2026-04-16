from validaciones import validar_menu
from gestionar_prestamo import (
    guardar_prestamo,
    gestionar_prestamo,
    consultar_prestamo,
    buscar_prestamo,
    listar_prestamo,
    eliminar_prestamo
)


def menu_prestamo():
    """Menú unificado de gestión de préstamos."""
    while True:
        op = validar_menu('''
            1. Registrar préstamo
            2. Gestionar préstamo
            3. Consultar tus préstamos
            4. Buscar una solicitud de préstamo
            5. Ver solicitudes de préstamo
            6. Eliminar solicitudes
            7. Salir
        ''', 1, 7)
        
        match op:
            case 1:
                guardar_prestamo()
            case 2:
                gestionar_prestamo()
            case 3:
                consultar_prestamo()
            case 4:
                buscar_prestamo()
            case 5:
                listar_prestamo()
            case 6:
                eliminar_prestamo()
            case 7:
                break

