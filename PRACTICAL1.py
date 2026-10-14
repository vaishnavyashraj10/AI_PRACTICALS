board = [" "] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

def check_win(p):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == p for i in line)
               for line in wins)

player = "X"

while True:
    display()
    try:
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1
    except ValueError:
        print("Enter a number from 1 to 9.")
        continue

    if pos not in range(9) or board[pos] != " ":
        print("Invalid position!")
        continue

    board[pos] = player

    if check_win(player):
        display()
        print(player, "wins!")
        break

    if " " not in board:
        display()
        print("Draw!")
        break

    player = "O" if player == "X" else "X"
    