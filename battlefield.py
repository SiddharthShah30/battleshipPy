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
    print("3. Scoreboard")
    print("4. Exit")
    print("""
------------------------------------------------------------------------------
          """)

def show_instructions():
    clear_screen()
    print("""
██╗███╗   ██╗███████╗████████╗██████╗ ██╗   ██╗ ██████╗████████╗██╗ ██████╗ ███╗   ██╗███████╗
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║   ██║██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝
██║██╔██╗ ██║███████╗   ██║   ██████╔╝██║   ██║██║        ██║   ██║██║   ██║██╔██╗ ██║███████╗
██║██║╚██╗██║╚════██║   ██║   ██╔══██╗██║   ██║██║        ██║   ██║██║   ██║██║╚██╗██║╚════██║
██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║███████║
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
""")
    print("""
🎯 OBJECTIVE
Destroy all enemy ships hidden on the board
before you run out of attempts.

----------------------------------------
🧑 PLAYER SETUP
• Enter your name
• Choose number of ships to hunt (1–3)

----------------------------------------
📏 BOARD & ATTEMPTS

Ships     Board Size     Starting Attempts
------------------------------------------
1 ship    5 x 5          3 attempts
2 ships   7 x 7          6 attempts
3 ships   9 x 9          9 attempts

----------------------------------------
🎮 HOW TO PLAY

1. The board shows rows and columns numbered
2. Enter ROW first, then COLUMN
3. Example:
      Row: 2
      Column: 4
   → targets position (2,4)

----------------------------------------
💥 HIT / MISS SYSTEM

X  = Hit (part of ship destroyed)
O  = Miss (empty water)
~  = Unknown water

✔ Each guess uses 1 attempt
✔ Every HIT gives you +1 BONUS attempt
✔ Sink ALL ships to win

----------------------------------------
🏆 SCORING

You earn points based on:
• Number of ships destroyed
• Attempts saved
• Board difficulty

Higher difficulty = higher score

----------------------------------------
📜 SCOREBOARD

Your best scores are saved locally.
View them from the main menu.

----------------------------------------
""")
    input()

def setup_player():
    clear_screen()
    print("""
------------------------------------------------------------------------------------
 ██████╗  █████╗ ███╗   ███╗███████╗     ███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝ ██╔══██╗████╗ ████║██╔════╝     ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
██║  ███╗███████║██╔████╔██║█████╗       ███████╗█████╗     ██║   ██║   ██║██████╔╝
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝       ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗     ███████║███████╗   ██║   ╚██████╔╝██║     
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     
------------------------------------------------------------------------------------
          """)

    name = input("Enter your name: ").strip()

    while True:
        ships = input("Enter the number of ships you want to play with (1-3): ").strip()
        if ships in ['1', '2', '3']:
            ships = int(ships)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")

    board_sizes = {1:5, 2:7, 3:9}
    board_size = board_sizes[ships]

    attempts = ships * 3

    return name, ships, board_size, attempts

def place_multiple_ships(size, num_ships, length=3):
    ships = []

    while len(ships) < num_ships:
        new_ship = place_ship(size, length)

        if not any(cell in ship for ship in ships for cell in new_ship):
            ships.append(new_ship)
    return ships

def create_board(size):
    board = []
    for _ in range(size):
        row = ["~"] * size
        board.append(row)
    return board

def print_board(board):
    size = len(board)

    print(" "+" ".join(f"{i:2}" for i in range(size)))

    print(" " + "---"*size)

    for i, row in enumerate(board):
        print(f"{i:2} | " + " ".join(f"{cell:2}" for cell in row))


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

def calculate_score(num_ships, attempts_used, attempts_available, board_size, hits):
    
    total_cells = num_ships * 3
    hit_ratio = hits / total_cells
    ship_points = hits * 15
    efficiency_bonus = max(0, (attempts_available - attempts_used) * 5)
    difficulty_multiplier = board_size * 2

    if hits == 0:
        return 0
    
    return ship_points + efficiency_bonus + difficulty_multiplier


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
        name, num_ships, size, max_attempts = setup_player()
        board = create_board(size)
        ships = place_multiple_ships(size, num_ships)
        hits = set()
        attempts_used = 0
        attempts_available = max_attempts

        while attempts_used < attempts_available:

            clear_screen()

            print("Enemy Waters:\n")
            print_board(board)
            print("\nAttempts left: {}".format(attempts_available - attempts_used))
            guess = get_guess(size)

            if guess is None:
                continue

            row,col = guess

            if board[row][col] in ["X", "O"]:
                print("You already guessed that location. Try again.")
                continue

            attempts_used += 1

            hit = False
            for ship in ships:
                if (row,col) in ship:
                    hit = True
                    break

            if hit:
                print("Hit! You hit the enemy's battleship!")
                board[row][col] = "X"
                hits.add((row,col))
                attempts_available += 1
            else:
                print("Miss! You missed the enemy's battleship.")
                board[row][col] = "O"
            
            time.sleep(2)
            
            all_cells = [cell for ship in ships for cell in ship]
            if all(cell in hits for cell in all_cells):
                break
        clear_screen()
        if all(cell in hits for cell in all_cells):
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
            score = calculate_score(num_ships, attempts_used, max_attempts, size, len(hits))
            print(f"\nYour score: {score}")
            save_score(name, score)
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
            score = calculate_score(num_ships, attempts_used, attempts_available, size, len(hits))
            print(f"\nYour score: {score}")
            save_score(name, score)
            print(f"The ship was located at: {ships}")
            total_cells = num_ships * 3
            print(f"You hit {len(hits)} out of {total_cells} parts of the ship.")
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


def show_scoreboard():
    clear_screen()
    print("""
 ██████╗  ██████╗  ██████╗ ██████╗ ███████╗██████╗  ██████╗  █████╗ ██████╗ ██████╗ 
██╔════╝ ██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗  ██║      ██║   ██║██████╔╝█████╗  ██████╔╝██║   ██║███████║██████╔╝██║  ██║
 ╚═══██╗ ██║      ██║   ██║██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║
██████╔╝ ╚██████╗ ╚██████╔╝██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
╚═════╝   ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
""")

    try:
        with open("score.txt", "r") as f:
            scores = [line.strip().split(":") for line in f if ":" in line]
            scores = [(name.strip(), score.strip()) for name, score in scores]
        
        scores.sort(key=lambda x: int(x[1]), reverse=True)
        for score in scores[:10]:  # Show top 10 scores
            print(f"{score[0]}: {score[1]}")

    except FileNotFoundError:
        print("No scores available yet.")
    
    input("\nPress Enter to return to the main menu...")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

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
            show_scoreboard()
            clear_screen()

        elif choice == '4':
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
            print("Invalid choice. Please enter a number between 1 and 4.")

def save_score(name, score):
    with open("score.txt", "a") as file:
        file.write(f"{name}: {score}\n")

main()