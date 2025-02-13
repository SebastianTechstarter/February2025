Aufgabe: Heute Vormittag haben wir prinzipien zur Verschlüsselung behandelt und anhand

einer Praxisaufgabe vertieft. Bearbeitet den Rest dieser Aufgabe, falls ihr nicht fertig
geworden seid.
Dabei haben wir mithilfe des AES-256 eine Datei mithilfe einer Schlüsseldatei verschlüsselt.
Orientiert euch bei dieser Praxisaufgabe an dieser Anleitung.
Nun wollen wir eine Verschlüsselung mit Hilfe eines individuellen Passworts erstellen
● Erstelle eine Datei sicher.txt mit einem Beispieltext.
● Verschlüssele sie mit AES-256 unter Verwendung eines selbst gewählten
Passworts, anstatt einer Key-Datei.
● Entschlüssele die Datei wieder.
● Erkläre in 1-2 Sätzen, warum diese Methode unsicherer ist als eine
Verschlüsselung mit einem zufälligen SSL-Key.
💡 Tipp: Nutze -pass pass:DeinPasswort anstelle von -pass file:key.txt.

Beantworte außerdem folgende Fragen:
● Warum wird für die Verschlüsselung ein „Salt“ hinzugefügt?
● Was passiert, wenn der symmetrische Schlüssel verloren geht?

# Lösung
- Ein Passwort ist unsicherer als eine Verschlüsselung mit einem zufälligen SSL-Key, da Passwörter leichter erraten werden können. Ein zufällig generierter Schlüssel bietet mehr Sicherheit, da dieser nicht mit Wörterbuch- oder Brute-Force-Angriffen geknackt werden kann.

- Ein "Salt" wird genutzt, um identische Passwörter zu vermeiden. Wenn zweimal dasselbe Passwort generiert wird, so wird ein einzelnes Zeichen ausgetauscht.

- Wenn der Schlüssel verloren geht, können die Daten nicht mehr entschlüsselt werden. Der Schlüssel wird nämlich sowohl für Verschlüsselung als auch die Entschlüsselung gebraucht wird.