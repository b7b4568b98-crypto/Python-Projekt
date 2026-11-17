"""Gift Detective: Flask-Web-App für Geschenkempfehlungen."""
import os
import secrets
from flask import Flask, render_template, request, session
from gift_engine import (INTERESTS, RECIPIENTS, OCCASIONS, AGE_GROUPS,
                         STYLES, DEADLINES, EXCLUSIONS,
                         recommend, validate_preferences)

app = Flask(__name__)
# Render setzt SECRET_KEY. Lokal wird ein temporärer Schlüssel verwendet.
app.secret_key = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
app.config["MAX_CONTENT_LENGTH"] = 32 * 1024

OPTIONS = {"interests": INTERESTS, "recipients": RECIPIENTS,
           "occasions": OCCASIONS, "ages": AGE_GROUPS, "styles": STYLES,
           "deadlines": DEADLINES, "exclusions": EXCLUSIONS}


@app.get("/")
def home():
    token = session.setdefault("csrf", secrets.token_urlsafe(24))
    return render_template("index.html", options=OPTIONS, token=token, errors={},
                           values={"recipient": "freund", "occasion": "geburtstag",
                                   "age": "adult", "style": "praktisch", "deadline": "flexibel",
                                   "budget": 40, "interests": [], "avoid": []})


@app.post("/ideen")
def ideas():
    token = session.get("csrf", "")
    submitted = request.form.get("csrf", "")
    if not token or not secrets.compare_digest(token, submitted):
        return "Sitzung abgelaufen. Bitte lade die Startseite neu.", 400

    values, errors = validate_preferences(request.form)
    if errors:
        return (render_template("index.html", options=OPTIONS, values=values,
                                token=token, errors=errors), 400)

    results = recommend(values, limit=6)
    return render_template("results.html", options=OPTIONS,
                           preferences=values, suggestions=results)


@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1")
