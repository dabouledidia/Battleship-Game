# DIMITROPOULOS DIMITRIOS
print('BATTLESHIP GAME')
print("The objective is to sink the opponent's ships before the opponent sinks yours.")
x = int(input("Input 1 for 1-player game or 2 for 2-player game: "))

from random import randint


def random_row(board):
    return randint(1, 6)


def random_col(board):
    return randint(1, 6)


def makeBoard(board):
    for i in range(0, 6):
        board.append([" "] * 6)
    board[0] = [" ", '1', '2', '3', '4', '5']
    board[1][0] = 'a'
    board[2][0] = 'b'
    board[3][0] = 'c'
    board[4][0] = 'd'
    board[5][0] = 'e'


def changeIntToStr(subpoInt):
    subpoStr = " "
    if subpoInt == 1:
        subpoStr = 'a'
    elif subpoInt == 2:
        subpoStr = 'b'
    elif subpoInt == 3:
        subpoStr = 'c'
    elif subpoInt == 4:
        subpoStr = 'd'
    elif subpoInt == 5:
        subpoStr = 'e'
    return subpoStr


def changeStrToInt(subpoStr):
    subpoInt = 0
    if subpoStr == 'a':
        subpoInt = 1
    elif subpoStr == 'b':
        subpoInt = 2
    elif subpoStr == 'c':
        subpoInt = 3
    elif subpoStr == 'd':
        subpoInt = 4
    elif subpoStr == 'e':
        subpoInt = 5
    return subpoInt


def print_board(board1, board2):
    print("    P1", end="            ")
    print("P2")
    for i in range(0, 6):
        print(" ".join(board1[i]), end="  ")
        print(" ".join(board2[i]))


def checkIfBoardEmpty(board):
    boardIsEmpty = "true"
    for i in range(1, 6):
        for j in range(1, 6):
            if board[i][j] == "x":
                boardIsEmpty = "false"
    return boardIsEmpty


def hitFound(board, boardhits, position1, position2):
    if board[position1][position2] == "x":
        print("Target hit!")
        board[position1][position2] = " "
        boardhits[position1][position2] = "o"
    else:
        print("Target Missed")
        boardhits[position1][position2] = "x"


def givePositions(board1, board2):
    print("\nThe board is consisted of five rows and five cols.\nEach row is represented by a letter from a to e.\n"
          "Each col is represented by a num from 1 to 5.\n"
          "For example, the position b3 equals to the third col of the second row.\n")
    for i in range(1, 6):
        position1 = str(input("Player 1 enter the position of your ship no " + str(i) + " :"))
        subpoStr1 = position1[0:1]
        subpoStr2 = position1[1:len(position1)]
        subpoInt1 = changeStrToInt(subpoStr1)
        subpoInt2 = int(subpoStr2)
        while subpoInt1 < 1 or subpoInt1 > 5 or subpoInt2 < 1 or subpoInt2 > 5 or board1[subpoInt1][subpoInt2] == "x":
            position1 = str(input("Invalid position,or position already taken.Try again:"))
            subpoStr1 = position1[0:1]
            subpoStr2 = position1[1:len(position1)]
            subpoInt1 = changeStrToInt(subpoStr1)
            subpoInt2 = int(subpoStr2)
        board1[subpoInt1][subpoInt2] = "x"
    if x == 2:
        for i in range(1, 6):
            position1 = str(input("Player 2 enter the position of your ship no " + str(i) + " :"))
            subpoStr1 = position1[0:1]
            subpoStr2 = position1[1:len(position1)]
            subpoInt1 = changeStrToInt(subpoStr1)
            subpoInt2 = int(subpoStr2)
            while subpoInt1 < 1 or subpoInt1 > 5 or subpoInt2 < 1 or subpoInt2 > 5 or board2[subpoInt1][subpoInt2] == "x":
                position1 = str(input("Invalid position,or position already taken.Try again:"))
                subpoStr1 = position1[0:1]
                subpoStr2 = position1[1:len(position1)]
                subpoInt1 = changeStrToInt(subpoStr1)
                subpoInt2 = int(subpoStr2)
            board2[subpoInt1][subpoInt2] = "x"
    if x == 1:
        for i in range(1, 6):
            subpoInt1 = int(random_row(board2))
            subpoInt2 = int(random_col(board2))
            while subpoInt1 < 1 or subpoInt1 > 5 or subpoInt2 < 1 or subpoInt2 > 5 or board2[subpoInt1][
                subpoInt2] == "x":
                subpoInt1 = int(random_row(board2))
                subpoInt2 = int(random_col(board2))
            board2[subpoInt1][subpoInt2] = "x"

def main():

    board1 = []
    board2 = []
    board1hits = []
    board2hits = []
    won1 = "false"
    won2 = "false"

    makeBoard(board1)
    makeBoard(board2)
    makeBoard(board1hits)
    makeBoard(board2hits)
    givePositions(board1, board2)
    print("Player 1 starts first")
    print_board(board1hits, board1hits)

    while True:
        position1 = str(input("Player 1 enter the position to throw your missle: "))
        subpoStr1 = position1[0:1]
        subpoStr2 = position1[1:len(position1)]
        subpoInt1 = changeStrToInt(subpoStr1)
        subpoInt2 = int(subpoStr2)
        while subpoInt1 < 1 or subpoInt1 > 5 or subpoInt2 < 1 or subpoInt2 > 5 or board2hits[subpoInt1][
            subpoInt2] == "o" or board2hits[subpoInt1][subpoInt2] == "x":
            position1 = str(input("Invalid position,or missle already thrown there.Try again: "))
            subpoStr1 = position1[0:1]
            subpoStr2 = position1[1:len(position1)]
            subpoInt1 = changeStrToInt(subpoStr1)
            subpoInt2 = int(subpoStr2)
        print("Missile thrown at " + position1)
        hitFound(board2, board2hits, subpoInt1, subpoInt2)
        print_board(board1hits, board2hits)
        won1 = checkIfBoardEmpty(board2)
        print(" ")
        if won1 == "true":
            print("\nGame Over.\nPlayer 1 wins!")
            break
        if x == 2:
            position1 = str(input("Player 2 enter the position to throw your missle: "))
            subpoStr1 = position1[0:1]
            subpoStr2 = position1[1:len(position1)]
            subpoInt1 = changeStrToInt(subpoStr1)
            subpoInt2 = int(subpoStr2)
            while subpoInt1 < 1 or subpoInt1 > 5 or subpoInt2 < 1 or subpoInt2 > 5 or board1hits[subpoInt1][
                subpoInt2] == "o" or board1hits[subpoInt1][subpoInt2] == "x":
                position1 = str(input("Invalid position,or missle already thrown there.Try again: "))
                subpoStr1 = position1[0:1]
                subpoStr2 = position1[1:len(position1)]
                subpoInt1 = changeStrToInt(subpoStr1)
                subpoInt2 = int(subpoStr2)
            print("Missile thrown at " + position1)
        if x == 1:
            subpoInt1 = int(random_row(board2))
            subpoInt2 = int(random_col(board2))
            while subpoInt1 < 1 or subpoInt1 > 5 or subpoInt2 < 1 or subpoInt2 > 5 or board1hits[subpoInt1][
                subpoInt2] == "o" or board1hits[subpoInt1][subpoInt2] == "x":
                subpoInt1 = int(random_row(board2))
                subpoInt2 = int(random_col(board2))
            print("Missile thrown at " + changeIntToStr(subpoInt1) + str(subpoInt2))
        hitFound(board1, board1hits, subpoInt1, subpoInt2)
        print_board(board1hits, board2hits)
        won2 = checkIfBoardEmpty(board1)
        if won2 == "true":
            print("\nGame Over.\nPlayer 2 wins!")
            break

main()