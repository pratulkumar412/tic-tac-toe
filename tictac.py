board = [' ' for i in range(10)]
board[0]='*'
temp = board

def playerWon():
    print('YOU WON!')
    exit()

def compWon():
    print('YOU LOOSE!')
    exit()

def insertlettter(letter,pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos]==' '
    return False

def printBoard():
    for i in range(1,9,3):
        print(board[i],'|',board[i+1],'|',board[i+2])
    print('\n')

def isBoardFull():
    if board.count(' ') >=1:
        return True
    return False

def isWinner(l):
    return (
           (board[1]==l and board[2]==l and board[3]==l)
        or (board[4]==l and board[5]==l and board[6]==l)
        or (board[7]==l and board[8]==l and board[9]==l)
        or (board[1]==l and board[4]==l and board[7]==l)
        or (board[2]==l and board[5]==l and board[8]==l)
        or (board[3]==l and board[6]==l and board[9]==l)
        or (board[1]==l and board[5]==l and board[9]==l)
        or (board[3]==l and board[5]==l and board[7]==l)
        )

def isWinnerTemp(b,l):
    return (
            (b[1]==l and b[2]==l and b[3]==l)
        or (b[4]==l and b[5]==l and b[6]==l)
        or (b[7]==l and b[8]==l and b[9]==l)
        or (b[1]==l and b[4]==l and b[7]==l)
        or (b[2]==l and b[5]==l and b[8]==l)
        or (b[3]==l and b[6]==l and b[9]==l)
        or (b[1]==l and b[5]==l and b[9]==l)
        or (b[3]==l and b[5]==l and b[7]==l)
        )

def playerMove():
    run = True
    while run:
        move = input('Select a position between 1 to 9:  ')
        try:
            move = int(move)
            if(move > 0 and move<=9):
                if(spaceIsFree(move)):
                    run = False
                    insertlettter('X',move)
                else:
                    print('This position is already occupied... Select another  ')
            else:
                print('Select a valid position between 1 to 9:  ')
        except:
             print('Enter a valid positon  ')

def nextMove(tempBoard, chance) :
    if isWinnerTemp(tempBoard, 'O'):
        return tempBoard.count(' ') + 1
    if isWinnerTemp(tempBoard, 'X'):
        return - 1 - tempBoard.count(' ')

    temp = tempBoard
    uti = {}
    utility = 0

    if tempBoard.count(' ')==0:
        return 0

    for i in range(1,10):
        if tempBoard[i] == ' ' :
            if chance%2 == 0:
                temp[i] = 'O'
            else:
                temp[i] = 'X'
            utility = nextMove(temp, chance+1)
            temp[i] = ' '
            uti[i] = utility

    bestchoice = 0
    if chance%2 == 0:
        bestchoice = -5
        for i in uti :
            bestchoice = max(bestchoice, uti[i])
    else:
        bestchoice = 5
        for i in uti :
            bestchoice = min(bestchoice, uti[i])

    return bestchoice

def compMove():
    temp = board
    uti = {}
    chance = 0
    utility = 0

    for i in range(1,10):
        if board[i] == ' ' :
            temp[i] = 'O'
            utility = nextMove(temp, chance+1)
            temp[i] = ' '
            uti[i] = utility

    maxuti = 0
    for i in uti :
        maxuti = max(maxuti,uti[i])
    for i in uti :
        if uti[i] == maxuti:
            insertlettter('O',i)
            break

print('Hello!\nAre you ready to play?')

for i in range(1,5):
    playerMove()
    if isWinner('X'):
        playerWon()

    compMove()
    printBoard()
    if isWinner('O'):
        compWon()

playerMove()
printBoard()
if isWinner('X'):
    playerWon()
else :
    print('DRAW!')
