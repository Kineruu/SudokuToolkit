# Imports
from solver import backtracking, printBoard
import random

raw_output = True

def generateBoard(difficulty="EASY"):
    """
    Generates a sudoku board based on the difficulty that's provided in the argument
    """

    board = [[0]*9 for _ in range(9)]

    backtracking(board) # Let's see if this will work at all LOL

    if difficulty == "EASY":
        remove_count = random.randint(1, 2)
    elif difficulty == "MEDIUM":
        remove_count = random.randint(3, 4)
    elif difficulty == "HARD":
        remove_count = random.randint(5, 6)
    elif difficulty == "EXPERT":
        remove_count = random.randint(7, 8)
    else:
        remove_count = 3

    for _ in range(9):
        positions = random.sample(range(9), remove_count)
        for position in positions:
            board[_][position] = 0

    return board

if __name__ == "__main__":
    difficulty = input("[DIFFICULTY (EASY, MEDIUM, HARD, EXPERT)]: ").upper()

    # If the user writes something else.
    if difficulty not in ["EASY", "MEDIUM", "HARD", "EXPERT"]:
        print("Invalid difficulty, setting difficulty to EASY mode.")
        difficulty = "EASY"

    print()
    #generateBoard(difficulty)
    printBoard(generateBoard(difficulty))
    print()
    input()
