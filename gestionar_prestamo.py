from gestionar_json import cargar, guardar, generar_id
from gestionar_usuario import listar_usuario, validar_usuario
from validaciones import validar_entero, validar_menu
from gestionar_herramienta import listar_herramienta, validar_herramienta
from transformaciones import solicitar_fecha_inicio, gestionar, rechazar
from datetime import timedelta

NOMBRE_ARCHIVO = 'prestamos.json'


def _obtener_nombre_usuario(elemento):
    """Obtiene el nombre del usuario de un préstamo de forma segura."""
    return elemento.get('usuario', {}).get('nombre', 'No encontrado')


def _obtener_id_usuario(elemento):
    """Obtiene el ID del usuario de un préstamo de forma segura."""
    return elemento.get('usuario', {}).get('id', 'No encontrado')


def _obtener_nombre_herramienta(elemento):
    """Obtiene el nombre de la herramienta de un préstamo de forma segura."""
    return elemento.get('herramienta', {}).get('nombre', 'No encontrado')


def _obtener_id_herramienta(elemento):
    """Obtiene el ID de la herramienta de un préstamo de forma segura."""
    return elemento.get('herramienta', {}).get('id', 'No encontrado')


def guardar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    diccionario = {}
    diccionario['id'] = generar_id(registros)
    
    listar_usuario()
    id_usuario = validar_entero('Ingrese el id del usuario: ')
    while validar_usuario(id_usuario) is False:
        id_usuario = validar_entero('Error, usuario no encontrado. Intente nuevamente: ')
    diccionario['usuario'] = validar_usuario(id_usuario)
    
    listar_herramienta()
    id_herramienta = validar_entero('Ingrese el id de la herramienta: ')
    while validar_herramienta(id_herramienta) is False:
        id_herramienta = validar_entero('Error, herramienta no encontrada. Intente nuevamente: ')
    diccionario['herramienta'] = validar_herramienta(id_herramienta)
    
    cantidad = validar_entero('Ingrese la cantidad de herramientas a solicitar: ')
    diccionario['cantidad'] = cantidad
    
    diccionario['fecha_inicio'] = solicitar_fecha_inicio()
    dias = validar_entero('Ingrese la cantidad de días a usar la herramienta: ')
    diccionario['fecha_final'] = diccionario['fecha_inicio'] + timedelta(days=dias)
    diccionario['fecha_inicio'] = str(diccionario['fecha_inicio'])
    diccionario['fecha_final'] = str(diccionario['fecha_final'])
    diccionario['estado'] = 'En proceso'
    diccionario['observaciones'] = 'Pendiente'
    
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO, registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')
    print(f'SU ID ES {diccionario.get("id", "ID no encontrado")}, POR FAVOR GUÁRDELO PARA HACER SEGUIMIENTO')

def _imprimir_prestamo(elemento):
    """Imprime la información detallada de un préstamo."""
    print(f'''
        ****************************
        ID:             {elemento.get('id', 'No encontrado')}
        Usuario:        {_obtener_nombre_usuario(elemento)}
        ID Usuario:     {_obtener_id_usuario(elemento)}
        Herramienta:    {_obtener_nombre_herramienta(elemento)}
        ID Herramienta: {_obtener_id_herramienta(elemento)}
        Fecha Inicio:   {elemento.get('fecha_inicio', 'No encontrado')}
        Fecha Entrega:  {elemento.get('fecha_final', 'No encontrado')}
        Cantidad:       {elemento.get('cantidad', 'No encontrado')}
        Estado:         {elemento.get('estado', 'No encontrado')}
        Observaciones:  {elemento.get('observaciones', 'No encontrado')}
    ''')


def listar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay préstamos registrados.')
        return
    for elemento in registros:
        _imprimir_prestamo(elemento)


def consultar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay préstamos registrados.')
        return
    
    id_usuario = validar_entero('Ingrese el id de su usuario. Si no lo conoce contacte al administrador: ')
    encontrados = [
        e for e in registros
        if e.get('usuario', {}).get('id') == id_usuario
    ]
    
    if not encontrados:
        print(f'No se encontraron préstamos para el usuario con ID {id_usuario}.')
        return
    
    for elemento in encontrados:
        _imprimir_prestamo(elemento)


def buscar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay préstamos registrados.')
        return
    
    id_prestamo = validar_entero('Ingrese el id del préstamo a buscar: ')
    for elemento in registros:
        if elemento.get('id') == id_prestamo:
            _imprimir_prestamo(elemento)
            return
    
    print(f'No se encontró el préstamo con ID {id_prestamo}.')


def gestionar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay préstamos registrados.')
        return
    
    listar_prestamo()
    id_prestamo = validar_entero('Ingrese el id del préstamo a gestionar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_prestamo:
            op_gestionar = validar_menu('''
                Seleccione qué opción desea realizar con el préstamo:
                1. Gestionar (Aceptar o rechazar por stock)
                2. Rechazar (Indicar motivo)
            ''', 1, 2)
            
            match op_gestionar:
                case 1:
                    id_herramienta = _obtener_id_herramienta(elemento)
                    gestionar(id_herramienta, elemento)
                case 2:
                    rechazar(elemento)
            
            guardar(NOMBRE_ARCHIVO, registros)
            return
    
    print(f'No se encontró el préstamo con ID {id_prestamo}.')


def eliminar_prestamo():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay préstamos registrados.')
        return
    
    listar_prestamo()
    id_prestamo = validar_entero('Ingrese el id del préstamo a eliminar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_prestamo:
            nombre_herramienta = _obtener_nombre_herramienta(elemento)
            print(f'El préstamo de "{nombre_herramienta}" ha sido eliminado.')
            registros.remove(elemento)
            guardar(NOMBRE_ARCHIVO, registros)
            return
    
    print(f'No se encontró el préstamo con ID {id_prestamo}.')
