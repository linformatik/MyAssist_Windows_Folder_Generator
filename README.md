# MyAssist - Windows Folder Generator

Ein leichtgewichtiges Python-Tool aus dem **MyAssist**-Ökosystem zur automatischen Erstellung strukturierter Verzeichnishierarchien unter Windows.

Die gewünschte Ordnerstruktur wird einfach über eine `structure.json` definiert. Das Tool eignet sich perfekt, um beispielsweise vordefinierte Vault-Strukturen für **Obsidian** oder wiederkehrende Projektordner blitzschnell anzulegen.

📖 **Ausführliche Anleitung & Hintergrundartikel:**  
[Python-Tool MyAssist: Einen Windows Folder Generator entwickeln und als EXE-Datei bauen](https://linformatik.de/projekt/python-tool-myassist-einen-windows-folder-generator-entwickeln-und-als-exe-datei-bauen/)

---

## 🚀 Features

- **JSON-Basiert:** Vollständig konfigurierbare Ordnerstruktur via `structure.json`.
- **Portable EXE:** Startet direkt unter Windows ohne vorherige Python-Installation.
- **Sicher & Schnell:** Erstellt tiefe Ordnerstrukturen auf Knopfdruck.

---

## 🛠️ Verwendung

1. Lade das Release-Archiv (`.7z`) aus den [GitHub Releases](../../releases) herunter.
2. Entpacke die Datei an einem beliebigen Ort.
3. Passe die `structure.json` nach deinen Wünschen an.
4. Führe die `Windows_Folder_Generator.exe` aus.

### Beispiel `structure.json`

```json
{
  "Projekt_Name": {
    "01_Dokumente": {},
    "02_Obsidian_Vault": {
      "Daily Notes": {},
      "Projects": {},
      "Archive": {}
    },
    "03_Ressourcen": {}
  }
}
```

---

## 👤 Autor

**Salvatore Spadaro**  
Blog: [linformatik.de](https://linformatik.de/)

---

## 📜 Lizenz

Dieses Projekt steht unter der [MIT License](LICENSE).