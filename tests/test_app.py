import unittest
from werkzeug.datastructures import MultiDict

from app import app
from gift_engine import GIFTS, recommend, validate_preferences


GOOD_FORM = MultiDict([
    ("recipient", "freund"), ("age", "adult"), ("occasion", "geburtstag"),
    ("style", "praktisch"), ("budget", "40"), ("deadline", "flexibel"),
    ("interests", "lesen"), ("interests", "reisen"),
])


class GiftDetectiveTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def token(self):
        self.client.get("/")
        with self.client.session_transaction() as sess:
            return sess["csrf"]

    def test_startseite_zeigt_geschenkformular(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'name="budget"', response.data)
        self.assertIn(b'name="interests"', response.data)

    def test_empfehlungsliste_funktioniert(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.add("csrf", self.token())
        response = self.client.post("/ideen", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Ideen für dich".encode(), response.data)
        self.assertIn("Richtwert".encode(), response.data)

    def test_kaputte_budgetangabe_wird_abgelehnt(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.setlist("budget", ["-20"])
        data.add("csrf", self.token())
        response = self.client.post("/ideen", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Budget zwischen".encode(), response.data)

    def test_csrf_schutz(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.add("csrf", "falscher-wert")
        response = self.client.post("/ideen", data=data)
        self.assertEqual(response.status_code, 400)

    def test_budgets_werden_eingehalten(self):
        prefs, errors = validate_preferences(GOOD_FORM)
        self.assertFalse(errors)
        results = recommend(prefs)
        self.assertTrue(results)
        self.assertTrue(all(r["gift"].price <= 40 for r in results))

    def test_ausschluss_von_gutscheinen(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.add("avoid", "gutschein")
        prefs, errors = validate_preferences(data)
        self.assertFalse(errors)
        self.assertTrue(all("gutschein" not in r["gift"].exclude for r in recommend(prefs)))

    def test_kurzfristige_suche_filtert_geplante_erlebnisse(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.setlist("deadline", ["sofort"])
        prefs, errors = validate_preferences(data)
        self.assertFalse(errors)
        self.assertTrue(all(r["gift"].availability != "planbar" for r in recommend(prefs)))

    def test_gueltige_interessen_bevorzugt(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.setlist("interests", ["lesen"])
        prefs, _ = validate_preferences(data)
        results = recommend(prefs)
        self.assertIn("lesen", results[0]["gift"].interests)

    def test_ungueltige_interessen_abgefangen(self):
        data = MultiDict(GOOD_FORM.items(multi=True))
        data.add("interests", "__fake__")
        _, errors = validate_preferences(data)
        self.assertIn("interests", errors)

    def test_katalog_groesser_als_40(self):
        self.assertGreaterEqual(len(GIFTS), 40)

    def test_health(self):
        self.assertEqual(self.client.get("/health").status_code, 200)


if __name__ == "__main__":
    unittest.main()
