from gestionar_json import cargar, guardar, generar_id
from validaciones import validar_entero, validar_texto, validar_menu
from transformaciones import transformar_tipo

NOMBRE_ARCHIVO = 'usuarios.json'


def _imprimir_usuario(elemento):
    """Imprime la información detallada de un usuario."""
    print(f'''
        ****************************
        ID:             {elemento.get('id', 'No encontrado')}
        Nombre:         {elemento.get('nombre', 'No encontrado')}
        Apellido:       {elemento.get('apellido', 'No encontrado')}
        Teléfono:       {elemento.get('telefono', 'No encontrado')}
        Dirección:      {elemento.get('direccion', 'No encontrado')}
        Tipo Usuario:   {elemento.get('tipo', 'No encontrado')}
    ''')


def guardar_usuario():
    registros = cargar(NOMBRE_ARCHIVO)
    diccionario = {}
    diccionario['id'] = generar_id(registros)
    diccionario['nombre'] = validar_texto('Ingrese el nombre de la persona: ', 1, 30)
    diccionario['apellido'] = validar_texto('Ingrese el apellido de la persona: ', 1, 30)
    diccionario['telefono'] = validar_entero('Ingrese su número de teléfono: ')
    diccionario['direccion'] = validar_texto('Ingrese la dirección de residencia del usuario: ', 1, 50)
    
    tipo_id = validar_menu('''
        Seleccione el tipo de usuario:
        1. Residente
        2. Administrador
    ''', 1, 2)
    diccionario['tipo'] = transformar_tipo(tipo_id)
    
    registros.append(diccionario)
    guardar(NOMBRE_ARCHIVO, registros)
    print('DATOS GUARDADOS CORRECTAMENTE!')


def listar_usuario():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay usuarios registrados.')
        return
    for elemento in registros:
        _imprimir_usuario(elemento)


def buscar_usuario():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay usuarios registrados.')
        return
    
    id_usuario = validar_entero('Ingrese el id del usuario a buscar: ')
    for elemento in registros:
        if elemento.get('id') == id_usuario:
            _imprimir_usuario(elemento)
            return
    
    print(f'No se encontró el usuario con ID {id_usuario}.')


def validar_usuario(id_usuario):
    """Valida que un usuario exista y retorna sus datos."""
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        return False
    
    for elemento in registros:
        if elemento.get('id') == id_usuario:
            return elemento
    return False


def actualizar_usuario():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay usuarios registrados.')
        return
    
    listar_usuario()
    id_usuario = validar_entero('Ingrese el id del usuario a actualizar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_usuario:
            op_actualizar = validar_menu('''
                ¿Qué dato desea actualizar?
                1. Nombre
                2. Apellido
                3. Teléfono
                4. Dirección
                5. Tipo de usuario
                6. Cancelar
            ''', 1, 6)
            
            match op_actualizar:
                case 1:
                    elemento['nombre'] = validar_texto('Ingrese el nombre: ', 1, 30)
                case 2:
                    elemento['apellido'] = validar_texto('Ingrese el apellido: ', 1, 30)
                case 3:
                    elemento['telefono'] = validar_entero('Ingrese el número de teléfono: ')
                case 4:
                    elemento['direccion'] = validar_texto('Ingrese la dirección: ', 1, 50)
                case 5:
                    tipo_id = validar_menu('''
                        Seleccione el tipo de usuario:
                        1. Residente
                        2. Administrador
                    ''', 1, 2)
                    elemento['tipo'] = transformar_tipo(tipo_id)
                case 6:
                    print('Operación cancelada.')
                    return
            
            guardar(NOMBRE_ARCHIVO, registros)
            print('DATO ACTUALIZADO CORRECTAMENTE!')
            return
    
    print(f'No se encontró el usuario con ID {id_usuario}.')


def eliminar_usuario():
    registros = cargar(NOMBRE_ARCHIVO)
    if not registros:
        print('No hay usuarios registrados.')
        return
    
    listar_usuario()
    id_usuario = validar_entero('Ingrese el id del usuario a eliminar: ')
    
    for elemento in registros:
        if elemento.get('id') == id_usuario:
            nombre = elemento.get('nombre', 'Usuario')
            print(f'El usuario "{nombre}" ha sido eliminado del sistema.')
            registros.remove(elemento)
            guardar(NOMBRE_ARCHIVO, registros)
            return
    
    print(f'No se encontró el usuario con ID {id_usuario}.')
