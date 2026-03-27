class Paciente:
    def __init__(self, nombre, edad, peso, talla, factor_actividad, factor_estres=1.0):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.factor_actividad = factor_actividad
        self.factor_estres = factor_estres

    def calcular_imc(self):
        imc = self.peso / self.talla**2
        return imc

    def clasificar_imc(self):
        imc = self.calcular_imc()
        if imc > 29.9:
            return "Obesidad"
        elif imc > 24.9:
            return "Sobrepeso"
        elif imc >= 18.5:
            return "Eutrofico"
        else:
            return "Bajo peso"

    def calcular_get(self):
        gasto_energetico_total = self.calcular_tmb() * self.factor_actividad * self.factor_estres
        return gasto_energetico_total