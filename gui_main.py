"""
Grafische Benutzeroberfläche für den BMI-Rechner
Autor: [Stefan Todorovski / Mustafa Sipahi]
Datum: [15.03.2026]
Kurzbeschreibung: GUI-Version des BMI-Rechners mit Tkinter
"""

import tkinter as tk
from tkinter import messagebox, scrolledtext
import bmi_calculator as bmi

class BMIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI-Rechner")
        self.root.geometry("600x500")

        # Eingabefelder
        self.create_input_fields()

        # Buttons
        self.create_buttons()

        # Ausgabebereich
        self.create_output_area()

    def create_input_fields(self):
        # Frame für Eingaben
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # Name
        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Größe
        tk.Label(input_frame, text="Größe (m):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.height_entry = tk.Entry(input_frame)
        self.height_entry.grid(row=1, column=1, padx=5, pady=5)

        # Gewicht
        tk.Label(input_frame, text="Gewicht (kg):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.weight_entry = tk.Entry(input_frame)
        self.weight_entry.grid(row=2, column=1, padx=5, pady=5)

    def create_buttons(self):
        # Frame für Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # BMI berechnen
        tk.Button(button_frame, text="BMI berechnen", command=self.calculate_bmi).grid(row=0, column=0, padx=5)

        # Verlauf anzeigen
        tk.Button(button_frame, text="Verlauf anzeigen", command=self.show_history).grid(row=0, column=1, padx=5)

        # Kategorien erklären
        tk.Button(button_frame, text="Kategorien erklären", command=self.show_categories).grid(row=0, column=2, padx=5)

        # Gesundheitstipp
        tk.Button(button_frame, text="Gesundheitstipp", command=self.show_tip).grid(row=0, column=3, padx=5)

    def create_output_area(self):
        # Scrolled Text für Ausgaben
        self.output_text = scrolledtext.ScrolledText(self.root, width=70, height=15)
        self.output_text.pack(pady=10)

    def calculate_bmi(self):
        try:
            name = self.name_entry.get().strip() or "Unbekannt"
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())

            if height <= 0 or weight <= 0:
                messagebox.showerror("Fehler", "Größe und Gewicht müssen größer als 0 sein!")
                return

            result = bmi.bmi_berechnen(height, weight, name)

            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"BMI-Ergebnis für {result['name']}:\n")
            self.output_text.insert(tk.END, f"BMI-Wert: {result['wert']:.1f}\n")
            self.output_text.insert(tk.END, f"Kategorie: {result['kategorie']}\n")
            self.output_text.insert(tk.END, f"{result['empfehlung']}\n")

        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen für Größe und Gewicht eingeben!")

    def show_history(self):
        history = bmi.verlauf_anzeigen()
        self.output_text.delete(1.0, tk.END)

        if not history:
            self.output_text.insert(tk.END, "Noch keine BMI-Berechnungen vorhanden.\n")
        else:
            self.output_text.insert(tk.END, "BMI-Verlauf (letzte 10 Berechnungen):\n\n")
            for i, entry in enumerate(history, 1):
                self.output_text.insert(tk.END, f"{i}. {entry['name']}: BMI {entry['wert']:.1f} - {entry['kategorie']}\n")

    def show_categories(self):
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "BMI-Kategorien (WHO-Standard):\n\n")
        self.output_text.insert(tk.END, "Untergewicht: < 18.5\n")
        self.output_text.insert(tk.END, "Normalgewicht: 18.5 - 24.9\n")
        self.output_text.insert(tk.END, "Übergewicht: 25.0 - 29.9\n")
        self.output_text.insert(tk.END, "Adipositas Grad I: 30.0 - 34.9\n")
        self.output_text.insert(tk.END, "Adipositas Grad II: 35.0 - 39.9\n")
        self.output_text.insert(tk.END, "Adipositas Grad III: ≥ 40.0\n")

    def show_tip(self):
        # Einfaches Dialogfenster für Kategorie-Auswahl
        tip_window = tk.Toplevel(self.root)
        tip_window.title("Gesundheitstipp auswählen")
        tip_window.geometry("300x150")

        tk.Label(tip_window, text="Kategorie:").pack(pady=5)
        category_var = tk.StringVar()
        category_menu = tk.OptionMenu(tip_window, category_var, "untergewicht", "normal", "übergewicht", "adipositas")
        category_menu.pack(pady=5)

        def get_tip():
            category = category_var.get()
            if category:
                tip = bmi.gesundheitstipp(category)
                self.output_text.delete(1.0, tk.END)
                self.output_text.insert(tk.END, f"Gesundheitstipp für {category}:\n{tip}\n")
                tip_window.destroy()
            else:
                messagebox.showerror("Fehler", "Bitte eine Kategorie auswählen!")

        tk.Button(tip_window, text="Tipp anzeigen", command=get_tip).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BMIGUI(root)
    root.mainloop()