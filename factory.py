from hombre import PacienteHombre
from mujer import PacienteMujer


def construir_paciente(datos):
    if datos["sexo"] == "MASCULINO":
        return PacienteHombre(**datos)
    else:
        return PacienteMujer(**datos)
