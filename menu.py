from factory import construir_paciente
from persistencia import guardar_pacientes
from tablas_frisancho import CLASIFICACION_MUSCULAR, CLASIFICACION_GRASA, clasificar_percentil

ARCHIVO_PACIENTES = "pacientes.json"
SEXOS = ("MASCULINO", "FEMENINO")


def pedir_numero(mensaje, tipo, minimo=None, maximo=None):
    while True:
        try:
            valor = tipo(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número válido")


def pedir_talla(mensaje):
    while True:
        try:
            talla = float(input(mensaje))
            if not (1.0 <= talla <= 2.5):
                print("Talla fuera de rango. Ingrese en metros (ej: 1.75)")
                continue
            return talla
        except ValueError:
            print("Debe ingresar un número válido")


def pedir_sexo():
    while True:
        sexo = input(f"Ingrese el sexo ({"/".join(SEXOS)}): ").upper().strip()
        if sexo in SEXOS:
            return sexo
        print(f"Sexo incorrecto, ingrese ({"/".join(SEXOS)})")


def seccion(titulo):
    print(f"\n{titulo:-^50}")


def pedir_datos():
    nombre = input("Ingrese el nombre: ").strip().title()
    sexo = pedir_sexo()
    edad = pedir_numero("Ingrese la edad (18-90 años): ", int, 18, 90)
    peso = pedir_numero("Ingrese el peso (KG): ", float, 1.0)
    talla = pedir_talla("Ingrese la talla (MTS): ")
    factor_actividad = pedir_numero("Ingrese el factor de actividad: ", float, 1)
    factor_estres = pedir_numero("Ingrese el factor de estres: ", float, 1)
    carpo = pedir_numero("Ingrese el carpo: ", float, 6)
    cb = pedir_numero("Ingrese circunferencia braquial (CM): ", float, 7)
    pct_mm = pedir_numero("Ingrese el pliegue cutaneo tricipital (mm): ", float, 2)
    return {
        "nombre": nombre,
        "sexo": sexo,
        "edad": edad,
        "peso": peso,
        "talla": talla,
        "factor_actividad": factor_actividad,
        "factor_estres": factor_estres,
        "carpo": carpo,
        "cb": cb,
        "pct_mm": pct_mm,
    }


def seleccionar_paciente(pacientes, accion):
    if not pacientes:
        print("No hay pacientes registrados")
        return
    while True:
        print("\n" + "-" * 40)
        print("  LISTA DE PACIENTES")
        print("-" * 40)
        try:
            for i, paciente in enumerate(pacientes):
                print(f"{i + 1}. {paciente.nombre}")
            print("Escriba X para salir")
            print("-" * 40)
            opcion = input("Seleccione un paciente: ").upper().strip()
            if opcion == "X":
                break
            else:
                accion(pacientes[int(opcion) - 1])
                break
        except(ValueError, IndexError):
            print("Opcion invalida")


def reporte(p):
    amb = p.calcular_amb()
    agb = p.calcular_agb()

    print("=" * 50)
    print(f"{'EVALUACION NUTRICIONAL - ' + p.nombre:^50}")
    print("=" * 50)

    seccion(" ANTROPOMETRIA ")
    print(f"  IMC:          {p.calcular_imc():.2f} -> {p.clasificar_imc()}")
    print(f"  Contextura:   {p.clasificar_contextura()} (índice: {p.calcular_contextura():.1f})")

    seccion(" PESOS DE REFERENCIA ")
    print(f"  IMC ideal:    {p.calcular_imc_ideal_contextura()} (contextura {p.clasificar_contextura()})")
    print(f"  Ideal:        {p.calcular_peso_ideal():.2f} kg")
    print(f"  Maximo:       {p.calcular_peso_maximo():.2f} kg")
    print(f"  Minimo:       {p.calcular_peso_minimo():.2f} kg")
    print(f"  Ajustado:     {p.calcular_peso_ajustado():.2f} kg")

    seccion(" REQUERIMIENTO ENERGETICO ")
    print(f"  TMB:          {p.calcular_tmb():.1f} kcal")
    print(f"  GET (Mifflin):{p.calcular_get():.1f} kcal")

    seccion(" COMPOSICION CORPORAL (Frisancho 1981) ")
    print(f"  CMB:          {p.calcular_cmb():.2f} cm")
    print(f"  AMB:          {amb:.2f} cm²")
    print(f"  AGB:          {agb:.2f} cm²")
    print(f"\n  AMB: {clasificar_percentil(amb, p.tabla_amb, CLASIFICACION_MUSCULAR)}")
    print(f"  AGB: {clasificar_percentil(agb, p.tabla_agb, CLASIFICACION_GRASA)}")
    print("=" * 50)


def menu(pacientes):
    while True:
        print("\n" + "=" * 40)
        print("  CALCULADORA NUTRICIONAL v2")
        print("=" * 40)
        print("  1. Agregar paciente")
        print("  2. Ver pacientes")
        print("  3. Eliminar paciente")
        print("  4. Salir")
        print("=" * 40)
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":  # AGREGAR
                datos = pedir_datos()
                paciente = construir_paciente(datos)
                pacientes.append(paciente)
                guardar_pacientes(pacientes, ARCHIVO_PACIENTES)
                reporte(paciente)

            case "2":  # VER PACIENTES
                seleccionar_paciente(pacientes, reporte)

            case "3":  # ELIMINAR
                def eliminar_paciente(paciente):
                    pacientes.remove(paciente)
                    print("Paciente eliminado: ", paciente.nombre)
                    guardar_pacientes(pacientes, ARCHIVO_PACIENTES)

                seleccionar_paciente(pacientes, eliminar_paciente)
            case "4":
                break
            case _:
                print("Opcion invalida")
