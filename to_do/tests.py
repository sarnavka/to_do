import unittest
from to_do import ListaZadan, Zadanie

class TestListaZadan(unittest.TestCase):

    def setUp(self):
        """Inicjalizacja przed każdym testem"""
        self.lista = ListaZadan()

    # Testy dla funkcji dodaj_zadanie()
    def test_dodaj_zadanie_1(self):
        zadanie = self.lista.dodaj_zadanie("Kup mleko")
        self.assertIn(zadanie, self.lista.zadania)
        self.assertEqual(zadanie.tytul, "Kup mleko")
        self.assertFalse(zadanie.ukonczone)

    # Testy dla funkcji usun_zadanie()
    def test_usun_zadanie_1(self):
        zadanie = self.lista.dodaj_zadanie("Kup mleko")
        self.lista.usun_zadanie(zadanie)
        self.assertNotIn(zadanie, self.lista.zadania)

    # Testy dla funkcji oznacz_jako_ukonczone()
    def test_oznacz_jako_ukonczone_1(self):
        zadanie = self.lista.dodaj_zadanie("Kup mleko")
        zadanie.oznacz_jako_ukonczone()
        self.assertTrue(zadanie.ukonczone)

    # Testy dla funkcji oznacz_jako_nieukonczone()
    def test_oznacz_jako_nieukonczone_1(self):
        zadanie = self.lista.dodaj_zadanie("Kup mleko")
        zadanie.oznacz_jako_ukonczone()
        zadanie.oznacz_jako_nieukonczone()
        self.assertFalse(zadanie.ukonczone)

    # Testy dla funkcji edytuj()
    def test_edytuj_1(self):
        zadanie = self.lista.dodaj_zadanie("Kup mleko")
        zadanie.edytuj("Kup chleb")
        self.assertEqual(zadanie.tytul, "Kup chleb")

    # Testy dla funkcji pobierz_ukonczone_zadania()
    def test_pobierz_ukonczone_zadania_1(self):
        zadanie1 = self.lista.dodaj_zadanie("Kup mleko")
        zadanie1.oznacz_jako_ukonczone()
        ukonczone_zadania = self.lista.pobierz_ukonczone_zadania()
        self.assertIn(zadanie1, ukonczone_zadania)
        self.assertEqual(len(ukonczone_zadania), 1)

if __name__ == "__main__":
    unittest.main()
