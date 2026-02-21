import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_menu():
    print("""
██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
""")
    print("""
------------------------------------------------------------------------------
          """)
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")
    print("""
------------------------------------------------------------------------------
          """)

def show_instructions():
    print("""
██╗███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║██╔██╗ ██║███████╗   ██║   ██████╔╝██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║██║╚██╗██║╚════██║   ██║   ██╔══██╗██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
""")
    print("""
----------------------------------------------------------------------------------------------
          """)
    print("Guess the Cordinates of the Enemy's Battleship!")
    print("Enter the coordinates to hit the hidden ship.")
    print("Enter the row and column numbers when asked.")
    print("Sink all the ships of your enemy to win the game!")

def create_board(size):
    board = []
    for _ in range(size):
        row = ["~"] * size
        board.append(row)
    return board

def print_board(board):
    size = len(board)

    print(" "+ " ".join(str(i) for i in range(size)))

    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def place_ship(size, length=3):
    orientation = random.choice(["H", "V"])

    if orientation == "H":
        row = random.randint(0, size - 1)
        col = random.randint(0, size - length)
        return [(row, col + i) for i in range(length)]
    
    else:
        row = random.randint(0, size - length)
        col = random.randint(0, size - 1)
        return [(row + i, col) for i in range(length)]
    
    ship = [(row + i, col) for i in range(length)]
    return ship

def get_guess(size):
    try:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        if 0 <= row < size and 0 <= col <size:
            return (row, col)
        else:
            print("Coordinates out of bounds. Please enter values between 0 and {}.".format(size - 1))
            return None
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

def start_game():
    while True:
        clear_screen()

        print("""
------------------------------------------------------------------------------------------------------------          
██████╗  █████╗ ████████╗████████╗██╗     ███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗███████╗██╗
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██████╔╝███████║   ██║      ██║   ██║     █████╗      ███████╗   ██║   ███████║██████╔╝   ██║   ███████╗██║
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   ╚════██║╚═╝
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   ███████║██╗
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
------------------------------------------------------------------------------------------------------------
""")
        size = 5
        board = create_board(size)
        ship = place_ship(size, 3)
        hits = set()
        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:

            clear_screen()

            print("Enemy Waters:\n")
            print_board(board)
            print("\nAttempts left: {}".format(max_attempts - attempts))
            guess = get_guess(size)

            if guess is None:
                continue

            row,col = guess

            if board[row][col] in ["X", "O"]:
                print("You already guessed that location. Try again.")
                continue

            attempts += 1

            if (row,col) in ship:
                print("Hit! You hit the enemy's battleship!")
                board[row][col] = "X"
                hits.add((row,col))
            else:
                print("Miss! You missed the enemy's battleship.")
                board[row][col] = "O"
            
            time.sleep(2)
            
            if all(pos in hits for pos in ship):
                break
        clear_screen()
        if all(pos in hits for pos in ship):
            print("""\n
██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║██║
 ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║██║
  ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║██╗
   ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝

 █████╗ ██╗     ██╗          ███████╗██╗  ██╗██╗██████╗ ███████╗    ███████╗██╗   ██╗███╗   ██╗██╗  ██╗
██╔══██╗██║     ██║          ██╔════╝██║  ██║██║██╔══██╗██╔════╝    ██╔════╝██║   ██║████╗  ██║██║ ██╔╝
███████║██║     ██║          ███████╗███████║██║██████╔╝███████╗    ███████╗██║   ██║██╔██╗ ██║█████╔╝ 
██╔══██║██║     ██║          ╚════██║██╔══██║██║██╔═══╝ ╚════██║    ╚════██║██║   ██║██║╚██╗██║██╔═██╗ 
██║  ██║███████╗███████╗     ███████║██║  ██║██║██║     ███████║    ███████║╚██████╔╝██║ ╚████║██║  ██╗
╚═╝  ╚═╝╚══════╝╚══════╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝    ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝
""")
        else:
            print("""\n
███████╗ █████╗ ██╗██╗     ███████╗██████╗     ████████╗ ██████╗ 
██╔════╝██╔══██╗██║██║     ██╔════╝██╔══██╗    ╚══██╔══╝██╔═══██╗
█████╗  ███████║██║██║     █████╗  ██║  ██║       ██║   ██║   ██║
██╔══╝  ██╔══██║██║██║     ██╔══╝  ██║  ██║       ██║   ██║   ██║
██║     ██║  ██║██║███████╗███████╗██████╔╝       ██║   ╚██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝        ╚═╝    ╚═════╝ 

███████╗██╗███╗   ██╗██╗  ██╗    ████████╗██╗  ██╗███████╗    ███████╗██╗  ██╗██╗██████╗ ███████╗██╗
██╔════╝██║████╗  ██║██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔════╝██║  ██║██║██╔══██╗██╔════╝██║
███████╗██║██╔██╗ ██║█████╔╝        ██║   ███████║█████╗      ███████╗███████║██║██████╔╝███████╗██║
╚════██║██║██║╚██╗██║██╔═██╗        ██║   ██╔══██║██╔══╝      ╚════██║██╔══██║██║██╔═══╝ ╚════██║╚═╝
███████║██║██║ ╚████║██║  ██╗       ██║   ██║  ██║███████╗    ███████║██║  ██║██║██║     ███████║██╗
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚═╝╚═╝     ╚══════╝╚═╝
""")
            print_board(board)
            print(f"The ship was located at: {ship}")
            print(f"You hit {len(hits)} out of 3 parts of the ship.")
        print("\n1. Restart game")
        print("2. Return to main menu")

        choice = input("Enter your choice 1 or 2: ")

        if choice == '1':
            continue
        elif choice == '2':
            return
        else:
            print("Invalid choice.")
            input("Press Enter to try again...")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            clear_screen()
            start_game()
            input("Press Enter to return to the main menu...")
            clear_screen()
        
        elif choice == '2':
            clear_screen()
            show_instructions()
            input("Press Enter to return to the main menu...")
            clear_screen()

        elif choice == '3':
            clear_screen()
            print("""
 ██████╗  ██████╗  ██████╗ ██████╗ ██╗  ██╗███████╗██╗
██╔════╝ ██╔═══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝██║
██║  ███╗██║   ██║██║  ██║██████╔╝ ╚████╔╝ █████╗  ██║
██║   ██║██║   ██║██║  ██║██╔══██╗  ╚██╔╝  ██╔══╝  ╚═╝
╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ███████╗██╗
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝
""")
            for i in range(6, 0, -1):
                print("Exiting the game in {} seconds...".format(i))
                time.sleep(1)
            clear_screen()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

main()