import random

# I hope it will be working.

allNumbers = list(range(1, 10))
possibleRowNumbers = []

# Setting up the board
board = [[0]*9 for i in range(9)]

# Difficulties
EASYNUMBERS = 2
MEDIUMNUMBERS = 4
HARDNUMBERS = 6

difficulty = input("[DIFFICULTY (EASY, MEDIUM, HARD)]: ").upper()

if difficulty not in ["EASY", "MEDIUM", "HARD"]:
    print("Invalid difficulty, setting difficulty to EASY mode.")
    difficulty = "EASY"

# I want to first generate the whole board and then based on the difficuly, removed X amount of numbers from each row

def getPossibleRowNumbers():
    global possibleRowNumbers
    for rows in range(9):
        numbers = list(range(1, 10))

        if difficulty == "EASY":
            removeCount = EASYNUMBERS
        
        elif difficulty == "MEDIUM":
            removeCount = MEDIUMNUMBERS

        elif difficulty == "HARD":
            removeCount = HARDNUMBERS

        else:
            removeCount = EASYNUMBERS

        removePositions = random.sample(range(9), removeCount)
        for i in removePositions:
            numbers[i] = 0

        possibleRowNumbers.append(numbers)

#def printBoard():
#    for i in range(9):
#        print(possibleRowNumbers[i])
#
#       if (i + 1) % 3 == 0:
#            print()

# Printing out the board...?
def printBoard():
    # For each row that's in the userNumbers
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
    