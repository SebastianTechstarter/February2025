import hashlib
from cryptography.fernet import Fernet

users_list = []


# Generiert einen Verschlüsselungsschlüssel (in einem realen Szenario sollte dieser sicher gespeichert werden)
key = Fernet.generate_key()
cipher = Fernet(key)


def encrypt_value(value):
    return cipher.encrypt(value.encode()).decode()


def decrypt_value(value):
    return cipher.decrypt(value.encode()).decode()


def hash_password(password):
    return hashlib.sha512(password.encode()).hexdigest()


def login(musername, mpassword):
    print(f"My Username: {musername} Password: {mpassword}")
    user = None
    hashed_password = hash_password(mpassword)
    for u in users_list:
        if u["username"] == musername and u["password"] == hashed_password:
            user = u
            break

    return user


def signup(musername, mpassword, credit_card):
    for u in users_list:
        if u["username"] == musername:
            print("User exists already, please Login")
            return

    new_user_id = len(users_list) + 1  # 1, 2,
    hashed_password = hash_password(mpassword)
    encrypted_credit_card = encrypt_value(credit_card)
    users_list.append(
        {
            "id": new_user_id,
            "username": musername,
            "password": hashed_password,
            "credit_card": encrypted_credit_card,
        }
    )


def buy_product(musername):
    user = None
    for u in users_list:
        if u["username"] == musername:
            user = u
            break
    credit_card_encryted = user["credit_card"]
    credit_card = decrypt_value(credit_card_encryted)
    print(f"User has bought the item with credit card {credit_card}")


# -------------------------------------

type = input("Was möchtest Du tun? (a/r): ")

username = input("Wie lautet Dein Login-Name? ")
password = input("Wie lautet Dein Passwort? ")

if type == "a":
    current_user = login(username, password)

    if current_user == None:
        print("Nutzer existiert nicht. Bitte registrieren!")
        exit()

    buy_product(current_user["credit_card"])

if type == "r":
    credit_card = input("Wie lautet die Kreditkarte? ")
    message = signup(username, password, credit_card)
    if message == None:
        print("Nutzer existiert. Bitte einloggen!")
        exit()

print(f"My Logged in user with {username} and {password} is {current_user}")
# ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae --> test123
# d9b5f58f0b38198293971865a14074f59eba3e82595becbe86ae51f1d9f1f65e --> Test123
# ecd71870d1963316a97e3ac3408c9835ad8cf0f3c1bc703527c30265534f75ae
# daef4953b9783365cad6615223720506cc46c5167cd16ab500fa597aa08ff964eb24fb19687f34d7665f778fcb6c5358fc0a5b81e1662cf90f73a2671c53f991
