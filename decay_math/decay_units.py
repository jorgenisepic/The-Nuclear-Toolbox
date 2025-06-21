# decay_units.py — interactive CLI for decay unit conversions

def years_to_seconds(years):
    return years * 365.25 * 24 * 3600

def seconds_to_years(seconds):
    return seconds / (365.25 * 24 * 3600)

def days_to_seconds(days):
    return days * 24 * 3600

def seconds_to_days(seconds):
    return seconds / (24 * 3600)

def becquerel_to_curie(bq):
    return bq / 3.7e10

def curie_to_becquerel(ci):
    return ci * 3.7e10

def gray_to_sievert(gray, weighting=1):
    return gray * weighting

def sievert_to_gray(sv, weighting=1):
    return sv / weighting

def run_unit_converter():
    print("=== Unit Converter ===")
    print("1. Years → Seconds")
    print("2. Seconds → Years")
    print("3. Days → Seconds")
    print("4. Seconds → Days")
    print("5. Bq → Ci")
    print("6. Ci → Bq")
    print("7. Gy → Sv")
    print("8. Sv → Gy")
    print("9. Exit")

    while True:
        choice = input("\nSelect a conversion (1–9): ")

        if choice == "1":
            y = float(input("Years: "))
            print("→", years_to_seconds(y), "seconds")

        elif choice == "2":
            s = float(input("Seconds: "))
            print("→", seconds_to_years(s), "years")

        elif choice == "3":
            d = float(input("Days: "))
            print("→", days_to_seconds(d), "seconds")

        elif choice == "4":
            s = float(input("Seconds: "))
            print("→", seconds_to_days(s), "days")

        elif choice == "5":
            bq = float(input("Becquerels: "))
            print("→", becquerel_to_curie(bq), "Curies")

        elif choice == "6":
            ci = float(input("Curies: "))
            print("→", curie_to_becquerel(ci), "Becquerels")

        elif choice == "7":
            gy = float(input("Gray: "))
            rf = float(input("Radiation Weighting Factor (usually 1–20): "))
            print("→", gray_to_sievert(gy, rf), "Sieverts")

        elif choice == "8":
            sv = float(input("Sievert: "))
            rf = float(input("Radiation Weighting Factor (usually 1–20): "))
            print("→", sievert_to_gray(sv, rf), "Grays")

        elif choice == "9":
            print("Goodbye.")
            break

        else:
            print("Invalid selection.")

if __name__ == "__main__":
    run_unit_converter()
