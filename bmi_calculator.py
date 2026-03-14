"""
BMI-Rechner - Berechnungslogik
Autor: [Stefan Todorovski, Mustafa Sipahi]
Datum: [14.03.2026]
Kurzbeschreibung: Enthält die BMI-Berechnungsfunktionen und Datenhaltung
"""

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