

# MINI PROJECT TIC TAC TOE -------------------------------------------

# Function to display the Tic Tac Toe board --------------------------
def display_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")
# --------------------------------------------------------------------


# Function to get the position from the player -----------------------
def player_input(player):
    position = input(f"Player {player}, enter the position (1 to 9): ")
    while not position.isdigit() or int(position) < 1 or int(position) > 9:
        position = input("Invalid input. Please enter a valid position (1 to 9): ")
    return int(position)
# --------------------------------------------------------------------


# Function to check if there is a winner -----------------------------
def check_win(board):
    winning_combinations = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
    ]

    for combination in winning_combinations:
        positions = [board[row][col] for row, col in combination]
        if all(position == "X" for position in positions):
            return "X"
        elif all(position == "O" for position in positions):
            return "O"
    return None
# ----------------------------------------------------------------------


# The main function to play the game -----------------------------------
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    moves_left = 9

    print("Let's play Tic Tac Toe!")
    display_board(board)

    while moves_left > 0:
        position = player_input(current_player)
        row = (position - 1) // 3
        col = (position - 1) % 3

        if board[row][col] == " ":
            board[row][col] = current_player
            moves_left -= 1
            display_board(board)

            if check_win(board):
                print(f"Player {current_player} wins!")
                return

            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    print("It's a tie!")
# ----------------------------------------------------------------------


# Start the game (and enjoy !) -----------------------------------------
play()
