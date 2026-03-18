"""
BMI Calculator Module
Berechnung des Body Mass Index und Kategorisierung
"""

def calculate_bmi(height, weight):
    """
    Berechnet den BMI.
    Args:
        height (float): Größe in Metern
        weight (float): Gewicht in kg
    Returns:
        float: BMI Wert
    Raises:
        ValueError: Wenn height oder weight <= 0
    """
    if height <= 0 or weight <= 0:
        raise ValueError("Wert muss größer als 0 sein!")
    return round(weight / (height ** 2), 1)

def get_bmi_category(bmi):
    """
    Gibt die BMI-Kategorie basierend auf WHO-Standards zurück.
    """
    if bmi < 18.5:
        return "Untergewicht"
    elif 18.5 <= bmi < 25:
        return "Normalgewicht"
    elif 25 <= bmi < 30:
        return "Übergewicht"
    elif 30 <= bmi < 35:
        return "Adipositas Grad I"
    elif 35 <= bmi < 40:
        return "Adipositas Grad II"
    else:
        return "Adipositas Grad III"

def get_health_tip(category):
    """
    Gibt einen Gesundheitstipp basierend auf der Kategorie.
    """
    tips = {
        "Untergewicht": "Achten Sie auf eine ausgewogene Ernährung und konsultieren Sie einen Arzt.",
        "Normalgewicht": "Halten Sie Ihren Lebensstil bei – Bewegung und gesunde Ernährung sind wichtig.",
        "Übergewicht": "Reduzieren Sie Kalorienaufnahme und erhöhen Sie körperliche Aktivität.",
        "Adipositas Grad I": "Suchen Sie professionelle Hilfe für Gewichtsmanagement.",
        "Adipositas Grad II": "Medizinische Betreuung ist empfohlen.",
        "Adipositas Grad III": "Sofortige medizinische Intervention erforderlich."
    }
    return tips.get(category, "Konsultieren Sie einen Arzt für persönliche Ratschläge.")

class BMICalculator:
    def __init__(self):
        self.history = []

    def add_calculation(self, name, height, weight):
        try:
            bmi = calculate_bmi(height, weight)
            category = get_bmi_category(bmi)
            tip = get_health_tip(category)
            entry = {
                "name": name,
                "height": height,
                "weight": weight,
                "bmi": bmi,
                "category": category,
                "tip": tip
            }
            self.history.append(entry)
            if len(self.history) > 10:
                self.history.pop(0)
            return entry
        except ValueError as e:
            raise e

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []
