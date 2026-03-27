from paciente import Paciente

class PacienteMujer(Paciente):
    def __init__(self, nombre, edad, peso, talla, factor_actividad, factor_estres=1.0):
        super().__init__(nombre, edad, peso, talla, factor_actividad, factor_estres)

    def calcular_tmb(self):
        tmb = (10 * self.peso) + (6.25 * (self.talla*100)) - (5 * self.edad) - 161
        return tmb
