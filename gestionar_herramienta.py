from gestionar_json import cargar, guardar, generar_id
from validaciones import validar_menu, validar_entero, validar_texto
from gestionar_categoria import validar_categoria, listar_categoria
from transformaciones import transformar_estado

NOMBRE_ARCHIVO = 'herramientas.json'


def _obtener_nombre_categoria(elemento):
    """Obtiene el nombre de la categoría de una herramienta de forma segura."""
    return elemento.get('categoria', {}).get('categoria', 'No encontrado')


def _obtener_id_categoria(elemento):
    """Obtiene el ID de la categoría de una herramienta de forma segura."""
    return elemento.get('categoria', {}).get('id', 'No encontrado')


def _imprimir_herramienta(elemento):
    """Imprime la información detallada de una herramienta."""
    print(f'''
        ****************************
        ID:             {elemento.get('id', 'No encontrado')}
        Nombre:         {elemento.get('nombre', 'No encontrado')}
        ID Categoría:   {_obtener_id_categoria(elemento)}
        Categoría:      {_obtener_nombre_categoria(elemento)}
        Cantidad:       {elemento.get('cantidad', 'No encontrado')}
        Estado:         {elemento.get('estado', 'No encontrado')}
        Precio:         {elemento.get('precio', 'No encontrado')}
    ''')


def guardar_herramienta():
    registros = cargar(NOMBRE_ARCHIVO)
    diccionario = {}
    diccionario['id'] = generar_id(registros)
    diccionario['nombre'] = validar_texto('Ingrese el nombre: ', 1, 20)
    
    listar_categoria()
    id_categoria = validar_entero('Ingrese el id de la categoría: ')
    while validar_categoria(id_categoria) is False:
        id_categoria = validar_entero('Error, categoría no encontrada. Intente nuevamente: ')
    diccionario['categoria'] = validar_categoria(id_categoria)
    
    diccionario['cantidad'] = validar_entero('Ingrese la cantidad disponible de esta herramienta: ')
    
    estado_id = validar_menu('''
        Seleccione el estado de la herramienta:
        1. Activa
        2. En reparación
        3. Fuera de servicio
    ''', 1, 3)
    diccionario['estado'] = transformar_estado(estado_id)
    
    diccionario['precio'] = validar_entero('Ingrese el valor de la herramienta: ')
    
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO, registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')


def listar_herramienta():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay herramientas registradas.')
        return
    for elemento in registros:
        _imprimir_herramienta(elemento)

def validar_herramienta(id_herramienta):
    """Valida que una herramienta exista y retorna sus datos."""
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return False
    
    for elemento in registros:
        if elemento.get('id') == id_herramienta:
            return elemento
    return False


def buscar_herramienta():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay herramientas registradas.')
        return
    
    id_herramienta = validar_entero('Ingrese el id de la herramienta a buscar: ')
    for elemento in registros:
        if elemento.get('id') == id_herramienta:
            _imprimir_herramienta(elemento)
            return
    
    print(f'No se encontró la herramienta con ID {id_herramienta}.')


def actualizar_herramienta():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay herramientas registradas.')
        return
    
    listar_herramienta()
    id_herramienta = validar_entero('Ingrese el id de la herramienta a actualizar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_herramienta:
            op_actualizar = validar_menu('''
                ¿Qué dato desea actualizar?
                1. Nombre
                2. Categoría
                3. Estado
                4. Precio
                5. Cantidad
                6. Cancelar
            ''', 1, 6)
            
            match op_actualizar:
                case 1:
                    elemento['nombre'] = validar_texto('Ingrese el nombre: ', 1, 20)
                case 2:
                    listar_categoria()
                    id_categoria = validar_entero('Ingrese el id de la categoría: ')
                    while validar_categoria(id_categoria) is False:
                        id_categoria = validar_entero('Error, categoría no encontrada. Intente nuevamente: ')
                    elemento['categoria'] = validar_categoria(id_categoria)
                case 3:
                    estado_id = validar_menu('''
                        Seleccione el nuevo estado:
                        1. Activa
                        2. En reparación
                        3. Fuera de servicio
                    ''', 1, 3)
                    elemento['estado'] = transformar_estado(estado_id)
                case 4:
                    elemento['precio'] = validar_entero('Ingrese el nuevo valor de la herramienta: ')
                case 5:
                    elemento['cantidad'] = validar_entero('Ingrese la nueva cantidad disponible: ')
                case 6:
                    print('Operación cancelada.')
                    return
            
            guardar(NOMBRE_ARCHIVO, registros)
            print('DATO ACTUALIZADO CORRECTAMENTE!')
            return
    
    print(f'No se encontró la herramienta con ID {id_herramienta}.')


def eliminar_herramienta():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay herramientas registradas.')
        return
    
    listar_herramienta()
    id_herramienta = validar_entero('Ingrese el id de la herramienta a eliminar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_herramienta:
            nombre = elemento.get('nombre', 'Herramienta')
            print(f'La herramienta "{nombre}" ha sido eliminada.')
            registros.remove(elemento)
            guardar(NOMBRE_ARCHIVO, registros)
            return
    
    print(f'No se encontró la herramienta con ID {id_herramienta}.')

