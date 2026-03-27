from paciente import Paciente

class PacienteHombre(Paciente):


    def calcular_tmb(self):
        tmb = (10 * self.peso) + (6.25 * (self.talla*100)) - (5 * self.edad) + 5
        return tmb
