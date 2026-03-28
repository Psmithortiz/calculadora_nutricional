from paciente import Paciente


class PacienteHombre(Paciente):

    def calcular_tmb(self):
        return (10 * self.peso) + (6.25 * (self.talla * 100)) - (5 * self.edad) + 5

    def clasificar_contextura(self):
        indice = self.calcular_contextura()
        if indice > 10.4:
            return "Pequeña"
        elif indice >= 9.6:
            return "Mediana"
        else:
            return "Grande"
