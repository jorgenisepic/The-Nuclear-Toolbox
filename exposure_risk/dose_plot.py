# dose_plot.py

import matplotlib.pyplot as plt

# Predefined radiation exposure levels (in mSv)
exposure_levels = {
    "Dental X-ray": 0.005,
    "Chest X-ray": 0.1,
    "CT Scan (Chest)": 7.0,
    "Natural Background (Annual)": 2.4,
    "Flight (NY to Tokyo)": 0.2,
    "Chernobyl Worker (Acute)": 1000,
    "Fatal Dose": 4000
}

def plot_exposure_levels():
    activities = list(exposure_levels.keys())
    doses = list(exposure_levels.values())

    plt.figure(figsize=(10, 6))
    bars = plt.barh(activities, doses, color='tomato')
    plt.xlabel("Dose (mSv)")
    plt.title("Radiation Exposure Levels from Various Sources")
    plt.xscale('log')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Add labels to each bar
    for bar, dose in zip(bars, doses):
        plt.text(dose * 1.05, bar.get_y() + bar.get_height()/2,
                 f"{dose} mSv", va='center')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_exposure_levels()