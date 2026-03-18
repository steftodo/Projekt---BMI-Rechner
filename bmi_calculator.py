"""
BMI-Rechner - Berechnungslogik
Autor: [Mustafa Sipahi / Stefan Todorovski]
Datum: [14.03.2026]
Kurzbeschreibung: Enthält die BMI-Berechnungsfunktionen und Datenhaltung
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
# Globale Liste für BMI-Verlauf (speichert die letzten 10 Berechnungen)
bmi_verlauf = []

def bmi_berechnen(groesse, gewicht, name="Unbekannt"):
    """
    Berechnet den BMI aus Größe und Gewicht
    Parameter:
        groesse: float - Körpergröße in Metern
        gewicht: float - Gewicht in Kilogramm
        name: str - Name für den Eintrag
    Rückgabewert: dict - BMI-Ergebnis mit allen Informationen
    """
    # BMI-Formel: Gewicht / (Größe in Metern)²
    bmi_wert = gewicht / (groesse ** 2)
    
    # BMI-Kategorie bestimmen (Verzweigung mit if/elif)
    if bmi_wert < 18.5:
        kategorie = "Untergewicht"
        empfehlung = "✅ Tipp: Achten Sie auf ausgewogene Mahlzeiten mit ausreichend Nährstoffen."
    elif bmi_wert < 25:
        kategorie = "Normalgewicht"
        empfehlung = "✅ Tipp: Super! Halten Sie Ihr Gewicht mit gesunder Ernährung und Bewegung."
    elif bmi_wert < 30:
        kategorie = "Übergewicht"
        empfehlung = "✅ Tipp: Regelmäßige Bewegung und eine ausgewogene Ernährung können helfen."
    elif bmi_wert < 35:
        kategorie = "Adipositas Grad I"
        empfehlung = "✅ Tipp: Konsultieren Sie einen Arzt für einen individuellen Ernährungsplan."
    elif bmi_wert < 40:
        kategorie = "Adipositas Grad II"
        empfehlung = "✅ Tipp: Medizinische Beratung wird empfohlen. Kleine Schritte zählen!"
    else:
        kategorie = "Adipositas Grad III"
        empfehlung = "✅ Tipp: Suchen Sie unbedingt ärztliche Unterstützung für Ihre Gesundheit."
    
    # Ergebnis als Dictionary (Rückgabewert!)
    ergebnis = {
        'name': name,
        'wert': round(bmi_wert, 1),
        'kategorie': kategorie,
        'empfehlung': empfehlung
    }
    
    # Zum Verlauf hinzufügen (am Anfang einfügen)
    bmi_verlauf.insert(0, ergebnis)
    
    # Verlauf auf 10 Einträge begrenzen
    if len(bmi_verlauf) > 10:
        bmi_verlauf.pop()
    
    return ergebnis

def verlauf_anzeigen():
    """
    Gibt den BMI-Verlauf zurück
    Rückgabewert: list - Liste der letzten BMI-Berechnungen
    """
    return bmi_verlauf

def gesundheitstipp(kategorie):
    """
    Gibt einen allgemeinen Gesundheitstipp basierend auf der Kategorie
    Parameter:
        kategorie: str - Die BMI-Kategorie
    Rückgabewert: str - Ein Gesundheitstipp
    """
    tipps = {
        "untergewicht": "Essen Sie nährstoffreiche Lebensmittel und führen Sie ein Ernährungstagebuch.",
        "normal": "Großartig! Bleiben Sie aktiv und achten Sie auf ausgewogene Mahlzeiten.",
        "übergewicht": "Integrieren Sie mehr Bewegung in den Alltag, z.B. Treppen statt Aufzug.",
        "adipositas": "Konsultieren Sie einen Ernährungsberater und setzen Sie sich realistische Ziele."
    }
    
    # Standard-Tipp für nicht gefundene Kategorien
    return tipps.get(kategorie, "Achten Sie allgemein auf eine gesunde Lebensweise mit ausreichend Bewegung.")
