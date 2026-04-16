from validaciones import validar_entero, validar_texto
from datetime import date
from gestionar_json import cargar, guardar
from logs import historial


ESTADOS_HERRAMIENTA = {
    1: 'Activa',
    2: 'En reparación',
    3: 'Fuera de servicio'
}

TIPOS_USUARIO = {
    1: 'Residente',
    2: 'Administrador'
}

ARCHIVO_HERRAMIENTAS = 'herramientas.json'


def transformar_estado(estado_id):
    return ESTADOS_HERRAMIENTA.get(estado_id, 'Estado desconocido')


def transformar_tipo(tipo_id):
    return TIPOS_USUARIO.get(tipo_id, 'Tipo desconocido')


def solicitar_fecha_inicio():
    while True:
        anio = validar_entero('Ingrese el año de la solicitud: ')
        mes = validar_entero('Ingrese el mes (1-12): ')
        dia = validar_entero('Ingrese el día: ')
        try:
            fecha = date(anio, mes, dia)
            return fecha
        except ValueError:
            print('Error: la fecha ingresada no es válida. Intente nuevamente.')


def _hay_stock_suficiente(herramienta, cantidad_solicitada):
    return herramienta.get('cantidad', 0) >= cantidad_solicitada


def gestionar(id_herramienta, elemento):
    registros = cargar(ARCHIVO_HERRAMIENTAS)
    cantidad_solicitada = elemento.get('cantidad', 0)

    for herramienta in registros:
        if herramienta.get('id') == id_herramienta:
            if _hay_stock_suficiente(herramienta, cantidad_solicitada):
                herramienta['cantidad'] -= cantidad_solicitada
                elemento['estado'] = 'Aceptada'
                elemento['observaciones'] = 'Solicitud aprobada. No olvides devolver la herramienta en la fecha indicada.'
                print(f'Solicitud aceptada. Stock restante: {herramienta["cantidad"]} unidad(es).')
                guardar(ARCHIVO_HERRAMIENTAS, registros)
            else:
                elemento['estado'] = 'Rechazada'
                elemento['observaciones'] = 'Solicitud rechazada: stock insuficiente.'
                print('No hay suficiente stock para aprobar esta solicitud.')
                historial('Solicitud de préstamo rechazada por stock insuficiente.')
            return


def rechazar(elemento):
    elemento['observaciones'] = validar_texto(
        'Ingrese el motivo del rechazo: ', 1, 100
    )
    elemento['estado'] = 'Rechazada'