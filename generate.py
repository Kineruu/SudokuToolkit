import random

# I hope it will be working.

allNumbers = list(range(1, 10))
possibleRowNumbers = []

# Setting up the board
board = [[0]*9 for i in range(9)]

# Difficulties
# I think that's better
EASYNUMBERS = random.randint(2, 3)
MEDIUMNUMBERS = random.randint(4, 5)
HARDNUMBERS = random.randint(6, 8)

difficulty = input("[DIFFICULTY (EASY, MEDIUM, HARD)]: ").upper()


# If the user writes something else.
if difficulty not in ["EASY", "MEDIUM", "HARD"]:
    print("Invalid difficulty, setting difficulty to EASY mode.")
    difficulty = "EASY"

# I want to first generate the whole board and then based on the difficuly, removed X amount of numbers from each row

def getPossibleRowNumbers():
    global possibleRowNumbers
    for rows in range(9):
        numbers = list(range(1, 10))

        # If difficulty is equal to EASY
        if difficulty == "EASY":
            # Set "removeCount" to a variable EASYNUMBERS
            removeCount = EASYNUMBERS
        
        elif difficulty == "MEDIUM":
            removeCount = MEDIUMNUMBERS

        elif difficulty == "HARD":
            removeCount = HARDNUMBERS

        else:
            # In case something goes wrong
            removeCount = EASYNUMBERS

        # Learnt that today, this is fun
        removePositions = random.sample(range(9), removeCount)
        for i in removePositions:
            numbers[i] = 0

        possibleRowNumbers.append(numbers)


# Yes that's the same code that I used in the solver.py file
# Printing out the board...?
def printBoard():
    # For each row 
    for i in range(9):
        # Every 3 rows and if i is not equal to 0 so it doesn't write it at the beginning
        if i % 3 == 0 and i != 0:
            # Prints it "*" 21 times
            print("-" * 21)
    
        for j in range(9):
            # Every 3 numbers
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            number = possibleRowNumbers[i][j]
            value = number if number != 0 else "_"
            print(value, end=" ")
    
        print()

if __name__ == "__main__":
    getPossibleRowNumbers()
    printBoard()
    