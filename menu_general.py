from validaciones import validar_menu
from menu_categoria import menu_categoria
from menu_herramientas import menu_herramienta
from menu_usuario import menu_usuario
from menu_prestamo_admin import menu_prestamo_admin
from menu_consultas import menu_reportes
from permisos import login
from gestionar_json import cargar
from logs import historial
from menu_prestamo_residente import menu_prestamo_residente


def _mostrar_mensaje_salida_admin():
    """Muestra el mensaje de despedida del administrador."""
    print('''
        __________________________________________
        /                                          \\
        |      ¡HASTA LUEGO, VECINO ADMIN!          |
        |__________________________________________/
        
        La sesión se ha cerrado correctamente.
        Gracias por cuidar de nuestra comunidad.
        
        [ ESTADO: SISTEMA FUERA DE LÍNEA ]
        __________________________________________
    ''')


def _mostrar_mensaje_salida_residente():
    """Muestra el mensaje de despedida del residente."""
    print('''
        __________________________________________
        /                                          \\
        |      ¡HASTA LUEGO, VECINO RESIDENTE!      |
        |__________________________________________/
        
        La sesión se ha cerrado correctamente.
        Gracias por cuidar de nuestra comunidad.
        
        [ ESTADO: SISTEMA FUERA DE LÍNEA ]
        __________________________________________
    ''')


def _validar_categoria_existe():
    """Verifica si existen categorías registradas."""
    if not cargar('categorias.json'):
        print('No se puede registrar herramientas hasta ingresar una categoría.')
        historial('Intento de registro de herramienta sin categorías disponibles.')
        return False
    return True


def _validar_usuarios_herramientas_existen():
    """Verifica si existen usuarios y herramientas registrados."""
    if not cargar('usuarios.json') or not cargar('herramientas.json'):
        print('No hay registros de usuarios o herramientas.')
        print('Contacte al administrador para registrar usuarios y herramientas.')
        historial('Intento de gestión de préstamo sin usuarios o herramientas.')
        return False
    return True


def _validar_reportes_disponibles():
    """Verifica si hay registros disponibles para reportes."""
    if not cargar('prestamos.json') or not cargar('herramientas.json'):
        print('No hay registros disponibles para consultas de reportes.')
        historial('Intento de consulta de reportes sin registros.')
        return False
    return True


def menu_general():
    """Menú principal del sistema."""
    permiso = login()
    while True:
        if permiso == 'admin':
            op_menu_admin = validar_menu('''
                /\\______________/\\
                /  ¡BIENVENIDO A!  \\
                |      APP: TU       |
                |AMIGO DEL VECINDARIO|
                \\  ____________  /
                \\/            \\/

                ******* ¡HOLA ADMIN! *****
                Selecciona una opción:
                -----------------------
                1) Gestionar Herramientas
                2) Gestionar Categorías
                3) Gestionar Usuarios
                4) Gestionar Préstamos
                5) Consultar Reportes
                6) Salir
                -----------------------
                >>>''', 1, 6)
            
            match op_menu_admin:
                case 1:
                    if _validar_categoria_existe():
                        menu_herramienta()
                case 2:
                    menu_categoria()
                case 3:
                    menu_usuario()
                case 4:
                    if _validar_usuarios_herramientas_existen():
                        menu_prestamo_admin()
                case 5:
                    if _validar_reportes_disponibles():
                        menu_reportes()
                case 6:
                    _mostrar_mensaje_salida_admin()
                    break
        else:
            op_menu_residente = validar_menu('''
                /\\______________/\\
                /  ¡BIENVENIDO A!  \\
                |      APP: TU       |
                |AMIGO DEL VECINDARIO|
                \\  ____________  /
                \\/            \\/

                ***** ¡HOLA VECINO! *****
                Selecciona una opción:
                -----------------------
                1) Solicitar Préstamo
                2) Salir
                -----------------------
                >>>''', 1, 2)
            
            match op_menu_residente:
                case 1:
                    if _validar_usuarios_herramientas_existen():
                        menu_prestamo_residente()
                case 2:
                    _mostrar_mensaje_salida_residente()
                    break

                    
