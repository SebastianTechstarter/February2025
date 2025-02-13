class Birthday:
    def __init__(self):
        # Vordefiniertes Dictionary mit Geburtstagen
        self.birthdays = {
            "Goethe": "28.08.1749",
            "Schiller": "10.11.1759",
            "Einstein": "14.03.1879",
        }

    def get_birthday(self, name):
        return self.birthdays.get(name, "Geburtstag nicht gefunden.")

    def add_birthday(self, name, date):
        self.birthdays[name] = date
        print(f"Geburtstag für {name} hinzugefügt/aktualisiert.")

    def list_birthdays(self):
        print("Gespeicherte Geburtstage:")
        for name, date in self.birthdays.items():
            print(f"{name}: {date}")


# Nutzung der Geburtstagsbibliothek
library = Birthday()

# Liste der Geburtstage anzeigen
library.list_birthdays()

# Geburtstag von Goethe abrufen
print("Goethes Geburtstag:", library.get_birthday("Goethe"))

# Neuen Geburtstag hinzufügen
library.add_birthday("Newton", "04.01.1643")

# Aktualisierte Geburtstagsliste anzeigen
library.list_birthdays()
