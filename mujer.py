from paciente import Paciente
from tablas_frisancho import AMB_MUJER, AGB_MUJER, obtener_tabla_edad

class PacienteMujer(Paciente):
    def __init__(self, nombre, edad, peso, talla, carpo, cb, pct_mm,
                 factor_actividad, factor_estres=1.0):
        super().__init__(nombre, edad, peso, talla, carpo, cb, pct_mm,
                         factor_actividad, factor_estres)
        self.tabla_amb = obtener_tabla_edad(AMB_MUJER, self.edad)
        self.tabla_agb = obtener_tabla_edad(AGB_MUJER, self.edad)

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
