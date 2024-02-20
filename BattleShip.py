from random import randint

# Function to create the game board
def create_board(size):
    return [['O' for _ in range(size)] for _ in range(size)]

# Function to print the game board
def print_board(board):
    for row in board:
        print(" ".join(row))

# Function to generate a random row and column for the ship
def generate_random_location(board):
    return randint(0, len(board))

# Function to check if the player's guess is valid
def is_valid_guess(board, guess_row, guess_col):
    return 0 <= guess_row < len(board) and 0 <= guess_col < len(board)

# Main game function
def battleship_game(num_ships):
    size = 7 + (num_ships-1) * 2  # Calculate board size based on the number of ships
    attempts = 3 + num_ships * 2  # Calculate the maximum number of attempts
    
    print(f"Welcome to Battleship with {num_ships} ship(s)!")
    print(f"You have {attempts} attempts to find the ship(s).")
    
    board = create_board(size)
    
    # Generate random ship locations
    ships = [(generate_random_location(board), generate_random_location(board)) for _ in range(num_ships)]
    ship_value = num_ships
    for turn in range(attempts):
        print("\nTurn", turn + 1)
        print_board(board)
        while True:
            try:
                guess_row = int(input(f"Guess Row (0 to {size - 1}): "))
                guess_col = int(input(f"Guess Col (0 to {size - 1}): "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        if not is_valid_guess(board, guess_row, guess_col):
            print("Oops, that's not even in the ocean.")
            continue
        
        if (guess_row, guess_col) in ships:
            print("Congratulations! You sank my battleship!")
            ship_value -= 1
            if ship_value == 0:
                board[guess_row][guess_col] = "X"
                ("Congratulations! You Won the War!!!")
                break
            else:
                print(f"You have {ship_value} left to sink")
                board[guess_row][guess_col] = "X"
            
        else:
            if board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
            else:
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X"
    
    else:
        print("\nGame Over. You are out of turns.")
        print("The ship(s) were located at:")
        for ship in ships:
            print(f"Row: {ship[0]}, Col: {ship[1]}")

# Get user input for the number of ships
while True:
    try:
        num_ships = int(input("Enter the number of ships to find: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Play the game
battleship_game(num_ships)

