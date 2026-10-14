board = [" "] * 9

wins = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def winner(b, p):
    return any(all(b[i] == p for i in line) for line in wins)

def minimax(b, is_max):
    if winner(b, "O"):
        return 1
    if winner(b, "X"):
        return -1
    if " " not in b:
        return 0

    scores = []
    for i in range(9):
        if b[i] == " ":
            b[i] = "O" if is_max else "X"
            scores.append(minimax(b, not is_max))
            b[i] = " "

    return max(scores) if is_max else min(scores)

def best_move():
    best_score = -float("inf")
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score, move = score, i

    return move

def display():
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        if i < 6:
            print("--+---+--")

while True:
    display()
    pos = int(input("Enter your position (1-9): ")) - 1

    if pos not in range(9) or board[pos] != " ":
        print("Invalid move!")
        continue

    board[pos] = "X"

    if winner(board, "X"):
        display()
        print("You win!")
        break
    if " " not in board:
        display()
        print("Draw!")
        break

    move = best_move()
    board[move] = "O"
    print("Computer chose:", move + 1)

    if winner(board, "O"):
        display()
        print("Computer wins!")
        break
    if " " not in board:
        display()
        print("Draw!")
        break