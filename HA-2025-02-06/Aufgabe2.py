from cryptography.fernet import (
    Fernet,
)  # aus dem Paket cryptography wird das Modul Fernet importiert.

# Generiert einen Verschlüsselungsschlüssel (in einem realen Szenario sollte dieser sicher gespeichert werden)
key = (
    Fernet.generate_key()
)  # die Variable key erhält einen Schlüssel zur Verschlüsselung (Sagt man das so? Klingt irgendwie nicht sinnvoll.)

cipher = Fernet(key)  # Definition des Verschlüsselungsobjekts

# Simulierte Datenbank
users = (
    []
)  # aktuell ist die User-Liste noch leer. Hier legen wir ein Dictionary an, um die User zu hinterlegen.


def encrypt_password(
    password,
):  # Definition der Funktion zum Verschlüsseln des Passworts
    return cipher.encrypt(password.encode()).decode()  # Das Passwort wird verschlüsselt


def decrypt_password(
    encrypted_password,
):  # Definition der Funktion zum Entschlüsseln des Passworts.
    return cipher.decrypt(
        encrypted_password.encode()
    ).decode()  # Das Passwort wird entschlüsselt.


def login(musername, mpassword):  # Definition der Login-Funktion
    # Geht durch die Benutzerliste auf der Suche nach dem Benutzernamen und dem entsprechenden Passwort
    # Das eingegebene Passwort muss mit dem entschlüsselten Passwort übereinstimmen
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    for u in users:
        if u["username"] == musername and decrypt_password(u["password"]) == mpassword:
            user = u
    return user  # Gibt daraufhin den entsprechenden User bei Übereinstimmung zurück.


def signup(musername, mpassword):  # Defintion der Registrieren-Funktion
    # Generiert eine neue User-ID, die der Anzahl an bisherigen Usern+1 entspricht.
    new_user_id = len(users) + 1
    encrypted_password = encrypt_password(mpassword)
    # Neuer User wird an das User-Dictionary mit verschlüsseltem Passwort angehängt.
    users.append(
        {"id": new_user_id, "username": musername, "password": encrypted_password}
    )


# Eigentlicher Start des Programms
username = input("Wie lautet dein login Name: ")  # Programm fragt nach Username
password = input("Wie lautet dein password: ")  # Programm fragt nach dem Passwort

signup(username, password)  # User wird zuerst registriert
current_user = login(
    username, password
)  # Danach versucht das Programm, den Nutzer mit den eigegebenen Daten einzuloggen.
# Gibt danach den angemeldeten User aus.
print(f"My Logged in user with {username} and {password} is {current_user}")
