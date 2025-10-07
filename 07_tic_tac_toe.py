# -----------------------------------------
# 🎮 Tic Tac Toe Game
# -----------------------------------------

# Initialize board
board = [" " for _ in range(9)]

# Function to print the board neatly
def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

# All possible win conditions
win_conditions = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]

# Check if a player has won
def check_winner(player):
    for combo in win_conditions:
        if all(board[i] == player for i in combo):
            return True
    return False

# Main game loop
while True:
    choice = input("Do you want to play Tic Tac Toe? (y/n): ").lower()
    if choice == "n":
        print("👋 Understandable, have a nice day ❤️")
        break
    elif choice != "y":
        print("⚠️ Invalid input. Please enter 'y' or 'n'.")
        continue

    # Reset board for a new game
    board = [" " for _ in range(9)]
    current_player = "O"
    moves = 0

    print("\nStarting a new game of Tic Tac Toe!")
    print("Use numbers 0–8 to choose a slot:\n")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 \n")

    # Game loop
    while moves < 9:
        print_board()
        try:
            pos = int(input(f"Player {current_player}, choose a slot (0–8): "))
            if pos < 0 or pos > 8:
                print("❌ Invalid slot! Pick a number between 0–8.")
                continue
            if board[pos] != " ":
                print("⚠️ Slot already taken! Choose another.")
                continue

            # Place move
            board[pos] = current_player
            moves += 1

            # Check for win
            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} wins! 🏆")
                break

            # Switch player
            current_player = "X" if current_player == "O" else "O"

        except ValueError:
            print("⚠️ Please enter a valid number (0–8).")

    else:
        print_board()
        print("🤝 It's a draw!")
