from collections import Counter
from gestionar_json import cargar
from validaciones import validar_menu, validar_entero


def _imprimir_herramienta(elemento):
    print(f'''
        ****************************
        ID:             {elemento.get('id', 'No encontrado')}
        Nombre:         {elemento.get('nombre', 'No encontrado')}
        Categoría:      {elemento.get('categoria', {}).get('categoria', 'No encontrado')}
        Cantidad:       {elemento.get('cantidad', 'No encontrado')}
        Estado:         {elemento.get('estado', 'No encontrado')}
        Precio:         {elemento.get('precio', 'No encontrado')}
    ''')


def _imprimir_prestamo(elemento):
    print(f'''
        ****************************
        ID:              {elemento.get('id', 'No encontrado')}
        Usuario:         {elemento.get('usuario', {}).get('nombre', 'No encontrado')}
        ID Usuario:      {elemento.get('usuario', {}).get('id', 'No encontrado')}
        Herramienta:     {elemento.get('herramienta', {}).get('nombre', 'No encontrado')}
        ID Herramienta:  {elemento.get('herramienta', {}).get('id', 'No encontrado')}
        Fecha Inicio:    {elemento.get('fecha_inicio', 'No encontrado')}
        Fecha Entrega:   {elemento.get('fecha_final', 'No encontrado')}
        Estado:          {elemento.get('estado', 'No encontrado')}
        Observaciones:   {elemento.get('observaciones', 'No encontrado')}
    ''')


def stock_minimo():
    registros = cargar('herramientas.json')
    if not registros:
        print('No hay herramientas registradas.')
        return
    stock = validar_entero('Ingrese el stock mínimo a buscar: ')
    encontrados = [e for e in registros if e.get('cantidad', 0) <= stock]
    if not encontrados:
        print(f'No hay herramientas con stock menor o igual a {stock}.')
        return
    for elemento in encontrados:
        _imprimir_herramienta(elemento)


def activos_completados():
    registros = cargar('prestamos.json')
    if not registros:
        print('No hay préstamos registrados.')
        return

    op = validar_menu('''
        1. En proceso
        2. Completados
    ''', 1, 2)

    if op == 1:
        resultados = [e for e in registros if e.get('estado') == 'En proceso']
        mensaje_vacio = 'No hay préstamos en estado "En proceso".'
    else:
        resultados = [e for e in registros if e.get('estado') in ('Aceptada', 'Rechazada')]
        mensaje_vacio = 'No hay préstamos completados o rechazados.'

    if not resultados:
        print(mensaje_vacio)
        return
    for elemento in resultados:
        _imprimir_prestamo(elemento)


def historial_usuarios():
    registros = cargar('prestamos.json')
    if not registros:
        print('No hay préstamos registrados.')
        return
    id_usuario = validar_entero('Ingrese el ID del usuario: ')
    resultados = [
        e for e in registros
        if e.get('usuario', {}).get('id') == id_usuario
    ]
    if not resultados:
        print(f'No se encontraron préstamos para el usuario con ID {id_usuario}.')
        return
    for elemento in resultados:
        _imprimir_prestamo(elemento)


def herramienta_mas_usada():
    registros = cargar('prestamos.json')
    if not registros:
        print('No hay préstamos registrados.')
        return
    conteo = Counter(p['herramienta']['id'] for p in registros if 'herramienta' in p)
    herramientas = cargar('herramientas.json')
    for herramienta in herramientas:
        cantidad = conteo.get(herramienta['id'], 0)
        if cantidad > 0:
            print(f"{herramienta['id']} - {herramienta['nombre']}: {cantidad} préstamo(s)")


def usuario_mas_usado():
    registros = cargar('prestamos.json')
    if not registros:
        print('No hay préstamos registrados.')
        return
    conteo = Counter(p['usuario']['id'] for p in registros if 'usuario' in p)
    usuarios = cargar('usuarios.json')
    for usuario in usuarios:
        cantidad = conteo.get(usuario['id'], 0)
        if cantidad > 0:
            print(f"{usuario['id']} - {usuario['nombre']} {usuario['apellido']}: {cantidad} préstamo(s)")
