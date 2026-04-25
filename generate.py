# Imports
from solver import backtracking, printBoard
import random

# Main function
def generateBoard(difficulty="EASY"):
    """
    Generates a sudoku board based on the difficulty that's provided in the argument
    """

    board = [[0]*9 for _ in range(9)]

    backtracking(board) # Let's see if this will work at all LOL

    if difficulty == "EASY" or difficulty == "1":
        remove_count = random.randint(30, 45)
    elif difficulty == "MEDIUM" or difficulty == "2":
        remove_count = random.randint(45, 55)
    elif difficulty == "HARD" or difficulty == "3":
        remove_count = random.randint(55, 65)
    elif difficulty == "EXPERT" or difficulty == "4":
        remove_count = random.randint(65, 75)
    else:
        remove_count = 52

    for _ in range(remove_count):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        board[row][col] = 0

    return board

if __name__ == "__main__":
    difficulty = input("[DIFFICULTY (EASY - 1, MEDIUM - 2, HARD - 3, EXPERT - 4)]: ").upper()

    # If the user writes something else.
    if difficulty not in ["EASY", "1", "MEDIUM", "2", "HARD", "3", "EXPERT", "4"]:
        print("Invalid difficulty, setting difficulty to EASY mode.")
        difficulty = "EASY"

    print()
    printBoard(generateBoard(difficulty))
    input()
