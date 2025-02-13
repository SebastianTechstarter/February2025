# Tic Tac Toe in Python

# Spielfeld initialisieren
board = [" " for _ in range(9)]  # Ein 3x3-Gitter als Liste (9 Felder)


# Das Spielfeld anzeigen
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Überprüfen, ob ein Spieler gewonnen hat
def check_winner(player):
    win_conditions = [
        (0, 1, 2),  # Erste Reihe
        (3, 4, 5),  # Zweite Reihe
        (6, 7, 8),  # Dritte Reihe
        (0, 3, 6),  # Erste Spalte
        (1, 4, 7),  # Zweite Spalte
        (2, 5, 8),  # Dritte Spalte
        (0, 4, 8),  # Diagonale
        (2, 4, 6),  # Diagonale
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


# Überprüfen, ob das Spielfeld voll ist (Unentschieden)
def check_draw():
    return " " not in board


# Funktion für den Zug eines Spielers
def player_turn(player):
    while True:
        try:
            move = int(input(f"Spieler {player}, wähle ein Feld (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Ungültige Eingabe! Wähle eine Zahl zwischen 1 und 9.")
            elif board[move] != " ":
                print("Dieses Feld ist bereits belegt!")
            else:
                board[move] = player
                break
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben.")


# Hauptspielfunktion
def tic_tac_toe():
    current_player = "X"  # Spieler X beginnt
    while True:
        print_board()
        player_turn(current_player)

        if check_winner(current_player):
            print_board()
            print(f"Spieler {current_player} hat gewonnen!")
            break
        elif check_draw():
            print_board()
            print("Unentschieden!")
            break

        # Wechseln zum anderen Spieler
        current_player = "O" if current_player == "X" else "X"


# Spiel starten
tic_tac_toe()

# Die Lösung wurde zu 80% durch google udn youtube erstellt. Forallem das Spielfeld erstellen habe ich übernommen.
# Die Idee stammt aus dem Link in der Aufgabe. Das Lösen wurde über youtube erklärt.
