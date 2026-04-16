import os


def cargar_txt(nombre_archivo):
    """Carga el contenido de un archivo de texto."""
    try:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                return archivo.read()
        return ''
    except OSError as e:
        print(f'Error al cargar el archivo "{nombre_archivo}": {e}')
        return ''


def guardar_txt(nombre_archivo, mensaje):
    """Guarda un mensaje al final de un archivo de texto."""
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(mensaje + '\n')
    except OSError as e:
        print(f'Error al guardar en el archivo "{nombre_archivo}": {e}')
