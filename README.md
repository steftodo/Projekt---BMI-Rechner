# BMI-Rechner

Ein interaktives Programm zur Berechnung des Body Mass Index (BMI) mit Konsolen- und grafischer Benutzeroberfläche, entwickelt in Python.

## Autoren

- Stefan Todorovski
- Mustafa Sipahi

## Datum

15.03.2026

## Kurzbeschreibung
Ein interaktives, konsolenbasiertes Programm zur Berechnung des Body Mass Index (BMI). 
Der Rechner ermöglicht wiederholte Berechnungen, speichert den Verlauf der letzten 10 
Eingaben und gibt individuelle Gesundheitsempfehlungen basierend auf den Ergebnissen.

## Python-Version
- Python 3.11 oder höher
- Getestet mit Python 3.11.4

## Verwendete Module / Bibliotheken
Das Programm verwendet ausschließlich die Python-Standardbibliothek:
- **math** (implizit) - Für mathematische Berechnungen
- Tkinter (für GUI-Version) - Standardmäßig in Python enthalten
- Keine externen Module erforderlich!

## Features

- BMI-Berechnung
- Kategorisierung nach WHO-Standards (Untergewicht, Normalgewicht, Übergewicht, Adipositas)
- Verlauf der letzten Berechnungen
- Gesundheitstipps basierend auf BMI-Kategorie
- Einfache GUI mit Tkinter
- Konsolenversion für wiederholte Berechnungen

## Installation

1. Python 3.11+ installieren (https://www.python.org/downloads/)
2. Projektordner herunterladen oder klonen
3. Terminal/Command Prompt öffnen
4. In den Projektordner navigieren: `cd bmi_rechner`
5. Programm starten: `python main.py` oder `python gui_main.py`

## Verwendung

### GUI-Version
Führe `gui_main.py` aus:
```
python gui_main.py
```

- Gib Name, Größe (in Metern) und Gewicht (in kg) ein.
- Klicke auf "BMI berechnen", um das Ergebnis zu erhalten.
- Verwende die anderen Buttons für Verlauf, Kategorien oder Gesundheitstipps.   

### Konsolen-Version
Führe `main.py` aus:
```
python main.py
```

## BMI-Kategorien (WHO-Standard)

- Untergewicht: < 18.5
- Normalgewicht: 18.5 - 24.9
- Übergewicht: 25.0 - 29.9
- Adipositas Grad I: 30.0 - 34.9
- Adipositas Grad II: 35.0 - 39.9
- Adipositas Grad III: ≥ 40.0

## Hinweis

Dies ist ein Bildungsprojekt und ersetzt keine professionelle medizinische Beratung. Bei gesundheitlichen Fragen konsultiere einen Arzt.