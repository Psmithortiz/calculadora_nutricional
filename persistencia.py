import json

from factory import construir_paciente


def guardar_pacientes(pacientes, archivo):
    lista_dicts = [p.to_dict() for p in pacientes]
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista_dicts, f, indent=4, ensure_ascii=False)


def cargar_pacientes(archivo):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        pacientes = [construir_paciente(dato) for dato in datos]
        return pacientes
    except FileNotFoundError:
        print(f"No se pudo cargar el archivo {archivo}")
        return []