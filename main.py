from hombre import PacienteHombre
from mujer import PacienteMujer

nombre = input("Ingrese el nombre: ")

exceptMesg = "Debe ingresar un número válido"

while True:
    sexo = input("Ingrese el sexo (Masculino/Femenino): ").upper()
    if sexo == "MASCULINO" or sexo == "FEMENINO":
        break
    print("Sexo incorrecto, ingrese Masculino o Femenino")

while True:
    try:
        edad = int(input("Edad : "))
        break
    except ValueError:
        print(exceptMesg)
while True:
    try:
        peso = float(input("Peso (kg): "))
        break
    except ValueError:
        print(exceptMesg)
while True:
    try:
        talla = float(input("Talla (mt): "))
        if not (1.0 <= talla <= 2.5):
            print("Talla fuera de rango. Ingrese en metros (ej: 1.75)")
            continue
        break
    except ValueError:
        print(exceptMesg)
while True:
    try:
        factor_actividad = float(input("Factor actividad: "))
        break
    except ValueError:
        print(exceptMesg)
while True:
    try:
        factor_estres = float(input("Factor estres: "))
        break
    except ValueError:
        print(exceptMesg)

if sexo == "MASCULINO":
    p = PacienteHombre(nombre, edad, peso, talla, factor_actividad, factor_estres)

else:
    p = PacienteMujer(nombre, edad, peso, talla, factor_actividad, factor_estres)


print(f"IMC: {p.calcular_imc():.2f}")
print(f"Clasificación: {p.clasificar_imc()}")
print(f"TMB: {p.calcular_tmb():.1f} kcal")
print(f"GET(Mifflin-St Jeor): {p.calcular_get():.1f} kcal")