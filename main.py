"""
Interaktiver BMI-Rechner - Hauptmodul
Autor: [Stefan Todorovski / Mustafa Sipahi]
Datum: [14.03.2026]
Kurzbeschreibung: Hauptprogramm mit Menüführung für den BMI-Rechner
"""

import bmi_calculator as bmi  # Import der BMI-Logik aus der anderen Datei (Modularisierung!)

def zeige_menu():
    """Zeigt das Hauptmenü an"""
    print("\n" + "="*50)
    print(" INTERAKTIVER BMI-RECHNER")
    print("="*50)
    print("1. Neuen BMI berechnen")
    print("2. BMI-Verlauf anzeigen")
    print("3. BMI-Kategorien erklärt")
    print("4. Gesundheits-Tipp anzeigen")
    print("5. Programm beenden")
    print("="*50)

def hole_kommazahl(prompt):
    """
    Holt und validiert eine Kommazahl-Eingabe
    Parameter: prompt - Eingabeaufforderung
    Rückgabewert: float - validierte Zahl
    """
    while True:  # Schleife für wiederholte Eingabe bis Erfolg
        try:  # Fehlerbehandlung mit try/except
            wert = float(input(prompt))
            if wert <= 0:  # Eingabevalidierung
                print("Fehler: Der Wert muss größer als 0 sein!")
                continue
            return wert
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben (z.B. 1.75 oder 70.5)!")

def hole_menueauswahl():
    """
    Holt und validiert die Menüauswahl
    Rückgabewert: int - gültige Menüauswahl (1-5)
    """
    while True:
        try:
            auswahl = int(input("\nIhre Auswahl (1-5): "))
            if 1 <= auswahl <= 5:
                return auswahl
            else:
                print("Fehler: Bitte eine Zahl zwischen 1 und 5 eingeben!")
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben!")

def main():
    """Hauptfunktion des Programms"""
    print("🏋️  Willkommen beim interaktiven BMI-Rechner!")
    print("Berechnen Sie Ihren Body Mass Index und erhalten Sie Gesundheits-Tipps.")
    
    # Hauptschleife für das Menü (while-Schleife)
    while True:
        zeige_menu()
        auswahl = hole_menueauswahl()
        
        # Verzweigung für Menüauswahl (if/elif)
        if auswahl == 1:
            # Neuen BMI berechnen
            print("\n--- Neue BMI-Berechnung ---")
            
            # Eingabe der Körperdaten mit Validierung
            groesse = hole_kommazahl("Ihre Körpergröße in Metern (z.B. 1.75): ")
            gewicht = hole_kommazahl("Ihr Gewicht in Kilogramm (z.B. 70.5): ")
            name = input("Name für diesen Eintrag (optional): ")
            if name.strip() == "":
                name = "Unbekannt"
            
            # BMI berechnen (Aufruf der Funktion aus bmi_calculator)
            ergebnis = bmi.bmi_berechnen(groesse, gewicht, name)
            
            # Ergebnis anzeigen
            print(f"\n📊 BMI-Ergebnis für {ergebnis['name']}:")
            print(f"   BMI-Wert: {ergebnis['wert']:.1f}")
            print(f"   Kategorie: {ergebnis['kategorie']}")
            print(f"   {ergebnis['empfehlung']}")
            
        elif auswahl == 2:
            # BMI-Verlauf anzeigen
            verlauf = bmi.verlauf_anzeigen()
            
            if not verlauf:
                print("\n📭 Noch keine BMI-Berechnungen vorhanden.")
            else:
                print("\n" + "-"*50)
                print(" BMI-VERLAUF (letzte 10 Berechnungen)")
                print("-"*50)
                # for-Schleife für die Ausgabe der Liste
                for i, eintrag in enumerate(verlauf, 1):
                    print(f"{i}. {eintrag['name']}: BMI {eintrag['wert']:.1f} - {eintrag['kategorie']}")
                print("-"*50)
                
        elif auswahl == 3:
            # BMI-Kategorien erklären
            print("\n" + "-"*50)
            print(" BMI-KATEGORIEN (WHO-Standard)")
            print("-"*50)
            print("Untergewicht: < 18.5")
            print("Normalgewicht: 18.5 - 24.9")
            print("Übergewicht: 25.0 - 29.9")
            print("Adipositas Grad I: 30.0 - 34.9")
            print("Adipositas Grad II: 35.0 - 39.9")
            print("Adipositas Grad III: ≥ 40.0")
            print("-"*50)
            
        elif auswahl == 4:
            # Gesundheits-Tipp anzeigen
            print("\nVerfügbare Kategorien: untergewicht, normal, übergewicht, adipositas")
            kategorie = input("Für welche BMI-Kategorie möchten Sie einen Tipp? ").lower()
            tipp = bmi.gesundheitstipp(kategorie)
            print(f"\n💡 Gesundheitstipp: {tipp}")
            
        elif auswahl == 5:
            # Programm beenden
            print("\n👋 Programm wird beendet. Bleiben Sie gesund!")
            break  # beendet die while-Schleife

if __name__ == "__main__":
    main()
import bmi_calculator as bmi  # Import der BMI-Logik aus der anderen Datei (Modularisierung!)

def zeige_menu():
    """Zeigt das Hauptmenü an"""
    print("\n" + "="*50)
    print(" INTERAKTIVER BMI-RECHNER")
    print("="*50)
    print("1. Neuen BMI berechnen")
    print("2. BMI-Verlauf anzeigen")
    print("3. BMI-Kategorien erklärt")
    print("4. Gesundheits-Tipp anzeigen")
    print("5. Programm beenden")
    print("="*50)

def hole_kommazahl(prompt):
    """
    Holt und validiert eine Kommazahl-Eingabe
    Parameter: prompt - Eingabeaufforderung
    Rückgabewert: float - validierte Zahl
    """
    while True:  # Schleife für wiederholte Eingabe bis Erfolg
        try:  # Fehlerbehandlung mit try/except
            wert = float(input(prompt))
            if wert <= 0:  # Eingabevalidierung
                print("Fehler: Der Wert muss größer als 0 sein!")
                continue
            return wert
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben (z.B. 1.75 oder 70.5)!")

def hole_menueauswahl():
    """
    Holt und validiert die Menüauswahl
    Rückgabewert: int - gültige Menüauswahl (1-5)
    """
    while True:
        try:
            auswahl = int(input("\nIhre Auswahl (1-5): "))
            if 1 <= auswahl <= 5:
                return auswahl
            else:
                print("Fehler: Bitte eine Zahl zwischen 1 und 5 eingeben!")
        except ValueError:
            print("Fehler: Bitte eine gültige Zahl eingeben!")

def main():
    """Hauptfunktion des Programms"""
    print("🏋️  Willkommen beim interaktiven BMI-Rechner!")
    print("Berechnen Sie Ihren Body Mass Index und erhalten Sie Gesundheits-Tipps.")
    
    # Hauptschleife für das Menü (while-Schleife)
    while True:
        zeige_menu()
        auswahl = hole_menueauswahl()
        
        # Verzweigung für Menüauswahl (if/elif)
        if auswahl == 1:
            # Neuen BMI berechnen
            print("\n--- Neue BMI-Berechnung ---")
            
            # Eingabe der Körperdaten mit Validierung
            groesse = hole_kommazahl("Ihre Körpergröße in Metern (z.B. 1.75): ")
            gewicht = hole_kommazahl("Ihr Gewicht in Kilogramm (z.B. 70.5): ")
            name = input("Name für diesen Eintrag (optional): ")
            if name.strip() == "":
                name = "Unbekannt"
            
            # BMI berechnen (Aufruf der Funktion aus bmi_calculator)
            ergebnis = bmi.bmi_berechnen(groesse, gewicht, name)
            
            # Ergebnis anzeigen
            print(f"\n📊 BMI-Ergebnis für {ergebnis['name']}:")
            print(f"   BMI-Wert: {ergebnis['wert']:.1f}")
            print(f"   Kategorie: {ergebnis['kategorie']}")
            print(f"   {ergebnis['empfehlung']}")
            
        elif auswahl == 2:
            # BMI-Verlauf anzeigen
            verlauf = bmi.verlauf_anzeigen()
            
            if not verlauf:
                print("\n📭 Noch keine BMI-Berechnungen vorhanden.")
            else:
                print("\n" + "-"*50)
                print(" BMI-VERLAUF (letzte 10 Berechnungen)")
                print("-"*50)
                # for-Schleife für die Ausgabe der Liste
                for i, eintrag in enumerate(verlauf, 1):
                    print(f"{i}. {eintrag['name']}: BMI {eintrag['wert']:.1f} - {eintrag['kategorie']}")
                print("-"*50)
                
        elif auswahl == 3:
            # BMI-Kategorien erklären
            print("\n" + "-"*50)
            print(" BMI-KATEGORIEN (WHO-Standard)")
            print("-"*50)
            print("Untergewicht: < 18.5")
            print("Normalgewicht: 18.5 - 24.9")
            print("Übergewicht: 25.0 - 29.9")
            print("Adipositas Grad I: 30.0 - 34.9")
            print("Adipositas Grad II: 35.0 - 39.9")
            print("Adipositas Grad III: ≥ 40.0")
            print("-"*50)
            
        elif auswahl == 4:
            # Gesundheits-Tipp anzeigen
            print("\nVerfügbare Kategorien: untergewicht, normal, übergewicht, adipositas")
            kategorie = input("Für welche BMI-Kategorie möchten Sie einen Tipp? ").lower()
            tipp = bmi.gesundheitstipp(kategorie)
            print(f"\n💡 Gesundheitstipp: {tipp}")
            
        elif auswahl == 5:
            # Programm beenden
            print("\n👋 Programm wird beendet. Bleiben Sie gesund!")
            break  # beendet die while-Schleife

if __name__ == "__main__":
    main()
>>>>>>> develop
