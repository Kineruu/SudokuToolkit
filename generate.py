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

        for amount in range(removeCount):
            number = random.choice(numbers)
            numbers.remove(number)
    
        possibleRowNumbers.append(numbers)

if __name__ == "__main__":
    getPossibleRowNumbers()
    print(possibleRowNumbers)