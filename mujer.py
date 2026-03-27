from paciente import Paciente

class PacienteMujer(Paciente):


    def calcular_tmb(self):
        tmb = (10 * self.peso) + (6.25 * (self.talla*100)) - (5 * self.edad) - 161
        return tmb
