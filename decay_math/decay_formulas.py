import numpy as np
import matplotlib.pyplot as plt
import math

def decay_constant(half_life):
    return math.log(2) / half_life

def remaining_quantity(N0, decay_const, time):
    return N0 * math.exp(-decay_const * time)

def find_time(N0, N, half_life):
    lam = decay_constant(half_life)
    return math.log(N0 / N) / lam

def estimate_half_life(N0, N, t):
    return t * math.log(2) / math.log(N0 / N)

def run_decay_cli():
    print("\n📉 Nuclear Decay Problem Solver")
    print("----------------------------------")
    print("1. Find remaining quantity after time")
    print("2. Estimate age from remaining sample")
    print("3. Find decay constant from half-life")
    print("4. Estimate half-life from measurements")
    mode = input("Select mode (1-4): ")

    try:
        if mode == "1":
            N0 = float(input("Initial quantity/activity (N₀): "))
            half_life = float(input("Half-life (years): "))
            t = float(input("Elapsed time (years): "))

            lam = decay_constant(half_life)
            N = remaining_quantity(N0, lam, t)
            print(f"\n Remaining quantity after {t} years: {N:.3f}")
            print(f"Decay constant λ: {lam:.5f} 1/year")

            # Plot
            times = np.linspace(0, t if t > 5 else half_life * 5, 200)
            values = remaining_quantity(N0, lam, times)
            plt.plot(times, values, label=f"T½ = {half_life} yr")
            plt.title("Radioactive Decay Over Time")
            plt.xlabel("Time (years)")
            plt.ylabel("Remaining (N)")
            plt.grid(True, linestyle="--", alpha=0.6)
            plt.legend()
            plt.tight_layout()
            plt.show()

        elif mode == "2":
            N0 = float(input("Original amount (N₀): "))
            N = float(input("Remaining amount (N): "))
            half_life = float(input("Half-life (years): "))
            t = find_time(N0, N, half_life)
            print(f"\n Estimated age of sample: {t:.2f} years")

        elif mode == "3":
            hl = float(input("Enter half-life (years): "))
            lam = decay_constant(hl)
            print(f"Decay constant λ: {lam:.5f} 1/year")

        elif mode == "4":
            N0 = float(input("Initial quantity (N₀): "))
            N = float(input("Remaining quantity (N): "))
            t = float(input("Elapsed time (years): "))
            hl = estimate_half_life(N0, N, t)
            print(f"Estimated half-life: {hl:.3f} years")

        else:
            print("Invalid selection.")

    except ValueError:
        print(" Please enter valid numbers.")

if __name__ == "__main__":
    run_decay_cli()