radiation_types = {
    "alpha": {
        "charge": "+2",
        "mass": "Heavy",
        "penetration": "Low",
        "shielding": "Paper/Skin",
        "danger": "High if inhaled"
    },
    "beta": {
        "charge": "-1",
        "mass": "Light",
        "penetration": "Medium",
        "shielding": "Aluminum",
        "danger": "Can burn skin"
    },
    "gamma": {
        "charge": "0",
        "mass": "None (wave)",
        "penetration": "High",
        "shielding": "Lead/Concrete",
        "danger": "Deep tissue damage"
    },
    "neutron": {
        "charge": "0",
        "mass": "Neutral particle",
        "penetration": "Very High",
        "shielding": "Water/Borated Concrete",
        "danger": "Can activate atoms"
    }
}

def print_radiation_chart():
    print("\n📊 Radiation Types Chart\n")
    print(f"{'Type':<10} {'Charge':<8} {'Mass':<18} {'Penetration':<12} {'Shielding':<25} {'Danger'}")
    print("-" * 90)
    for key, val in radiation_types.items():
        print(f"{key:<10} {val['charge']:<8} {val['mass']:<18} {val['penetration']:<12} {val['shielding']:<25} {val['danger']}")