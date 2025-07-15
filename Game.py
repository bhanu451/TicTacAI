import math

# Constants for the players and the board
HUMAN = 'X'  # Human player
AI = 'O'     # AI player
EMPTY = ' '  # Empty cell on the board

# Initialize the Tic-Tac-Toe board
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]

def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print('| ' + ' | '.join(row) + ' |')
    print()

def check_winner(board):
    """Checks if there is a winner or a draw."""
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if EMPTY in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to find the best move."""
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    """Finds the best move for the AI."""
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False)
                board[i][j] = EMPTY
                if move_val > best_val:
                    best_val = move_val
                    move = (i, j)
    return move

def make_move(board, row, col, player):
    """Makes a move on the board."""
    if board[row][col] == EMPTY:
        board[row][col] = player
        return True
    return False

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    current_player = HUMAN
    while True:
        print_board(board)
        if check_winner(board):
            print(f"{check_winner(board)} wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        if current_player == HUMAN:
            # Human's turn
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if make_move(board, row, col, HUMAN):
                current_player = AI
            else:
                print("Invalid move, try again.")
        else:
            # AI's turn
            row, col = best_move(board)
            make_move(board, row, col, AI)
            current_player = HUMAN

# Run the Tic-Tac-Toe game
tic_tac_toe()
