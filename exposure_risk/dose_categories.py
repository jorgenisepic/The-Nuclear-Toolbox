# dose_categories.py

def categorize_dose(dose_mSv: float):
    """
    Categorizes the dose and returns a tuple:
    (category_name, description, emoji/icon, color)

    Example:
    categorize_dose(0.05)
    → ("Very Low", "No health risk", "🟢", "green")
    """
    if dose_mSv <= 0.1:
        return (
            "Very Low",
            "Typical background radiation or minor diagnostics. No health risk.",
            "🟢",
            "green"
        )
    elif dose_mSv <= 10:
        return (
            "Low",
            "Comparable to X-rays or flights. Low long-term risk.",
            "🟡",
            "yellow"
        )
    elif dose_mSv <= 100:
        return (
            "Moderate",
            "Occupational level. Slight increased cancer risk over years.",
            "🟠",
            "orange"
        )
    elif dose_mSv <= 1000:
        return (
            "High",
            "Acute exposure zone. Risk of symptoms, seek evaluation.",
            "🔴",
            "red"
        )
    else:
        return (
            "Extreme",
            "Dangerous or potentially fatal dose. Emergency situation.",
            "☠️",
            "darkred"
        )