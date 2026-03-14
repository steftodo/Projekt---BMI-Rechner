"""
BMI-Rechner mit grafischer Benutzeroberfläche
Autor: [Stefan Todorovski / Mustafa Sipahi]
Datum: [14.03.2026]

Kombiniert die Module: bmi_calculator.py und bmi_visualizer.py in einer GUI
"""

import tkinter as tk
from tkinter import ttk, messagebox, font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import bmi_calculator as bmi
import bmi_visualizer as visual

class BMI_GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🏥 BMI-Rechner - Professionelle Gesundheitsanalyse")
        self.root.geometry("1000x700")
        self.root.minsize(900, 650)
        
        # Farbschema
        self.farben = {
            'bg': '#f0f4f8',
            'primary': '#2c3e50',
            'secondary': '#3498db',
            'success': '#27ae60',
            'warning': '#f39c12',
            'danger': '#e74c3c',
            'white': '#ffffff',
            'light': '#ecf0f1'
        }
        
        self.root.configure(bg=self.farben['bg'])
        
        # Aktuelle BMI-Daten
        self.aktueller_bmi = None
        self.aktuelle_daten = None
        
        # GUI aufbauen
        self.setup_ui()
        
        # Willkommensnachricht
        self.status_var.set("👋 Willkommen! Geben Sie Ihre Daten ein und klicken Sie auf 'BMI berechnen'")
    
    def setup_ui(self):
        """Baut die komplette Benutzeroberfläche auf"""
        
        # Hauptcontainer mit Padding
        main_container = ttk.Frame(self.root, padding="10")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Style konfigurieren
        self.setup_styles()
        
        # === LINKER BEREICH: BEDIENFELD ===
        left_frame = ttk.Frame(main_container, width=300, relief=tk.RAISED, borderwidth=2)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        left_frame.pack_propagate(False)
        left_frame.configure(width=300)
        
        # Header im Bedienfeld
        ttk.Label(left_frame, text="⚙️ BEDIENFELD", 
                 font=('Arial', 14, 'bold')).pack(pady=10)
        
        # Separator
        ttk.Separator(left_frame, orient='horizontal').pack(fill=tk.X, padx=5, pady=5)
        
        # === EINGABEFORMULAR ===
        input_frame = ttk.LabelFrame(left_frame, text="📝 Ihre Daten", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Name
        ttk.Label(input_frame, text="Name:").pack(anchor=tk.W)
        self.name_entry = ttk.Entry(input_frame, font=('Arial', 10))
        self.name_entry.pack(fill=tk.X, pady=(0, 10))
        self.name_entry.insert(0, "Unbekannt")
        
        # Größe
        ttk.Label(input_frame, text="Größe (m):").pack(anchor=tk.W)
        self.groesse_entry = ttk.Entry(input_frame, font=('Arial', 10))
        self.groesse_entry.pack(fill=tk.X, pady=(0, 10))
        self.groesse_entry.insert(0, "1.75")
        
        # Gewicht
        ttk.Label(input_frame, text="Gewicht (kg):").pack(anchor=tk.W)
        self.gewicht_entry = ttk.Entry(input_frame, font=('Arial', 10))
        self.gewicht_entry.pack(fill=tk.X, pady=(0, 10))
        self.gewicht_entry.insert(0, "70")
        
        # === AKTIONSBUTTONS ===
        action_frame = ttk.LabelFrame(left_frame, text="🎮 Aktionen", padding=10)
        action_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # BMI berechnen Button (groß und auffällig)
        self.calc_btn = tk.Button(action_frame, text="📊 BMI BERECHNEN", 
                                  bg=self.farben['success'], fg='white',
                                  font=('Arial', 11, 'bold'), height=2,
                                  command=self.bmi_berechnen)
        self.calc_btn.pack(fill=tk.X, pady=5)
        
        # Reset Button
        self.reset_btn = tk.Button(action_frame, text="🔄 Eingaben zurücksetzen",
                                   bg=self.farben['warning'], fg='white',
                                   font=('Arial', 10), command=self.eingaben_reset)
        self.reset_btn.pack(fill=tk.X, pady=5)
        
        # === GRAFIK-AUSWAHL ===
        grafik_frame = ttk.LabelFrame(left_frame, text="📈 Grafische Darstellung", padding=10)
        grafik_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.grafik_var = tk.StringVar(value="balken")
        
        ttk.Radiobutton(grafik_frame, text="📊 BMI-Balken", 
                       variable=self.grafik_var, value="balken").pack(anchor=tk.W)
        ttk.Radiobutton(grafik_frame, text="📈 Verlaufsgrafik", 
                       variable=self.grafik_var, value="verlauf").pack(anchor=tk.W)
        ttk.Radiobutton(grafik_frame, text="🥧 Kategorien-Torte", 
                       variable=self.grafik_var, value="torte").pack(anchor=tk.W)
        ttk.Radiobutton(grafik_frame, text="📊 Vergleichsgrafik", 
                       variable=self.grafik_var, value="vergleich").pack(anchor=tk.W)
        
        # Grafik anzeigen Button
        self.grafik_btn = tk.Button(grafik_frame, text="🖼️ Grafik anzeigen",
                                    bg=self.farben['secondary'], fg='white',
                                    font=('Arial', 10), command=self.grafik_anzeigen)
        self.grafik_btn.pack(fill=tk.X, pady=10)
        
        # === INFO-BEREICH ===
        info_frame = ttk.LabelFrame(left_frame, text="ℹ️ Info", padding=10)
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Version
        ttk.Label(info_frame, text="Version 2.0", font=('Arial', 9, 'italic')).pack()
        
        # === RECHTER BEREICH: ANZEIGE UND GRAFIK ===
        right_frame = ttk.Frame(main_container, relief=tk.SUNKEN, borderwidth=2)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # === BMI-ERGEBNIS-KARTE ===
        result_frame = ttk.LabelFrame(right_frame, text="📊 BMI-Ergebnis", padding=10)
        result_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # BMI-Wert (groß)
        self.bmi_wert_var = tk.StringVar(value="--")
        bmi_label = ttk.Label(result_frame, textvariable=self.bmi_wert_var,
                             font=('Arial', 24, 'bold'), foreground=self.farben['primary'])
        bmi_label.pack()
        
        # Kategorie
        self.kategorie_var = tk.StringVar(value="Bitte Daten eingeben")
        ttk.Label(result_frame, textvariable=self.kategorie_var,
                 font=('Arial', 12)).pack()
        
        # Separator
        ttk.Separator(result_frame, orient='horizontal').pack(fill=tk.X, pady=5)
        
        # Empfehlung
        self.empfehlung_text = tk.Text(result_frame, height=3, wrap=tk.WORD,
                                       font=('Arial', 10), bg=self.farben['light'])
        self.empfehlung_text.pack(fill=tk.X)
        self.empfehlung_text.insert(1.0, "👈 Geben Sie Ihre Daten links ein und klicken Sie auf 'BMI BERECHNEN'")
        self.empfehlung_text.config(state=tk.DISABLED)
        
        # === GRAFIK-BEREICH ===
        grafik_container = ttk.LabelFrame(right_frame, text="📈 Grafische Darstellung", padding=10)
        grafik_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame für Matplotlib-Figure
        self.grafik_frame = ttk.Frame(grafik_container)
        self.grafik_frame.pack(fill=tk.BOTH, expand=True)
        
        # Platzhalter für Matplotlib-Figure
        self.figur = None
        self.canvas = None
        
        # === STATUS-LEISTE ===
        status_frame = ttk.Frame(self.root, relief=tk.SUNKEN, borderwidth=1)
        status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.status_var = tk.StringVar()
        ttk.Label(status_frame, textvariable=self.status_var, 
                 font=('Arial', 9)).pack(side=tk.LEFT, padx=5)
        
        # Verlaufslänge anzeigen
        self.verlauf_var = tk.StringVar(value="Verlauf: 0 Einträge")
        ttk.Label(status_frame, textvariable=self.verlauf_var,
                 font=('Arial', 9)).pack(side=tk.RIGHT, padx=5)
    
    def setup_styles(self):
        """Konfiguriert ttk Styles für bessere Optik"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Farbschema für ttk Widgets
        style.configure('TLabel', background=self.farben['bg'], font=('Arial', 10))
        style.configure('TFrame', background=self.farben['bg'])
        style.configure('TLabelFrame', background=self.farben['bg'], font=('Arial', 10, 'bold'))
        style.configure('TButton', font=('Arial', 10))
    
    def bmi_berechnen(self):
        """Berechnet BMI aus den Eingabefeldern"""
        try:
            # Eingaben holen
            name = self.name_entry.get() or "Unbekannt"
            groesse = float(self.groesse_entry.get())
            gewicht = float(self.gewicht_entry.get())
            
            # Validierung
            if groesse <= 0 or groesse > 3:
                messagebox.showerror("Fehler", "Bitte eine realistische Größe eingeben (0.5-3.0 m)")
                return
            if gewicht <= 0 or gewicht > 500:
                messagebox.showerror("Fehler", "Bitte ein realistisches Gewicht eingeben (1-500 kg)")
                return
            
            # BMI berechnen
            self.aktuelle_daten = bmi.bmi_berechnen(groesse, gewicht, name)
            self.aktueller_bmi = self.aktuelle_daten['wert']
            
            # Ergebnis anzeigen
            self.bmi_wert_var.set(f"{self.aktueller_bmi:.1f}")
            self.kategorie_var.set(self.aktuelle_daten['kategorie'])
            
            # Empfehlung anzeigen
            self.empfehlung_text.config(state=tk.NORMAL)
            self.empfehlung_text.delete(1.0, tk.END)
            self.empfehlung_text.insert(1.0, self.aktuelle_daten['empfehlung'])
            self.empfehlung_text.config(state=tk.DISABLED)
            
            # Status aktualisieren
            self.status_var.set(f"✅ BMI berechnet für {name}: {self.aktueller_bmi:.1f}")
            self.verlauf_var.set(f"Verlauf: {len(bmi.bmi_verlauf)} Einträge")
            
            # Automatisch die Standardgrafik anzeigen
            self.grafik_var.set("balken")
            self.grafik_anzeigen()
            
        except ValueError:
            messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben!\n\nBeispiel:\nGröße: 1.75\nGewicht: 70")
    
    def grafik_anzeigen(self):
        """Zeigt die ausgewählte Grafik an"""
        if not self.aktueller_bmi and self.grafik_var.get() != "verlauf":
            messagebox.showwarning("Keine Daten", "Bitte zuerst einen BMI berechnen!")
            return
        
        # Alte Grafik entfernen
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        if self.figur:
            plt.close(self.figur)
        
        # Neue Grafik erstellen basierend auf Auswahl
        grafik_typ = self.grafik_var.get()
        
        if grafik_typ == "balken" and self.aktuelle_daten:
            self.figur = visual.erstelle_bmi_balken_figur(
                self.aktueller_bmi, self.aktuelle_daten['name'])
            titel = "📊 BMI-Balken"
            
        elif grafik_typ == "verlauf":
            if not bmi.bmi_verlauf:
                messagebox.showinfo("Kein Verlauf", "Noch keine Verlaufsdaten vorhanden.")
                return
            self.figur = visual.erstelle_verlaufs_figur(bmi.bmi_verlauf)
            titel = "📈 BMI-Verlauf"
            
        elif grafik_typ == "torte" and self.aktueller_bmi:
            self.figur = visual.erstelle_torten_figur(self.aktueller_bmi)
            titel = "🥧 Kategorien-Verteilung"
            
        elif grafik_typ == "vergleich" and self.aktuelle_daten:
            self.figur = visual.erstelle_vergleichs_figur(
                self.aktueller_bmi, 
                self.aktuelle_daten['groesse'], 
                self.aktuelle_daten['gewicht'])
            titel = "📊 Durchschnittsvergleich"
        
        else:
            messagebox.showwarning("Keine Grafik", "Für diese Grafik liegen nicht genügend Daten vor.")
            return
        
        # Grafik im GUI anzeigen
        if self.figur:
            self.canvas = FigureCanvasTkAgg(self.figur, self.grafik_frame)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            # Titel der Grafik in der Statusleiste
            self.status_var.set(f"🖼️ Zeige: {titel}")
    
    def eingaben_reset(self):
        """Setzt alle Eingaben zurück"""
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, "Unbekannt")
        self.groesse_entry.delete(0, tk.END)
        self.groesse_entry.insert(0, "1.75")
        self.gewicht_entry.delete(0, tk.END)
        self.gewicht_entry.insert(0, "70")
        
        self.bmi_wert_var.set("--")
        self.kategorie_var.set("Bitte Daten eingeben")
        
        self.empfehlung_text.config(state=tk.NORMAL)
        self.empfehlung_text.delete(1.0, tk.END)
        self.empfehlung_text.insert(1.0, "👈 Geben Sie Ihre Daten links ein und klicken Sie auf 'BMI BERECHNEN'")
        self.empfehlung_text.config(state=tk.DISABLED)
        
        # Grafik löschen
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
            self.canvas = None
        if self.figur:
            plt.close(self.figur)
            self.figur = None
        
        self.status_var.set("🔄 Eingaben zurückgesetzt")

def main():
    """Hauptfunktion zum Starten der GUI"""
    root = tk.Tk()
    app = BMI_GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()