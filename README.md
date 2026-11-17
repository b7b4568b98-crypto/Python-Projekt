# Gift Detective 🎁🔎

**Ein interaktiver Geschenk-Finder mit Python und Flask.**

Du möchtest jemandem etwas schenken, hast aber keine Idee? Gift Detective fragt nach Beziehung, Alter, Anlass, Interessen, Geschenkstil, Budget und Zeitdruck. Anschließend bewertet ein eigener, nachvollziehbarer Python-Algorithmus über 50 Beispielgeschenke und zeigt bis zu sechs passende Vorschläge mit Begründung an.

## So funktioniert der Algorithmus

1. **Eingaben prüfen:** Python prüft, ob die Angaben gültig sind.
2. **Harte Filter:** Geschenke über dem Budget, ausgeschlossene Geschenkarten und altersmäßig unpassende Vorschläge werden entfernt. Bei kurzfristiger Suche entfallen Ideen, die vorherige Planung brauchen.
3. **Bewerten:** Passende Interessen bringen die meisten Punkte. Danach folgen Geschenkstil, Beziehung, Anlass und weitere Kriterien.
4. **Abwechslung:** Der Algorithmus bevorzugt verschiedene Kategorien statt sechs beinahe gleicher Vorschläge.
5. **Begründen:** Jede Empfehlung zeigt, warum sie vorgeschlagen wurde.

**Wichtig:** Der Katalog ist handgepflegt. Preisangaben sind grobe Richtwerte, keine Live-Preise. Gift Detective verwendet keine KI, keine Shopschnittstelle und speichert keine eingegebenen persönlichen Angaben. Es werden noch keine Geschenke gekauft oder versendet.

## Projektstruktur

```text
Gift-Detective/
├── app.py                  # Flask: Startseite, Formulardaten, Ergebnisse
├── gift_engine.py          # Geschenkekatalog + Empfehlungsalgorithmus
├── requirements.txt        # Python-Pakete
├── render.yaml             # Konfiguration für Render
├── templates/
│   ├── base.html           # Gemeinsame HTML-Struktur
│   ├── index.html          # Eingabeformular
│   └── results.html        # Auswertung und Geschenkideen
├── static/
│   ├── style.css           # Design
│   └── app.js              # Kleine Browser-Interaktionen
└── tests/
    └── test_app.py        # Automatisierte Tests
```

## In PyCharm lokal starten

1. Repository über **Project from Version Control** klonen oder bestehendes Projekt mit **Git → Pull** aktualisieren. Lokale Änderungen vorher sichern.
2. Unten **Terminal** öffnen.
3. Abhängigkeiten installieren (Windows):

   ```powershell
   py -m pip install -r requirements.txt
   ```

4. App starten:

   ```powershell
   py app.py
   ```

5. Im Browser **http://127.0.0.1:5000** öffnen.
6. Beenden: im Terminal `Strg + C` drücken.

Bei aktiver virtueller Umgebung (`.venv`) stattdessen für beide Befehle `python` verwenden.

## Tests ausführen

```powershell
py -m unittest discover -s tests -v
```

## Änderungen veröffentlichen

1. In PyCharm programmieren und lokal testen.
2. Änderungen per Commit und Push zu GitHub übertragen.
3. Im bereits vorhandenen Render-Webservice **Manual Deploy → Deploy latest commit** wählen. Auto-Deploy bleibt ausgeschaltet.

Die Konfiguration behält den bisherigen Render-Servicenamen `python-projekt-formular` bei. Build Command: `pip install -r requirements.txt`. Start Command: `gunicorn app:app`. Gesundheitscheck: `/health`. Kein neuer Blueprint nötig, sofern der bestehende Service weiterhin mit diesem Repository verbunden ist.

## Was du selbst weiterprogrammieren kannst

- Füge in `gift_engine.py` ein eigenes Geschenk mit Tags hinzu.
- Ändere die Punktevergabe in `recommend()`.
- Baue ein weiteres Kriterium ein, z. B. "nachhaltig".
- Ergänze Kategorien und Interessen im Formular.
- Optional später: favorisierte Ideen in einer Datenbank speichern.

## Technologie

Python · Flask · Jinja2/HTML · CSS · etwas JavaScript · GitHub · Render
