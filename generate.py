import random

# I hope it will be working.

allNumbers = set(range(1, 10))

# Setting up the board
board = [[0]*9 for i in range(9)]

# Difficulties
EASY = random.randint(2, 3)
MEDIUM = random.randint(4, 6)
HARD = random.randint(7, 8)

# I want to first generate the whole board and then based on the difficuly, removed X amount of numbers from each row

# WORKING ON IT

if __name__ == "__main__":
    ...