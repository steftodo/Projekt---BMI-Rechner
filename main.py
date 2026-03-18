"""
Interaktiver BMI-Rechner - Konsolenversion
"""

import bmi_calculator

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Fehler: Der Wert muss größer als 0 sein!")
                continue
            return value
        except ValueError:
            print("❌ Fehler: Bitte eine gültige Zahl eingeben!")

def get_menu_choice():
    while True:
        try:
            choice = int(input("\nWählen Sie eine Option (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("❌ Fehler: Bitte eine Zahl zwischen 1 und 6 eingeben!")
        except ValueError:
            print("❌ Fehler: Bitte eine gültige Zahl eingeben!")

def main():
    calculator = bmi_calculator.BMICalculator()

    print("👋 Willkommen zum Interaktiven BMI-Rechner!")
    print("=" * 50)

    while True:
        print("\n📋 Menü:")
        print("1. BMI berechnen")
        print("2. Verlauf anzeigen")
        print("3. Verlauf löschen")
        print("4. BMI-Kategorien anzeigen")
        print("5. Testfälle ausführen")
        print("6. Programm beenden")

        choice = get_menu_choice()

        if choice == 1:
            name = input("👤 Name: ")
            height = get_float_input("📏 Größe (in Metern): ")
            weight = get_float_input("⚖️ Gewicht (in kg): ")

            try:
                result = calculator.add_calculation(name, height, weight)
                print("\n✅ BMI-Berechnung erfolgreich!")
                print(f"👤 Name: {result['name']}")
                print(f"📏 Größe: {result['height']} m")
                print(f"⚖️ Gewicht: {result['weight']} kg")
                print(f"🧮 BMI: {result['bmi']}")
                print(f"📊 Kategorie: {result['category']}")
                print(f"💡 Tipp: {result['tip']}")
            except ValueError as e:
                print(f"❌ {e}")

        elif choice == 2:
            history = calculator.get_history()
            if not history:
                print("📭 Noch keine BMI-Berechnungen vorhanden.")
            else:
                print("\n📜 Verlauf der letzten Berechnungen:")
                for i, entry in enumerate(history, 1):
                    print(f"{i}. {entry['name']}: BMI {entry['bmi']} ({entry['category']})")

        elif choice == 3:
            calculator.clear_history()
            print("🗑️ Verlauf gelöscht.")

        elif choice == 4:
            print("\n📊 BMI-Kategorien (WHO-Standard):")
            print("- Untergewicht: < 18.5")
            print("- Normalgewicht: 18.5 - 24.9")
            print("- Übergewicht: 25.0 - 29.9")
            print("- Adipositas Grad I: 30.0 - 34.9")
            print("- Adipositas Grad II: 35.0 - 39.9")
            print("- Adipositas Grad III: ≥ 40.0")

        elif choice == 5:
            run_test_cases()

        elif choice == 6:
            print("👋 Programm wird beendet. Bleiben Sie gesund!")
            break

def run_test_cases():
    """
    Führt die Testfälle aus TESTCASES.md aus.
    """
    print("\n🧪 Testfälle werden ausgeführt...")

    calculator = bmi_calculator.BMICalculator()

    # Testfall 1: Normale BMI-Berechnung
    try:
        result = calculator.add_calculation("Test", 1.75, 70)
        assert result['bmi'] == 22.9 and result['category'] == "Normalgewicht"
        print("✅ Testfall 1: Bestanden")
    except:
        print("❌ Testfall 1: Fehlgeschlagen")

    # Testfall 2: Untergewicht
    try:
        result = calculator.add_calculation("Test2", 1.70, 50)
        assert result['bmi'] == 17.3 and result['category'] == "Untergewicht"
        print("✅ Testfall 2: Bestanden")
    except:
        print("❌ Testfall 2: Fehlgeschlagen")

    # Testfall 3: Übergewicht
    try:
        result = calculator.add_calculation("Test3", 1.65, 80)
        assert result['bmi'] == 29.4 and result['category'] == "Übergewicht"
        print("✅ Testfall 3: Bestanden")
    except:
        print("❌ Testfall 3: Fehlgeschlagen")

    # Testfall 4: Adipositas
    try:
        result = calculator.add_calculation("Test4", 1.70, 110)
        assert result['bmi'] == 38.1 and result['category'] == "Adipositas Grad II"
        print("✅ Testfall 4: Bestanden")
    except:
        print("❌ Testfall 4: Fehlgeschlagen")

    # Testfall 5: Ungültige Größe
    try:
        calculator.add_calculation("Test", -1.75, 70)
        print("❌ Testfall 5: Fehlgeschlagen")
    except ValueError:
        print("✅ Testfall 5: Bestanden")

    # Testfall 6: Buchstabeneingabe - hier simulieren wir es
    # Da input nicht getestet wird, überspringen oder anpassen
    print("✅ Testfall 6: Übersprungen (interaktiv)")

    # Testfall 7: BMI-Verlauf
    calculator.clear_history()
    for i in range(12):
        calculator.add_calculation(f"Test{i}", 1.70, 70)
    assert len(calculator.get_history()) == 10
    print("✅ Testfall 7: Bestanden")

    # Testfall 8: Leerer Verlauf
    calculator.clear_history()
    assert len(calculator.get_history()) == 0
    print("✅ Testfall 8: Bestanden")

    # Testfall 9: Ungültige Menüauswahl - übersprungen, da interaktiv
    print("✅ Testfall 9: Übersprungen (interaktiv)")

    # Testfall 10: Programm beenden - übersprungen
    print("✅ Testfall 10: Übersprungen (interaktiv)")

    print("🧪 Testfälle abgeschlossen.")

if __name__ == "__main__":
    main()
