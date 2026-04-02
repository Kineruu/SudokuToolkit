
# Important stuff
userNumbers = []

# Range of numbers from 1 to 10
allNumbers = set(range(1, 10))

# For single candidate... That's not used anways
checking = True

# Says for itself
debugging = False

# Prints out the board.
def printBoard(board=None):
    if board == None:
        board = userNumbers
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

            number = board[i][j] if board[i][j] != 0 else "_"
            print(number, end=" ")
        print()

# A function that gets user's numbers...
def getUserNumbers():    
    """
    How this works:
    Asking the user to enter line by line the numbers
    0 or # represents empty space
    """
    # Making it global because "userNumbers" will be user later.
    global userNumbers

    # Explaining the basic common stuff.
    print("You must enter 9 numbers. \nIf you got a situation where there is no number between two numbers \njust add an empty space by putting 0 there... An example: 1 - 2 -> 1 0 2")
    # Do this 9 times
    for i in range(9):
        # Basically checking whether the user understands basic sudoku rules and what is said in the print statement
        while True:
            row = []
            try:
                # Gets basic user input, replacing # with 0's...
                userInput = input(f"Row {i+1}: ").replace("#", "0").strip()
                # Checking each number in the string
                for case in userInput:
                    # If it's a number
                    if case.isdigit():
                        # Add to the "row" list
                        row.append(int(case))
                    # Otherwise, skip it
                    else:
                        pass
                # If there are 9 elements in the "row" list
                if len(row) == 9:
                    userNumbers.append(row)
                    # Breaks the loop, allowing the for function continuing doing what it started
                    break
                else:
                    # Otherwise the user probably put something wrong and it's not a number... Or it's too long or too short
                    print("You must enter 9 numbers!")
            except ValueError:
                print("You must only enter numbers!")
                print("Restart the program to insert the numbers again.")
                break

# Getting empty spaces
def findEmptySpace():
    global checking

    while checking:
        checking = False
        # for each row
        for row in range(9):
            # for each column
            for col in range(9):
                # if the number in row and col is equal to 0
                # Detects 0s.
                if userNumbers[row][col] == 0:
                    # Get all values from the userNumers/current column but I'm using differnet variable
                    # So "row" and "r" don't override each other.

                    # I think this is called a "list comprehension" or something along these lines
                    # In "[ ]" because I want it to be in a list that will be used in a set later
                    # For r in range(9) -> r = 0, 1, 2, ..., 8, 9

                    # colValues = []
                    # for r in range(9):
                        #columnValues.append(userNumbers[r][col])

                    # This is the same thing but shorter.
                    colValues = [userNumbers[r][col] for r in range(9)]
                    if debugging:
                        print(f"Zero at: {row}, {col} | row: {userNumbers[row]}")

                    # Removes zeros
                    rowSet = set(userNumbers[row])
                    rowSet.discard(0)
                    colSet = set(colValues)
                    colSet.discard(0)

                    # Time to code the 3x3 box checker... 27/03/2026 - 19:24 / 07:24 PM CEST

                    # This is used to find the top left corner of the 3x3 box
                    boxRow = (row // 3) * 3
                    boxCol = (col // 3) * 3

                    boxSet = set()
                    for r in range(boxRow, boxRow + 3):
                        for c in range(boxCol, boxCol + 3):
                            boxSet.add(userNumbers[r][c])
                    boxSet.discard(0)

                    # All possible numbers that can be used = allNumbers (1 - 9) - all numbers that are in the row and column
                    possibleNumbers = allNumbers - rowSet - colSet - boxSet

                    # This is called "single candidate" in sudoku terms
                    if len(possibleNumbers) == 1:
                        number = possibleNumbers.pop()
                        userNumbers[row][col] = number
                        checking = True
                    
                    # Prints it out...
                    if debugging:
                        print(f"({row}, {col}) -> {possibleNumbers}")

def findRemaining(board=None): 
    """
    Checking what numbers are missing in the rows.
    """

    if board == None:
        board = userNumbers

    # Printing the numbers that user entered into a set
    for row in userNumbers:
        setRow = set(row)
        print(setRow)

    # A small border
    print("================================")

    # Just realised that this already removes the duplicate numbers for me as well LOL

    # Printing that numbers are missing in rows
    for row in userNumbers:
        setRow = set(row)
        setRow.discard(0) # Zero do not exist in sudoku.
        missingNumbers = allNumbers - setRow
    
    print(missingNumbers)

def isNumberSafe(row, col, number, board):
    """
    Checks whether the number that wants to be put into the cell is safe.
    """

    if board == None:
        board = userNumbers

    # If a number is already in the row, it cannot be put into the cell.
    if number in board[row]:
        return False

    # If a number is in the column, it cannot be put into the cell   
    for r in range(9):
        if board[r][col] == number:
            return False
        
    boxRow = (row // 3) * 3
    boxCol = (col // 3) * 3

    # Checks whether the number is already in the box
    for r in range(boxRow, boxRow + 3):
        for c in range(boxCol, boxCol + 3):
            if board[r][c] == number:
                return False

    return True

def backtracking(board):

    if board == None:
        board = userNumbers

    # For each row
    for row in range(9):
        # For each column
        for col in range(9):
            # If the number is equal to zero
            if board[row][col] == 0:
                # For numbers in the range 1 to 9
                for numbers in range(1, 10):
                    # if... calls the function
                    if isNumberSafe(row, col, numbers, board):
                        # Sets the board[row][col] to the numbers
                        board[row][col] = numbers
                        # Calls itself in the function. That's named recursion.
                        if backtracking(board):
                            return True
                        # Sets the number to zero if it fails to go further
                        board[row][col] = 0
                return False
    return True

# Running the program
if __name__ == "__main__":
    # It's not fancy but it's easy to read.
    print("")
    getUserNumbers()

    print()
    printBoard()

    if debugging:
        findRemaining()

    findEmptySpace()

    if backtracking(userNumbers):
        print()
        printBoard()
        input()
    else:
        print("The board cannot be solved!")
        input()
