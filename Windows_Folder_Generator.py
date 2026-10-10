import json
import sys
from pathlib import Path
import customtkinter as ctk

# Erscheinungsbild konfigurieren
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class FolderGeneratorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("MyAssist - Windows Folder Generator")
        self.geometry("550x540")  # Höhe angepasst, da Eingabefelder wegfallen

        # Zuverlässige Ermittlung des Ordners (egal ob als Skript oder .exe)
        if getattr(sys, "frozen", False):
            self.script_dir = Path(sys.executable).resolve().parent
        else:
            self.script_dir = Path(__file__).resolve().parent

        self.config_file = self.script_dir / "structure.json"
        self.config_data = self.load_config()

        # UI Elemente aufbauen
        self.create_widgets()

    def load_config(self):
        """Lädt die JSON-Datei direkt aus dem Verzeichnis der EXE / des Skripts."""
        if self.config_file.exists():
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"Fehler beim Laden der JSON: {e}")
        
        # Fallback, falls keine JSON existiert
        return {"root_name": "MyAssist", "folders": []}

    def create_widgets(self):
        # Überschrift
        self.label_title = ctk.CTkLabel(
            self, text="MyAssist - Windows Folder Generator", font=("Arial", 18, "bold")
        )
        self.label_title.pack(pady=15)

        # Name des Basis-Ordners / Zielverzeichnisses
        self.frame_root = ctk.CTkFrame(self)
        self.frame_root.pack(fill="x", padx=20, pady=5)

        self.label_root = ctk.CTkLabel(self.frame_root, text="Basis-Ordner (Ziel):")
        self.label_root.pack(side="left", padx=10)

        self.entry_root = ctk.CTkEntry(self.frame_root, width=280)
        self.entry_root.insert(
            0, self.config_data.get("root_name", "MyAssist")
        )
        self.entry_root.pack(side="right", padx=10, pady=5)

        # Liste der Unterordner (Textfeld zur Ansicht)
        self.label_list = ctk.CTkLabel(
            self,
            text="Definierte Ordner-Struktur (aus structure.json):",
            font=("Arial", 12),
        )
        self.label_list.pack(anchor="w", padx=22, pady=(10, 0))

        self.textbox_folders = ctk.CTkTextbox(self, width=490, height=240)
        self.textbox_folders.pack(pady=5, padx=20)
        self.update_textbox()

        # Statusmeldung
        self.label_status = ctk.CTkLabel(
            self, text="", font=("Arial", 12, "italic")
        )
        self.label_status.pack(pady=5)

        # Haupt-Aktionsbutton
        self.btn_create = ctk.CTkButton(
            self,
            text="🚀 Ordnerstruktur im gleichen Verzeichnis erstellen",
            fg_color="green",
            hover_color="darkgreen",
            height=40,
            command=self.create_folders,
        )
        self.btn_create.pack(pady=15, padx=20, fill="x")

    def update_textbox(self):
        self.textbox_folders.delete("1.0", "end")
        for folder in self.config_data.get("folders", []):
            self.textbox_folders.insert("end", f"{folder}\n")

    def create_folders(self):
        root_input = self.entry_root.get().strip()
        
        # Erstellt die Ordner relativ zum Verzeichnis, in dem die .exe liegt
        base_path = self.script_dir / root_input

        created_count = 0
        try:
            for folder in self.config_data.get("folders", []):
                full_path = base_path / folder
                full_path.mkdir(parents=True, exist_ok=True)
                created_count += 1

            self.label_status.configure(
                text=f"✓ Erfolgreich {created_count} Ordner in '{base_path.name}' erstellt!",
                text_color="lightgreen",
            )
        except Exception as e:
            self.label_status.configure(
                text=f"❌ Fehler: {str(e)}", text_color="red"
            )


if __name__ == "__main__":
    app = FolderGeneratorApp()
    app.mainloop()