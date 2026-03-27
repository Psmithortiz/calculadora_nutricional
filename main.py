from hombre import PacienteHombre
from mujer import PacienteMujer


def pedir_numero(mensaje, tipo):
    while True:
        try:
            return tipo(input(mensaje))
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
        sexo = input("Ingrese el sexo (Masculino/Femenino): ").upper()
        if sexo == "MASCULINO" or sexo == "FEMENINO":
            return sexo
        print("Sexo incorrecto, ingrese Masculino o Femenino")


def main():
    nombre = input("Ingrese el nombre: ")
    sexo = pedir_sexo()
    edad = pedir_numero("Ingrese la edad: ", int)
    peso = pedir_numero("Ingrese el peso (KG): ", float)
    talla = pedir_talla("Ingrese el talla (MTS): ")
    factor_actividad = pedir_numero("Ingrese el factor de actividad: ", float)
    factor_estres = pedir_numero("Ingrese el factor de estres: ", float)
    carpo = pedir_numero("Ingrese el carpo: ", float)

    if sexo == "MASCULINO":
        p = PacienteHombre(nombre, edad, peso, talla, carpo, factor_actividad, factor_estres)

    else:
        p = PacienteMujer(nombre, edad, peso, talla, carpo, factor_actividad, factor_estres)


#REPORTE
    print("========================================")
    print("EVALUACION NUTRICIONAL - " + p.nombre)
    print("========================================")
    print("ANTROPOMETRIA")
    print(f" IMC:   {p.calcular_imc():.2f}" " -> " + p.clasificar_imc())
    print(f" Contextura: {p.clasificar_contextura()}  Indice:  {p.calcular_contextura():.1f}")
    print("")
    print("PESOS DE REFERENCIA")
    print(f" IMC ideal (contextura): {p.calcular_imc_ideal_contextura()}")
    print(f" Peso ideal:    {p.calcular_peso_ideal():.2f}")
    print(f" Peso maximo:   {p.calcular_peso_maximo():.2f}")
    print(f" Peso minimo:   {p.calcular_peso_minimo():.2f}")
    print(f" Peso ajustado: {p.calcular_peso_ajustado():.2f}")
    print("")
    print("REQUERIMIENTO ENERGETICO")
    print(f" TMB:           {p.calcular_tmb():.1f} kcal")
    print(f" GET(Mifflin):  {p.calcular_get():.1f} kcal")





if __name__ == "__main__":
    main()
