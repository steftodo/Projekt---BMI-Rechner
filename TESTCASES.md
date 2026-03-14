# Testfälle für Interaktiven BMI-Rechner

## Testfall 1: Normale BMI-Berechnung
- **Input**: Größe=1.75m, Gewicht=70kg, Name="Test"
- **Erwartetes Ergebnis**: BMI=22.9, Kategorie="Normalgewicht"
- **Tatsächliches Ergebnis**: BMI=22.9, Kategorie="Normalgewicht"
- **Status**: ✅ Bestanden

## Testfall 2: Untergewicht-Berechnung
- **Input**: Größe=1.70m, Gewicht=50kg, Name="Test2"
- **Erwartetes Ergebnis**: BMI=17.3, Kategorie="Untergewicht"
- **Tatsächliches Ergebnis**: BMI=17.3, Kategorie="Untergewicht"
- **Status**: ✅ Bestanden

## Testfall 3: Übergewicht-Berechnung
- **Input**: Größe=1.65m, Gewicht=80kg, Name="Test3"
- **Erwartetes Ergebnis**: BMI=29.4, Kategorie="Übergewicht"
- **Tatsächliches Ergebnis**: BMI=29.4, Kategorie="Übergewicht"
- **Status**: ✅ Bestanden

## Testfall 4: Adipositas-Berechnung
- **Input**: Größe=1.70m, Gewicht=110kg, Name="Test4"
- **Erwartetes Ergebnis**: BMI=38.1, Kategorie="Adipositas Grad II"
- **Tatsächliches Ergebnis**: BMI=38.1, Kategorie="Adipositas Grad II"
- **Status**: ✅ Bestanden

## Testfall 5: Ungültige Größe (negative Zahl)
- **Input**: Größe=-1.75m
- **Erwartetes Ergebnis**: Fehlermeldung "Wert muss größer als 0 sein"
- **Tatsächliches Ergebnis**: Fehler: Der Wert muss größer als 0 sein!
- **Status**: ✅ Bestanden

## Testfall 6: Buchstabeneingabe bei Größe
- **Input**: Größe="abc"
- **Erwartetes Ergebnis**: Fehlermeldung "Bitte eine gültige Zahl"
- **Tatsächliches Ergebnis**: Fehler: Bitte eine gültige Zahl eingeben!
- **Status**: ✅ Bestanden

## Testfall 7: BMI-Verlauf (maximal 10 Einträge)
- **Input**: 12 BMI-Berechnungen durchführen
- **Erwartetes Ergebnis**: Nur die letzten 10 werden gespeichert
- **Tatsächliches Ergebnis**: Verlauf zeigt korrekt 10 Einträge
- **Status**: ✅ Bestanden

## Testfall 8: Leerer Verlauf anzeigen
- **Input**: Verlauf anzeigen ohne vorherige Berechnungen
- **Erwartetes Ergebnis**: "Noch keine BMI-Berechnungen vorhanden"
- **Tatsächliches Ergebnis**: 📭 Noch keine BMI-Berechnungen vorhanden.
- **Status**: ✅ Bestanden

## Testfall 9: Ungültige Menüauswahl
- **Input**: Menüauswahl "6" (außerhalb 1-5)
- **Erwartetes Ergebnis**: Fehlermeldung "Zahl zwischen 1 und 5"
- **Tatsächliches Ergebnis**: Fehler: Bitte eine Zahl zwischen 1 und 5 eingeben!
- **Status**: ✅ Bestanden

## Testfall 10: Programm beenden
- **Input**: Menüauswahl 5
- **Erwartetes Ergebnis**: Programm endet mit Abschiedsnachricht
- **Tatsächliches Ergebnis**: 👋 Programm wird beendet. Bleiben Sie gesund!
- **Status**: ✅ Bestanden