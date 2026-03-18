# BMI-Rechner

Ein einfacher BMI-Rechner mit grafischer Benutzeroberfläche, entwickelt in Python mit Tkinter.

## Autoren

- Stefan Todorovski
- Mustafa Sipahi

## Datum

15.03.2026

## Beschreibung

Dieses Projekt bietet einen BMI-Rechner (Body Mass Index) mit zwei Versionen:
- Eine Konsolenversion (`main.py`)
- Eine grafische Benutzeroberfläche (`gui_main.py`)

Der BMI-Rechner berechnet den Body Mass Index basierend auf Größe und Gewicht, kategorisiert das Ergebnis nach WHO-Standards und gibt Empfehlungen sowie Gesundheitstipps.

## Features

- BMI-Berechnung
- Kategorisierung nach WHO-Standards (Untergewicht, Normalgewicht, Übergewicht, Adipositas)
- Verlauf der letzten Berechnungen
- Gesundheitstipps basierend auf BMI-Kategorie
- Einfache GUI mit Tkinter

## Installation

1. Stelle sicher, dass Python 3 installiert ist.
2. Klone oder lade das Repository herunter.
3. Installiere erforderliche Abhängigkeiten (falls vorhanden):
   ```
   pip install tk
   ```
   Hinweis: Tkinter ist standardmäßig in Python enthalten.

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
Führe `main.py` aus (falls implementiert):
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