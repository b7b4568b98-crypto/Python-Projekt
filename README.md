# Einfaches Kontaktformular mit Python & Flask

Ein kleines, responsives Webprojekt mit HTML, CSS und Flask. Das Formular fragt **Name**, **E-Mail-Adresse** und **Nachricht** ab. Flask prüft die Eingaben auf dem Server und zeigt eine Bestätigung.

**Wichtig:** Das ist ein Demoformular. Nachrichten werden **nicht verschickt und nicht gespeichert**. Bitte keine echten vertraulichen Daten eingeben.

## Dateien

- `app.py` – Python-/Flask-Webserver und Formularvalidierung
- `templates/index.html` – HTML-Seite und Eingabefelder
- `static/style.css` – Design und mobile Ansicht
- `requirements.txt` – Python-Abhängigkeiten
- `render.yaml` – Render-Konfiguration
- `tests/test_app.py` – einfache Funktionstests

## Lokal starten

1. Python 3.10 oder neuer installieren.
2. Im Projektordner das Terminal öffnen.
3. Virtuelle Umgebung erstellen und aktivieren (empfohlen):

   Windows PowerShell:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Pakete installieren und App starten:

   ```bash
   pip install -r requirements.txt
   python app.py
   ```

5. Im Browser **http://127.0.0.1:5000** öffnen.

## Auf Render.com veröffentlichen

1. Diese Dateien in das GitHub-Repository hochladen. Die Ordnerstruktur beibehalten; vorhandene Dateien nicht versehentlich überschreiben.
2. Bei [Render](https://dashboard.render.com/) anmelden und GitHub verbinden.
3. **New → Blueprint** auswählen, das Repository verbinden und die Datei `render.yaml` verwenden. Render legt einen Python-Web-Service mit kostenlosem Plan an. Eventuelle Namenskonflikte kannst du im Dashboard korrigieren.
4. Die Einrichtung bestätigen und abwarten, bis der Deploy-Status **Live** ist.
5. Die von Render ausgegebene `https://...onrender.com`-Adresse öffnen.

**Alternativ ohne Blueprint:** **New → Web Service**, GitHub-Repository auswählen, Runtime `Python 3`, Build Command `pip install -r requirements.txt`, Start Command `gunicorn app:app`, Plan `Free`. Unter Environment unbedingt eine zufällige, geheime Variable `SECRET_KEY` setzen.

Render startet kostenlose Web-Services nach längerer Inaktivität beim nächsten Aufruf erneut. Ein kostenloser Web-Service hat keinen dauerhaft beschreibbaren lokalen Speicher.

## Tests

Nach Installation der Abhängigkeiten im Projektordner:

```bash
python -m unittest discover -s tests -v
```

## So funktioniert das Formular

1. Der Browser lädt die HTML-Vorlage von Flask.
2. Das Formular schickt die Daten über `POST` an `/`.
3. Flask prüft einen Sitzungstoken gegen fremde Formulare (CSRF-Schutz) und kontrolliert Länge und Format der Felder.
4. Bei Fehlern bleiben die Eingaben sichtbar. Bei Erfolg erscheint eine Meldung, ohne die Nachricht zu speichern.

Für echte Kontaktanfragen müsste später ein E-Mail-Dienst oder eine Datenbank ergänzt werden.
