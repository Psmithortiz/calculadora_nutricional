import math
from abc import ABC, abstractmethod


class Paciente(ABC):
    def __init__(self, nombre, edad, peso, talla, carpo, cb, pct_mm,
                 factor_actividad, factor_estres=1.0):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.factor_actividad = factor_actividad
        self.factor_estres = factor_estres
        self.carpo = carpo
        self.pct_mm = pct_mm
        self.cb = cb

    @abstractmethod
    def calcular_tmb(self):
        pass

    @abstractmethod
    def clasificar_contextura(self):
        pass

    def calcular_imc(self):
        return self.peso / self.talla ** 2

    def clasificar_imc(self):
        imc = self.calcular_imc()
        if imc >= 30:
            return "Obesidad"
        elif imc >= 25:
            return "Sobrepeso"
        elif imc >= 18.5:
            return "Eutrofico"
        else:
            return "Bajo peso"

    def calcular_get(self):
        return self.calcular_tmb() * self.factor_actividad * self.factor_estres

    def calcular_contextura(self):
        return (self.talla * 100) / self.carpo

    def calcular_imc_ideal_contextura(self):
        contextura = self.clasificar_contextura()
        match contextura:
            case "Pequeña":
                return 20 if self.edad < 65 else 23
            case "Mediana":
                return 23 if self.edad < 65 else 26
            case "Grande":
                return 25 if self.edad < 65 else 28
            case _:
                raise ValueError(f"Contextura no reconocida: {contextura}")

    def calcular_peso_ideal(self):
        return self.calcular_imc_ideal_contextura() * self.talla ** 2

    def calcular_peso_minimo(self):
        return 18.5 * self.talla ** 2

    def calcular_peso_maximo(self):
        return 24.9 * self.talla ** 2

    def calcular_peso_ajustado(self):
        peso_ideal = self.calcular_peso_ideal()
        return peso_ideal + 0.25 * (self.peso - peso_ideal)

    def calcular_cmb(self):
        return self.cb - (math.pi * (self.pct_mm / 10))

    def calcular_amb(self):
        return self.calcular_cmb() ** 2 / (4 * math.pi)

    def calcular_agb(self):
        return (self.cb ** 2 / (4 * math.pi)) - self.calcular_amb()
