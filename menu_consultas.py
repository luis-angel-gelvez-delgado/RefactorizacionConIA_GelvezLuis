from validaciones import validar_menu
from gestionar_consultas import (
    stock_minimo,
    activos_completados,
    historial_usuarios,
    herramienta_mas_usada,
    usuario_mas_usado
)


def menu_reportes():
    """Menú de reportes y consultas generales del sistema."""
    while True:
        op_reporte = validar_menu('''
            __________________________________________
            /                                          \\
            |       REPORTE Y CONSULTAS GENERALES      |
            |__________________________________________/
            
            Filtros de información disponibles:
            
                [1]  Stock mínimo (Baja disponibilidad)
                [2]  Solicitudes en proceso / completadas
                [3]  Buscar solicitudes por usuario
                [4]  Herramientas más usadas
                [5]  Usuarios con más préstamos
                [6]  Volver al menú anterior
                
            __________________________________________
            >>> Selecciona el reporte a generar (1-6): ''', 1, 6)
        
        match op_reporte:
            case 1:
                stock_minimo()
            case 2:
                activos_completados()
            case 3:
                historial_usuarios()
            case 4:
                herramienta_mas_usada()
            case 5:
                usuario_mas_usado()
            case 6:
                break
