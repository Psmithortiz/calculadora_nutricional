# Clinical Nutritional Calculator

A clinical nutritional calculator built in Python. Performs anthropometric evaluation, body composition analysis (Frisancho 1981), and energy requirement calculations via an interactive CLI menu.

Developed based on real clinical practice experience at Hospital Hernán Henríquez Aravena (HHHA), Temuco, Chile.

## Features

- Interactive menu: add, view, and delete patients
- JSON persistence: patient data is saved and loaded automatically between sessions
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

## Project Structure

```
main.py              # Entry point: loads data, launches menu
menu.py              # Interactive menu, input handling, report display
paciente.py          # Abstract base class with shared calculations
hombre.py            # PacienteHombre subclass (male-specific logic)
mujer.py             # PacienteMujer subclass (female-specific logic)
factory.py           # Factory function to build the correct subclass
persistencia.py      # JSON save/load functions
tablas_frisancho.py  # Frisancho 1981 reference tables and classification
```

## Tech Stack

- Python 3.10+ (required for match/case syntax)
- Object-oriented design: abstract base class `Paciente` with `PacienteHombre` and `PacienteMujer` subclasses
- Factory pattern for patient construction
- JSON persistence with UTF-8 encoding
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

## Disclaimer

Patient data is stored in a local JSON file without encryption or access control. This persistence layer was implemented purely as a learning exercise for JSON file handling in Python and is **not suitable for real clinical use**. In a production environment, patient data must comply with applicable data protection regulations.

## References

- Frisancho, A.R. (1981). New norms of upper limb fat and muscle areas for assessment of nutritional status. *Am J Clin Nutr*, 34, 2540-2545.
- Mifflin, M.D. et al. (1990). A new predictive equation for resting energy expenditure in healthy individuals. *Am J Clin Nutr*, 51(2), 241-247.
- Pinheiro Fernandes et al. (2019). Manual de Evaluación Nutricional. Universidad del Desarrollo, Chile.