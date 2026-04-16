from gestionar_txt import guardar_txt
from datetime import datetime

ARCHIVO_HISTORIAL = 'historial.txt'


def historial(mensaje):
    """Registra una acción en el archivo de historial con fecha y hora."""
    fecha = str(datetime.now())
    accion = f'{mensaje} en la fecha de {fecha}'
    print(accion)
    guardar_txt(ARCHIVO_HISTORIAL, accion)

