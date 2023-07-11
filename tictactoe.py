def print_board(board):
    """
    Prints the current state of the board.
    """
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")


def check_winner(board, player):
    """
    Checks if the specified player has won the game.
    """
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def play_game():
    """
    Runs the Tic Tac Toe game.
    """
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    print_board(board)
    while True:
        row = int(input("Enter row (0-2) for " + current_player + ": "))
        col = int(input("Enter column (0-2) for " + current_player + ": "))
        if board[row][col] != " ":
            print("Invalid move, try again.")
            continue
        board[row][col] = current_player
        print_board(board)
        if check_winner(board, current_player):
            print(current_player, "wins!")
            break
        if " " not in [cell for row in board for cell in row]:
            print("Tie game!")
            break
        current_player = players[(players.index(current_player) + 1) % 2]

play_game()
