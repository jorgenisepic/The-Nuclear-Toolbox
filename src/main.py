from exposure.exposure_calc import run_exposure_cli
from decay_math.decay_formulas import run_decay_cli

def main():
    print("\n📘 Nuclear Engineering Toolkit")
    print("1. Radioactive Decay Calculator")
    print("2. Radiation Exposure Estimator")

    choice = input("Choose a module (1-2): ")

    if choice == "1":
        run_decay_cli()
    elif choice == "2":
        run_exposure_cli()
    else:
        print("Invalid selection.")

if __name__ == "__main__":
    main()