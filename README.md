# Clinical Nutritional Calculator

A clinical nutritional calculator built in Python. Performs anthropometric evaluation, body composition analysis (Frisancho 1981), and energy requirement calculations. Outputs results to console.

Developed based on real clinical practice experience at Hospital Hernán Henríquez Aravena (HHHA), Temuco, Chile.

## Features

- Body Mass Index (BMI) calculation and classification
- Body frame size (height-to-wrist ratio)
- Ideal, minimum, maximum, and adjusted weight
- Basal Metabolic Rate (BMR) using Mifflin-St Jeor equation
- Total Energy Expenditure (TEE) using activity and stress factors
- Arm composition analysis:
  - MAMC — Mid-Arm Muscle Circumference (CMB)
  - AMA — Arm Muscle Area (AMB)
  - AFA — Arm Fat Area (AGB)
- Percentile classification based on age and sex (Frisancho 1981 tables)
- Adequacy percentage relative to 50th percentile reference

## Tech Stack

- Python 3.10+
- Object-oriented design: base class `Paciente` with `PacienteHombre` and `PacienteMujer` subclasses
- No external dependencies

## How to Run

1. Make sure you have Python 3.10+ installed
2. Clone the repository:
```
git clone https://github.com/Psmithortiz/calculadora_nutricional.git
```
3. Run the calculator:
```
python main.py
```

## References

- Frisancho, A.R. (1981). New norms of upper limb fat and muscle areas for assessment of nutritional status. *Am J Clin Nutr*, 34, 2540-2545.
- Mifflin, M.D. et al. (1990). A new predictive equation for resting energy expenditure in healthy individuals. *Am J Clin Nutr*, 51(2), 241-247.
- Pinheiro Fernandes et al. (2019). Manual de Evaluación Nutricional. Universidad del Desarrollo, Chile.