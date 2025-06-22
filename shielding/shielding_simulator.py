# shielding_simulator.py

shielding_factors = {
    "Paper": 0.05,
    "Aluminum": 0.3,
    "Lead": 0.95,
    "Concrete": 0.85,
    "Water": 0.8,
    "Borated Polyethylene": 0.9,
    "Polycarbonate": 0.4,
    "Glass": 0.6,
    "Steel": 0.88,
    "Air": 0.01,
    "Graphite": 0.5
}

def calculate_shielded_dose(initial_dose, material):
    material = material.title()
    if material not in shielding_factors:
        raise ValueError(f"Material '{material}' not supported.")
    blocked_fraction = shielding_factors[material]
    transmitted_dose = initial_dose * (1 - blocked_fraction)
    return transmitted_dose, blocked_fraction