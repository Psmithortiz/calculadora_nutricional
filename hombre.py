from paciente import Paciente
from tablas_frisancho import AMB_HOMBRE, AGB_HOMBRE, obtener_tabla_edad

class PacienteHombre(Paciente):
    def __init__(self, nombre, edad, peso, talla, carpo, cb, pct_mm,
                 factor_actividad, factor_estres):
        super().__init__(nombre, edad, peso, talla, carpo, cb, pct_mm,
                         factor_actividad, factor_estres)
        self.tabla_amb = obtener_tabla_edad(AMB_HOMBRE, self.edad)
        self.tabla_agb = obtener_tabla_edad(AGB_HOMBRE, self.edad)

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
