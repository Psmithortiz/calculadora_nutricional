from paciente import Paciente


class PacienteMujer(Paciente):

    def calcular_tmb(self):
        return (10 * self.peso) + (6.25 * (self.talla * 100)) - (5 * self.edad) - 161

    def clasificar_contextura(self):
        indice = self.calcular_contextura()
        if indice > 11:
            return "Pequeña"
        elif indice >= 10.1:
            return "Mediana"
        else:
            return "Grande"
