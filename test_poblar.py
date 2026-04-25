"""Script de prueba: pobla pacientes.json con datos de ejemplo."""

from factory import construir_paciente
from persistencia import guardar_pacientes

ARCHIVO_PACIENTES = "pacientes.json"

datos_prueba = [
    {"nombre": "Juan Pérez", "sexo": "MASCULINO", "edad": 30, "peso": 75.0,
     "talla": 1.75, "factor_actividad": 1.3, "factor_estres": 1.0,
     "carpo": 10.5, "cb": 30.0, "pct_mm": 12.0},

    {"nombre": "María López", "sexo": "FEMENINO", "edad": 25, "peso": 60.0,
     "talla": 1.62, "factor_actividad": 1.5, "factor_estres": 1.0,
     "carpo": 9.8, "cb": 26.0, "pct_mm": 18.0},

    {"nombre": "Carlos Muñoz", "sexo": "MASCULINO", "edad": 55, "peso": 90.0,
     "talla": 1.70, "factor_actividad": 1.2, "factor_estres": 1.2,
     "carpo": 11.0, "cb": 34.0, "pct_mm": 20.0},

    {"nombre": "Ana Torres", "sexo": "FEMENINO", "edad": 70, "peso": 52.0,
     "talla": 1.55, "factor_actividad": 1.2, "factor_estres": 1.0,
     "carpo": 9.5, "cb": 24.0, "pct_mm": 15.0},

    {"nombre": "Pedro Soto", "sexo": "MASCULINO", "edad": 42, "peso": 110.0,
     "talla": 1.80, "factor_actividad": 1.4, "factor_estres": 1.0,
     "carpo": 10.0, "cb": 36.0, "pct_mm": 25.0},
]

pacientes = [construir_paciente(d) for d in datos_prueba]
guardar_pacientes(pacientes, ARCHIVO_PACIENTES)
print(f"{len(pacientes)} pacientes guardados en {ARCHIVO_PACIENTES}")