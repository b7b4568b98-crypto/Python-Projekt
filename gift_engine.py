"""Der Empfehlungsalgorithmus für Gift Detective.

Keine KI, keine externen Shopping-APIs: transparente Regeln + Beispielgeschenke.
Alle Preise sind frei gewählte Richtwerte, keine aktuellen Händlerangebote.
"""
from dataclasses import dataclass


INTERESTS = {
    "lesen": "Bücher & Lesen", "kochen": "Kochen & Backen",
    "sport": "Sport & Bewegung", "reisen": "Reisen & Entdecken",
    "kreativ": "Kreativ & DIY", "technik": "Technik & Gadgets",
    "musik": "Musik", "gaming": "Gaming",
    "wellness": "Entspannung & Wellness", "natur": "Natur & Outdoor",
    "pflanzen": "Pflanzen", "mode": "Mode & Accessoires",
    "kaffee": "Kaffee & Tee", "essen": "Essen & Genießen",
    "fotografie": "Fotografie", "spiele": "Spiele & Rätsel",
}
RECIPIENTS = {
    "partner": "Partner:in", "freund": "Freund:in", "mama": "Mama",
    "papa": "Papa", "geschwister": "Geschwister", "grosseltern": "Großeltern",
    "kind": "Kind / Teenager", "kollegin": "Kolleg:in", "andere": "Andere Person",
}
OCCASIONS = {
    "geburtstag": "Geburtstag", "weihnachten": "Weihnachten",
    "danke": "Dankeschön", "jubilaeum": "Jubiläum", "einzug": "Einzug",
    "einfach_so": "Einfach so",
}
AGE_GROUPS = {
    "kind": "Bis 12 Jahre", "teen": "13–17 Jahre",
    "adult": "18–39 Jahre", "mid": "40–59 Jahre", "senior": "60+ Jahre",
}
STYLES = {
    "praktisch": "Praktisch", "persoenlich": "Persönlich",
    "erlebnis": "Erlebnis", "kreativ": "Originell & kreativ",
}
DEADLINES = {"sofort": "Heute oder morgen", "bald": "In wenigen Tagen", "flexibel": "Ich habe Zeit"}
EXCLUSIONS = {
    "gutschein": "Keine Gutscheine", "essen": "Nichts Essbares",
    "deko": "Keine Deko", "diy": "Nichts Selbstgemachtes",
}


@dataclass(frozen=True)
class Gift:
    title: str
    description: str
    price: int
    category: str
    interests: tuple[str, ...]
    styles: tuple[str, ...]
    availability: str = "laden"  # sofort = selbst machbar, laden = im Laden denkbar, planbar = vorher organisieren
    exclude: tuple[str, ...] = ()
    audience: tuple[str, ...] = ()
    ages: tuple[str, ...] = ()
    occasions: tuple[str, ...] = ()


def gift(title, desc, price, category, interests, styles, *, availability="laden",
         exclude=(), audience=(), ages=(), occasions=()):
    return Gift(title, desc, price, category, tuple(interests), tuple(styles),
                availability, tuple(exclude), tuple(audience), tuple(ages), tuple(occasions))


GIFTS = [
    gift("Buch mit persönlicher Widmung", "Ein Buch aus dem Lieblingsgenre und eine handgeschriebene Nachricht auf der ersten Seite.", 17, "Lesen", ["lesen"], ["persoenlich", "praktisch"]),
    gift("Leselampe mit Clip", "Kompakte Lampe zum Lesen im Bett oder auf Reisen.", 19, "Lesen", ["lesen", "reisen"], ["praktisch"]),
    gift("Buchladen-Gutschein", "Die beschenkte Person sucht sich ihr nächstes Lieblingsbuch selbst aus.", 20, "Lesen", ["lesen"], ["praktisch"], exclude=["gutschein"]),
    gift("Lesezeichen mit Erinnerung", "Ein Foto oder Spruch als selbstgestaltetes Lesezeichen.", 4, "Lesen", ["lesen", "kreativ"], ["persoenlich", "kreativ"], availability="sofort", exclude=["diy"]),
    gift("Gewürz-Tasting-Set", "Eine Auswahl ungewöhnlicher Gewürze für neue Kochideen.", 24, "Genuss", ["kochen", "essen"], ["praktisch", "kreativ"], exclude=["essen"]),
    gift("Rezeptbuch mit eigenen Favoriten", "Eine kleine Sammlung erprobter Rezepte mit persönlichen Tipps.", 8, "Genuss", ["kochen", "essen", "kreativ"], ["persoenlich", "kreativ"], availability="sofort", exclude=["diy"]),
    gift("Gemeinsamer Kochabend", "Ein geplanter Abend mit Wunschgericht, Einkauf und Küchenmusik.", 22, "Erlebnis", ["kochen", "essen"], ["erlebnis", "persoenlich"], availability="planbar", exclude=["essen"], audience=["partner", "freund", "geschwister"]),
    gift("Schönes Küchenutensil", "Ein hochwertiger Teigschaber oder eine praktische Reibe für Hobbyköch:innen.", 16, "Genuss", ["kochen"], ["praktisch"]),
    gift("Picknick mit Lieblingssnacks", "Eine gemeinsame Auszeit draußen, liebevoll vorbereitet.", 18, "Erlebnis", ["natur", "essen", "reisen"], ["erlebnis", "persoenlich"], availability="sofort", exclude=["essen"]),
    gift("Wander-Trinkflasche", "Robuste Flasche für Ausflüge, Wanderungen und Sport.", 21, "Outdoor", ["natur", "sport", "reisen"], ["praktisch"]),
    gift("Mini-Kräutergarten", "Ein kleines Set zum Ziehen frischer Kräuter am Fenster.", 15, "Pflanzen", ["pflanzen", "kochen", "natur"], ["praktisch", "kreativ"]),
    gift("Pflanzen-Stecklingsset", "Schöne Stecklinge mit handgeschriebenen Pflegetipps.", 7, "Pflanzen", ["pflanzen", "natur"], ["persoenlich", "kreativ"], availability="sofort", exclude=["diy"]),
    gift("Keramiktopf für Lieblingspflanze", "Ein besonderer Übertopf passend zum Zuhause.", 18, "Pflanzen", ["pflanzen", "mode"], ["praktisch", "kreativ"], exclude=["deko"], occasions=["einzug"]),
    gift("Reisejournal", "Ein schönes Notizbuch für Erinnerungen, Routen und kleine Entdeckungen.", 14, "Reisen", ["reisen", "kreativ", "fotografie"], ["praktisch", "persoenlich"]),
    gift("Kompaktes Reisespiel", "Ein leichtes Spiel für Zugfahrten, Urlaub und spontane Abende.", 13, "Spiele", ["reisen", "spiele"], ["praktisch", "erlebnis"]),
    gift("Reise-Organizer", "Taschen für Kabel, Tickets und Kleinteile unterwegs.", 23, "Reisen", ["reisen", "technik"], ["praktisch"]),
    gift("Konzertkarten", "Tickets für ein passendes Konzert oder einen kleinen Live-Auftritt.", 45, "Erlebnis", ["musik", "reisen"], ["erlebnis"], availability="planbar", audience=["partner", "freund", "geschwister"]),
    gift("Persönliche Playlist mit Cover", "Eine Playlist mit gemeinsamem Soundtrack und selbstgestaltetem Cover.", 0, "Persönlich", ["musik", "kreativ"], ["persoenlich", "kreativ"], availability="sofort", exclude=["diy"]),
    gift("Vinyl- oder CD-Fundstück", "Ein Album der Lieblingsband oder eine spannende Neuentdeckung.", 25, "Musik", ["musik"], ["persoenlich", "praktisch"]),
    gift("Mini-Bluetooth-Lautsprecher", "Kleiner Begleiter für Musik im Zimmer oder unterwegs.", 38, "Technik", ["musik", "technik", "reisen"], ["praktisch"]),
    gift("Kabel- und Gadget-Organizer", "Ordnung für Ladegeräte, Kopfhörer und kleines Technikzubehör.", 17, "Technik", ["technik", "reisen", "gaming"], ["praktisch"]),
    gift("Handy-Ständer für Schreibtisch", "Praktische Halterung für Videoanrufe, Rezepte oder Filme.", 11, "Technik", ["technik", "gaming", "kochen"], ["praktisch"]),
    gift("Digitaler Spiele-Gutschein", "Guthaben für die bevorzugte Gaming-Plattform – vorher Plattform prüfen.", 20, "Gaming", ["gaming", "technik"], ["praktisch"], availability="sofort", exclude=["gutschein"], ages=["teen", "adult", "mid"]),
    gift("Gaming-Mauspad", "Große, angenehme Unterlage für den Gaming-Schreibtisch.", 19, "Gaming", ["gaming", "technik"], ["praktisch"], ages=["teen", "adult", "mid"]),
    gift("Rätselbox", "Knifflige Rätsel zum Auspacken, Tüfteln und Entdecken.", 25, "Spiele", ["spiele", "gaming"], ["erlebnis", "kreativ"]),
    gift("Gesellschaftsspiel für kleine Gruppen", "Ein Spiel für gemeinsame Abende statt eines weiteren Gegenstands fürs Regal.", 27, "Spiele", ["spiele", "essen"], ["erlebnis", "praktisch"]),
    gift("Escape-Room-Besuch", "Ein Rätselerlebnis für zwei oder mehr Personen.", 60, "Erlebnis", ["spiele", "gaming"], ["erlebnis"], availability="planbar", audience=["partner", "freund", "geschwister"]),
    gift("Mini-Aquarellset", "Kompakte Farben und Papier für kreative Auszeiten.", 22, "Kreativ", ["kreativ", "natur"], ["kreativ", "praktisch"]),
    gift("Workshop-Gutschein", "Zum Beispiel für Keramik, Malen, Kochen oder einen DIY-Kurs.", 49, "Erlebnis", ["kreativ", "kochen"], ["erlebnis", "kreativ"], availability="planbar", exclude=["gutschein"]),
    gift("Schöne Woll- oder Häkelmaterialien", "Ein kleines Materialpaket für das nächste Kreativprojekt.", 25, "Kreativ", ["kreativ", "mode"], ["praktisch", "persoenlich"]),
    gift("Fotoabzüge mit Mini-Geschichte", "Drei bis fünf gemeinsame Fotos, mit einer kleinen Geschichte zu jedem Bild.", 6, "Persönlich", ["fotografie", "kreativ", "reisen"], ["persoenlich", "kreativ"], availability="sofort", exclude=["diy"]),
    gift("Fotobuch voller Erinnerungen", "Ein gestaltetes Album mit euren schönsten gemeinsamen Momenten.", 32, "Persönlich", ["fotografie", "reisen"], ["persoenlich", "kreativ"], availability="planbar", exclude=["diy"], audience=["partner", "freund", "mama", "papa", "grosseltern"]),
    gift("Gemeinsamer Foto-Spaziergang", "Ein Spaziergang mit kleinen Foto-Challenges und anschließender Bildauswahl.", 0, "Erlebnis", ["fotografie", "natur", "kreativ"], ["erlebnis", "persoenlich"], availability="sofort"),
    gift("Sofortbild-Fotoalbum", "Ein kleines Album für Erinnerungen mit Platz für Beschriftungen.", 18, "Fotografie", ["fotografie", "reisen"], ["persoenlich", "praktisch"]),
    gift("Tee-Probierset", "Mehrere spannende Teesorten zum gemeinsamen Probieren.", 17, "Genuss", ["kaffee", "wellness", "essen"], ["praktisch", "persoenlich"], exclude=["essen"]),
    gift("Besondere Kaffeebohnen", "Eine kleine Auswahl für jemanden, der gerne neue Röstungen entdeckt.", 18, "Genuss", ["kaffee", "essen"], ["praktisch"], exclude=["essen"]),
    gift("Wiederverwendbarer Thermobecher", "Für den Lieblingskaffee oder Tee unterwegs.", 24, "Alltag", ["kaffee", "reisen", "natur"], ["praktisch"]),
    gift("Entspannungsabend als Gutschein", "Du organisierst einen ruhigen Abend mit Musik, Getränken und einer Auszeit.", 10, "Wellness", ["wellness", "musik"], ["persoenlich", "erlebnis"], availability="sofort", exclude=["gutschein", "diy"]),
    gift("Wärmflasche mit weichem Bezug", "Kuschelige Begleitung für entspannte Abende.", 21, "Wellness", ["wellness"], ["praktisch", "persoenlich"]),
    gift("Wellness-Tageskarte", "Ein Gutschein für Therme oder Spa – Ort und Konditionen vorher prüfen.", 45, "Erlebnis", ["wellness"], ["erlebnis"], availability="planbar", exclude=["gutschein"]),
    gift("Yoga- oder Stretching-Set", "Ein einfaches Zubehörpaket für Bewegung zu Hause.", 28, "Sport", ["sport", "wellness"], ["praktisch"]),
    gift("Sporthandtuch mit Tasche", "Kompakt und praktisch für Training oder Ausflüge.", 16, "Sport", ["sport", "reisen"], ["praktisch"]),
    gift("Fahrrad-Ausflugsplanung", "Eine schöne Strecke mit Pausen und einem gemeinsamen Stopp planen.", 3, "Erlebnis", ["sport", "natur", "reisen"], ["erlebnis", "persoenlich"], availability="sofort"),
    gift("Schlichter Schal", "Ein vielseitiges Accessoire in einer passenden Lieblingsfarbe.", 29, "Mode", ["mode"], ["praktisch", "persoenlich"]),
    gift("Schmuckschale", "Ein kleiner Platz für Ringe, Ketten oder Schlüssel.", 16, "Mode", ["mode", "kreativ"], ["praktisch", "kreativ"], exclude=["deko"]),
    gift("Personalisierter Schlüsselanhänger", "Mit Initialen, einem gemeinsamen Insider oder einem kleinen Foto.", 12, "Persönlich", ["mode", "reisen"], ["persoenlich"], availability="planbar"),
    gift("Mini-Erinnerungsglas", "Ein Glas voller Komplimente, gemeinsamer Erinnerungen oder Mini-Gutscheine.", 5, "Persönlich", ["kreativ"], ["persoenlich", "kreativ"], availability="sofort", exclude=["diy"], audience=["partner", "freund", "mama", "papa", "geschwister", "grosseltern"]),
    gift("Handgeschriebener Brief", "Ein persönlicher Brief darüber, was du an der Person schätzt.", 0, "Persönlich", ["kreativ"], ["persoenlich"], availability="sofort", exclude=["diy"]),
    gift("Gemeinsamer Museumsbesuch", "Eine Ausstellung passend zu den Interessen plus Zeit für ein Gespräch.", 24, "Erlebnis", ["kreativ", "fotografie", "reisen"], ["erlebnis", "persoenlich"], availability="planbar"),
    gift("Kleine Genussbox", "Eine individuell zusammengestellte Box aus Lieblingssnacks und Getränken.", 20, "Genuss", ["essen", "kaffee"], ["persoenlich", "kreativ"], availability="sofort", exclude=["essen", "diy"]),
    gift("Blumen mit persönlicher Karte", "Ein kleiner Strauß mit einem guten, konkreten Dankeschön.", 15, "Persönlich", ["pflanzen", "natur"], ["persoenlich"], availability="laden", exclude=["deko"], occasions=["danke", "einfach_so"]),
    gift("Kleine Rätsel-Postkarte", "Eine selbst ausgedachte Mini-Schnitzeljagd auf Papier.", 2, "Kreativ", ["spiele", "kreativ"], ["kreativ", "persoenlich"], availability="sofort", exclude=["diy"]),
    gift("Mini-Pflanzenbestimmungsbuch", "Ein kleiner Begleiter für die nächste Naturentdeckung.", 12, "Natur", ["natur", "pflanzen", "lesen"], ["praktisch"]),
    gift("Kinder-Bastelbox", "Materialien für ein altersgerechtes Kreativprojekt.", 19, "Kreativ", ["kreativ", "spiele"], ["kreativ", "erlebnis"], ages=["kind"]),
    gift("Kinder-Experimentierset", "Ein kleines altersgerechtes Set zum Beobachten und Ausprobieren.", 27, "Spiele", ["technik", "natur", "spiele"], ["erlebnis", "kreativ"], ages=["kind"]),
]


def validate_preferences(form):
    """Bereitet Eingaben auf und verhindert ungültige Werte."""
    errors = {}
    choices = {
        "recipient": RECIPIENTS, "occasion": OCCASIONS,
        "age": AGE_GROUPS, "style": STYLES, "deadline": DEADLINES,
    }
    result = {}
    for field, options in choices.items():
        value = form.get(field, "")
        if value not in options:
            errors[field] = "Bitte wähle eine gültige Option."
        result[field] = value

    raw_budget = form.get("budget", "")
    try:
        budget = int(raw_budget)
        if not 5 <= budget <= 500:
            raise ValueError
    except (ValueError, TypeError):
        errors["budget"] = "Bitte wähle ein Budget zwischen 5 und 500 €."
        budget = 30
    result["budget"] = budget

    interests = list(dict.fromkeys(form.getlist("interests")))
    if len(interests) > 16 or any(item not in INTERESTS for item in interests):
        errors["interests"] = "Bitte wähle gültige Interessen."
    result["interests"] = interests

    avoid = list(dict.fromkeys(form.getlist("avoid")))
    if any(item not in EXCLUSIONS for item in avoid):
        errors["avoid"] = "Bitte wähle gültige Ausschlüsse."
    result["avoid"] = avoid
    return result, errors


def recommend(preferences, limit=6):
    """Filtert ungeeignete Geschenke, bewertet Treffer und mischt Kategorien.

    Rückgabe: Liste von Dictionaries mit Geschenk, Punktwert und Begründungen.
    Die Punktwerte sind *interne Rangwerte*, keine wissenschaftlichen Prozentwerte.
    """
    ranked = []
    age, deadline = preferences["age"], preferences["deadline"]
    selected_interests = set(preferences["interests"])
    for idea in GIFTS:
        if idea.price > preferences["budget"] or set(idea.exclude) & set(preferences["avoid"]):
            continue
        if idea.ages and age not in idea.ages:
            continue
        if deadline == "sofort" and idea.availability == "planbar":
            continue
        # Auch bei wenigen Tagen keine Ideen empfehlen, die längere Planung benötigen.
        if deadline == "bald" and idea.availability == "planbar":
            continue

        score = 1
        reasons = []
        matches = selected_interests.intersection(idea.interests)
        if matches:
            score += min(len(matches), 2) * 6
            reasons.append("Passt zu " + ", ".join(INTERESTS[i] for i in sorted(matches)[:2]))
        if preferences["style"] in idea.styles:
            score += 5
            reasons.append("Passt zum gewünschten Geschenkstil")
        if idea.audience and preferences["recipient"] in idea.audience:
            score += 3
            reasons.append("Gut für diese Beziehung")
        if idea.occasions and preferences["occasion"] in idea.occasions:
            score += 3
            reasons.append("Passt zum Anlass")
        if not idea.ages or age in idea.ages:
            score += 1
        if idea.price >= preferences["budget"] * 0.45:
            score += 1
        if deadline in {"sofort", "bald"} and idea.availability == "sofort":
            score += 2
            reasons.append("Auch kurzfristig umsetzbar")
        if not reasons:
            reasons.append("Bleibt innerhalb deines Budgets")
        ranked.append({"gift": idea, "score": score, "reasons": reasons[:3]})

    # Ohne Interesse gemischte Treffer; bei Interessen Treffer deutlich priorisieren.
    ranked.sort(key=lambda item: (-item["score"], item["gift"].price, item["gift"].title))
    result, used_categories = [], set()
    for item in ranked:
        if item["gift"].category not in used_categories:
            result.append(item)
            used_categories.add(item["gift"].category)
            if len(result) == limit:
                return result
    for item in ranked:
        if item not in result:
            result.append(item)
            if len(result) == limit:
                break
    return result
