from validaciones import validar_menu, validar_texto, validar_entero
from gestionar_json import cargar, guardar, generar_id

NOMBRE_ARCHIVO = 'categorias.json'


def _imprimir_categoria(elemento):
    """Imprime la información detallada de una categoría."""
    print(f'''
        ****************************
        ID:         {elemento.get('id', 'No encontrado')}
        Categoría:  {elemento.get('nombre', 'No encontrado')}
    ''')


def guardar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    diccionario = {}
    diccionario['id'] = generar_id(registros)
    diccionario['nombre'] = validar_texto('Ingrese el nombre de la categoría: ', 1, 30)
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO, registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')


def listar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay categorías registradas.')
        return
    for elemento in registros:
        _imprimir_categoria(elemento)


def buscar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay categorías registradas.')
        return
    
    id_categoria = validar_entero('Ingrese el id de la categoría a buscar: ')
    for elemento in registros:
        if elemento.get('id') == id_categoria:
            _imprimir_categoria(elemento)
            return
    
    print(f'No se encontró la categoría con ID {id_categoria}.')


def validar_categoria(id_categoria):
    """Valida que una categoría exista y retorna sus datos."""
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return False
    
    for elemento in registros:
        if elemento.get('id') == id_categoria:
            return elemento
    return False


def actualizar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay categorías registradas.')
        return
    
    listar_categoria()
    id_categoria = validar_entero('Ingrese el id de la categoría a actualizar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_categoria:
            op_actualizar = validar_menu('''
                ¿Qué dato desea actualizar?
                1. Nombre de la categoría
                2. Cancelar
            ''', 1, 2)
            
            match op_actualizar:
                case 1:
                    elemento['nombre'] = validar_texto('Ingrese el nuevo nombre de la categoría: ', 1, 30)
                case 2:
                    print('Operación cancelada.')
                    return
            
            guardar(NOMBRE_ARCHIVO, registros)
            print('DATO ACTUALIZADO CORRECTAMENTE!')
            return
    
    print(f'No se encontró la categoría con ID {id_categoria}.')


def eliminar_categoria():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay categorías registradas.')
        return
    
    listar_categoria()
    id_categoria = validar_entero('Ingrese el id de la categoría a eliminar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_categoria:
            nombre = elemento.get('nombre', 'Categoría')
            print(f'La categoría "{nombre}" ha sido eliminada.')
            registros.remove(elemento)
            guardar(NOMBRE_ARCHIVO, registros)
            return
    
    print(f'No se encontró la categoría con ID {id_categoria}.')
