class Zadanie:
    def __init__(self, tytul):
        self.tytul = tytul
        self.ukonczone = False

    def oznacz_jako_ukonczone(self):
        self.ukonczone = True

    def oznacz_jako_nieukonczone(self):
        self.ukonczone = False

    def edytuj(self, nowy_tytul):
        self.tytul = nowy_tytul


class ListaZadan:
    def __init__(self):
        self.zadania = []

    def dodaj_zadanie(self, tytul):
        """Dodaje nowe zadanie do listy"""
        zadanie = Zadanie(tytul)
        self.zadania.append(zadanie)
        print(f"Zadanie '{tytul}' dodane.")
        return zadanie

    def usun_zadanie(self, zadanie):
        """Usuwa zadanie z listy"""
        if zadanie in self.zadania:
            self.zadania.remove(zadanie)
            print(f"Zadanie '{zadanie.tytul}' usunięte.")
        else:
            print("Zadanie nie znalezione.")

    def pobierz_wszystkie_zadania(self):
        """Zwraca wszystkie zadania na liście"""
        return self.zadania

    def pobierz_ukonczone_zadania(self):
        """Zwraca tylko ukończone zadania"""
        return [zadanie for zadanie in self.zadania if zadanie.ukonczone]

    def pobierz_nieukonczone_zadania(self):
        """Zwraca tylko niewykonane zadania"""
        return [zadanie for zadanie in self.zadania if not zadanie.ukonczone]

    def wyswietl_zadania(self):
        """Wypisuje wszystkie zadania"""
        if not self.zadania:
            print("Brak zadań do wyświetlenia.")
            return
        for idx, zadanie in enumerate(self.zadania, 1):
            status = "Ukończone" if zadanie.ukonczone else "Niewykonane"
            print(f"{idx}. {zadanie.tytul} - {status}")

    def oznacz_zadanie_jako_ukonczone(self, index_zadania):
        """Oznacza zadanie jako ukończone"""
        try:
            zadanie = self.zadania[index_zadania]
            zadanie.oznacz_jako_ukonczone()
            print(f"Zadanie '{zadanie.tytul}' oznaczone jako ukończone.")
        except IndexError:
            print("Nieprawidłowy indeks zadania.")

    def oznacz_zadanie_jako_nieukonczone(self, index_zadania):
        """Oznacza zadanie jako niewykonane"""
        try:
            zadanie = self.zadania[index_zadania]
            zadanie.oznacz_jako_nieukonczone()
            print(f"Zadanie '{zadanie.tytul}' oznaczone jako niewykonane.")
        except IndexError:
            print("Nieprawidłowy indeks zadania.")

    def edytuj_zadanie(self, index_zadania, nowy_tytul):
        """Edytuje zadanie"""
        try:
            zadanie = self.zadania[index_zadania]
            zadanie.edytuj(nowy_tytul)
            print(f"Zadanie '{zadanie.tytul}' zostało zmienione na '{nowy_tytul}'.")
        except IndexError:
            print("Nieprawidłowy indeks zadania.")


def wyswietl_menu():
    """Wypisuje menu opcji"""
    print("\n--- Aplikacja ToDo ---")
    print("1. Dodaj zadanie")
    print("2. Usuń zadanie")
    print("3. Oznacz zadanie jako ukończone")
    print("4. Oznacz zadanie jako niewykonane")
    print("5. Edytuj zadanie")
    print("6. Wyświetl wszystkie zadania")
    print("7. Wyświetl zadania ukończone")
    print("8. Wyświetl zadania niewykonane")
    print("9. Zakończ")


def main():
    """Główna funkcja aplikacji"""
    lista_zadan = ListaZadan()

    while True:
        wyswietl_menu()
        wybor = input("Wybierz opcję: ")

        if wybor == '1':
            tytul = input("Wprowadź tytuł zadania: ")
            lista_zadan.dodaj_zadanie(tytul)

        elif wybor == '2':
            lista_zadan.wyswietl_zadania()
            try:
                index_zadania = int(input("Wprowadź numer zadania do usunięcia: ")) - 1
                lista_zadan.usun_zadanie(lista_zadan.zadania[index_zadania])
            except (IndexError, ValueError):
                print("Nieprawidłowy numer zadania.")

        elif wybor == '3':
            lista_zadan.wyswietl_zadania()
            try:
                index_zadania = int(input("Wprowadź numer zadania do oznaczenia jako ukończone: ")) - 1
                lista_zadan.oznacz_zadanie_jako_ukonczone(index_zadania)
            except (IndexError, ValueError):
                print("Nieprawidłowy numer zadania.")

        elif wybor == '4':
            lista_zadan.wyswietl_zadania()
            try:
                index_zadania = int(input("Wprowadź numer zadania do oznaczenia jako niewykonane: ")) - 1
                lista_zadan.oznacz_zadanie_jako_nieukonczone(index_zadania)
            except (IndexError, ValueError):
                print("Nieprawidłowy numer zadania.")

        elif wybor == '5':
            lista_zadan.wyswietl_zadania()
            try:
                index_zadania = int(input("Wprowadź numer zadania do edycji: ")) - 1
                nowy_tytul = input("Wprowadź nowy tytuł zadania: ")
                lista_zadan.edytuj_zadanie(index_zadania, nowy_tytul)
            except (IndexError, ValueError):
                print("Nieprawidłowy numer zadania.")

        elif wybor == '6':
            lista_zadan.wyswietl_zadania()

        elif wybor == '7':
            ukonczone_zadania = lista_zadan.pobierz_ukonczone_zadania()
            if not ukonczone_zadania:
                print("Brak ukończonych zadań.")
            for zadanie in ukonczone_zadania:
                print(f"- {zadanie.tytul}")

        elif wybor == '8':
            nieukonczone_zadania = lista_zadan.pobierz_nieukonczone_zadania()
            if not nieukonczone_zadania:
                print("Brak niewykonanych zadań.")
            for zadanie in nieukonczone_zadania:
                print(f"- {zadanie.tytul}")

        elif wybor == '9':
            print("Zakończono program.")
            break

        else:
            print("Nieprawidłowa opcja. Wybierz numer od 1 do 9.")


if __name__ == "__main__":
    main()
