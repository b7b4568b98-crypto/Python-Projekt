"""Einfaches Flask-Kontaktformular für das Deployment auf Render."""

import os
import re
import secrets

from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
# In Produktion setzt Render SECRET_KEY über render.yaml.
# Der zufällige Fallback ist nur für das lokale Ausprobieren gedacht.
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


def validate_form(values):
    """Prüft die drei Eingabefelder und gibt Fehlermeldungen zurück."""
    errors = {}
    name = values["name"]
    email = values["email"]
    message = values["message"]

    if not 2 <= len(name) <= 80:
        errors["name"] = "Bitte gib einen Namen mit 2 bis 80 Zeichen ein."
    if len(email) > 254 or not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        errors["email"] = "Bitte gib eine gültige E-Mail-Adresse ein."
    if not 10 <= len(message) <= 2000:
        errors["message"] = "Deine Nachricht muss 10 bis 2000 Zeichen enthalten."
    return errors


@app.route("/", methods=["GET", "POST"])
def index():
    token = session.setdefault("csrf_token", secrets.token_urlsafe(32))
    values = {"name": "", "email": "", "message": ""}
    errors = {}

    if request.method == "POST":
        submitted_token = request.form.get("csrf_token", "")
        if not secrets.compare_digest(token, submitted_token):
            errors["form"] = "Die Sitzung ist abgelaufen. Bitte lade die Seite neu."
            return render_template("index.html", values=values, errors=errors, csrf_token=token), 400

        values = {field: request.form.get(field, "").strip() for field in values}
        errors = validate_form(values)
        if errors:
            return render_template("index.html", values=values, errors=errors, csrf_token=token), 400

        # Demo: keine Datenbank und kein E-Mail-Versand.
        flash("Vielen Dank! Deine Eingabe wurde erfolgreich geprüft (Demo – nicht versendet oder gespeichert).", "success")
        return redirect(url_for("index") + "#formular")

    return render_template("index.html", values=values, errors=errors, csrf_token=token)


@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
