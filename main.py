from hombre import PacienteHombre
from mujer import PacienteMujer
from tablas_frisancho import CLASIFICACION_MUSCULAR, CLASIFICACION_GRASA, clasificar_percentil


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
        sexo = input("Ingrese el sexo (Masculino/Femenino): ").upper().strip()
        if sexo == "MASCULINO" or sexo == "FEMENINO":
            return sexo
        print("Sexo incorrecto, ingrese Masculino o Femenino")


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


def construir_paciente(datos):
    sexo = datos.pop("sexo")
    if sexo == "MASCULINO":
        return PacienteHombre(**datos)
    else:
        return PacienteMujer(**datos)


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


def main():
    datos = pedir_datos()
    paciente = construir_paciente(datos)
    reporte(paciente)


if __name__ == "__main__":
    main()
