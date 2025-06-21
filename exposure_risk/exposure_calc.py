import matplotlib.pyplot as plt

def annual_dose(hours_per_day, rate_uSv_per_hour):
    return hours_per_day * 365 * rate_uSv_per_hour / 1000  # mSv

def plot_annual_dose(daily_mSv):
    days = list(range(1, 366))
    cumulative_dose = [daily_mSv * d for d in days]

    plt.figure(figsize=(9, 4))
    plt.plot(days, cumulative_dose, label="Cumulative Dose (mSv)", color="red")
    plt.axhline(1, color="green", linestyle="--", label="Public Limit (1 mSv)")
    plt.axhline(5, color="orange", linestyle="--", label="Occupational Limit (5 mSv)")
    plt.xlabel("Day of Year")
    plt.ylabel("Total Dose (mSv)")
    plt.title("Radiation Dose Accumulation Over 1 Year")
    plt.ylim(0, max(6, max(cumulative_dose) + 0.5))
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()

def run_exposure_cli():
    while True:
        print("\nRadiation Exposure Calculator")
        print("------------------------------")
        print("1. Estimate safe daily hours (public dose limit)")
        print("2. Compare two worker exposure scenarios")
        print("3. Emergency radiation exposure dose")
        print("4. Exit")

        choice = input("Choose option (1–4): ")

        if choice == "1":
            target_mSv = float(input("Enter max annual dose in mSv (e.g. 1): "))
            rate = float(input("Radiation level in μSv/h: "))
            safe_hours = (target_mSv * 1000) / (365 * rate)
            print(f"Safe daily exposure time: {safe_hours:.2f} hours/day")
            # Plot what happens if user actually works that much
            daily_mSv = safe_hours * rate / 1000
            plot_annual_dose(daily_mSv)

        elif choice == "2":
            print("\nWorker A:")
            a_hours = float(input("Hours/day: "))
            a_rate = float(input("Radiation level in μSv/h: "))
            print("\nWorker B:")
            b_hours = float(input("Hours/day: "))
            b_rate = float(input("Radiation level in μSv/h: "))

            a_dose = annual_dose(a_hours, a_rate)
            b_dose = annual_dose(b_hours, b_rate)

            print(f"\nWorker A Annual Dose: {a_dose:.3f} mSv")
            print(f"Worker B Annual Dose: {b_dose:.3f} mSv")

            winner = "A" if a_dose > b_dose else "B" if b_dose > a_dose else "Neither"
            print(f"{winner} receives more radiation annually." if winner != "Neither" else "Both receive equal doses.")

            # Plot both
            days = list(range(1, 366))
            dose_A = [a_dose / 365 * d for d in days]
            dose_B = [b_dose / 365 * d for d in days]

            plt.figure(figsize=(9, 4))
            plt.plot(days, dose_A, label="Worker A", color="blue")
            plt.plot(days, dose_B, label="Worker B", color="purple")
            plt.axhline(1, color="green", linestyle="--", label="Public Limit")
            plt.axhline(5, color="orange", linestyle="--", label="Worker Limit")
            plt.xlabel("Day of Year")
            plt.ylabel("Cumulative Dose (mSv)")
            plt.title("Dose Comparison: Worker A vs. B")
            plt.grid(True, linestyle="--", alpha=0.4)
            plt.legend()
            plt.tight_layout()
            plt.show()

        elif choice == "3":
            hrs = float(input("Exposure duration (hours): "))
            rate = float(input("Radiation level in μSv/h: "))
            dose = hrs * rate / 1000
            print(f"Estimated Emergency Dose: {dose:.3f} mSv")
            if dose > 10:
                print("High dose. Acute effects possible.")
            elif dose > 1:
                print("Above public limit. Caution advised.")
            else:
                print("Within short-term safety limits.")

            # Show fixed point graph
            plt.figure(figsize=(6, 3))
            plt.bar(["Emergency Dose"], [dose], color="red")
            plt.axhline(1, color="green", linestyle="--", label="Public Limit")
            plt.axhline(5, color="orange", linestyle="--", label="Worker Limit")
            plt.ylabel("Dose (mSv)")
            plt.title("Emergency Radiation Exposure")
            plt.ylim(0, max(6, dose + 1))
            plt.legend()
            plt.tight_layout()
            plt.show()

        elif choice == "4":
            print("Exiting calculator.")
            break

        else:
            print("Invalid option. Please select 1–4.")

if __name__ == "__main__":
    run_exposure_cli()