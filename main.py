from menu import menu, ARCHIVO_PACIENTES
from persistencia import cargar_pacientes


def main():
    pacientes = cargar_pacientes(ARCHIVO_PACIENTES)
    menu(pacientes)

if __name__ == "__main__":
    main()
