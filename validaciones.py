def _validar_numero(mensaje, tipo):
   
    nombre_tipo = "entero" if tipo == int else "decimal"
    while True:
        try:
            dato = tipo(input(mensaje))
            if dato <= 0:
                print(f'Error: el número debe ser positivo.')
                continue
            return dato
        except ValueError:
            print(f'Error: solo se admiten números {nombre_tipo}s.')

def validar_entero(mensaje):
        return _validar_numero(mensaje, int)

def validar_decimales(mensaje):
    return _validar_numero(mensaje, float)




def validar_texto(mensaje, cantidad_minima, cantidad_maxima):
   
    dato = input(mensaje).strip()
    while len(dato) < cantidad_minima or len(dato) > cantidad_maxima:
        dato = input(
            f'Error: el texto debe tener entre {cantidad_minima} '
            f'y {cantidad_maxima} caracteres. Intente nuevamente: '
        ).strip()
    return dato


def validar_menu(mensaje, minimo, maximo):
    opcion = validar_entero(mensaje)
    while opcion < minimo or opcion > maximo:
        opcion = validar_entero(
            f'Opción inválida. Ingrese un número entre {minimo} y {maximo}: '
        )
    return opcion