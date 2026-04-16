import os
import json


def cargar(nombre_archivo):
    if not os.path.exists(nombre_archivo):
        return []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        print(f'Error: el archivo "{nombre_archivo}" está corrupto o tiene formato inválido.')
        return []


def guardar(nombre_archivo, lista_datos):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(lista_datos, archivo, indent=4, ensure_ascii=False)
    except OSError:
        print(f'Error: no se pudo guardar el archivo "{nombre_archivo}". Verifique permisos o espacio en disco.')


def generar_id(datos):
    if not datos:
        return 1
    ultimo_id = datos[-1].get("id")
    if not isinstance(ultimo_id, int):
        print('Advertencia: el último registro no tiene un "id" válido. Se asignará el ID 1.')
        return 1
    return ultimo_id + 1
