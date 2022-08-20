# 1. Magic 8-ball

from gettext import find
from random import randint
from unittest import result


answers = [ "It is certain", "It is decidedly so", "Without a \
doubt", "Yes, definitely", "You may rely on it", "As I see it, \
yes", "Most likely", "Outlook good", "Yes", "Signs point to yes",
"Reply hazy try again", "Ask again later", "Better not tell you \
now", "Cannot predict now", "Concentrate and ask again", "Don ' t \
count on it", "My reply is no", "My sources say no", "Outlook \
not so good", "Very doubtful" ]

def magic8Ball():
    question = input('Ask a question:')
    randomIdx = randint(0,len(answers)-1)
    print ('Answer to your question("{}") is: {}'.format(question, answers[randomIdx]))

# magic8Ball()

# 2. FIFO

def fifo():
    queue =[]

    while True:
        i = input('Please input something: ')
        if i=='':
            break
        if i=='?':
            print('The first element from the queue: {}'.format(queue.pop(0)))
        else:
            queue.extend(i)

# fifo()

# 3. Fibonacci
def fibo(num):
    if num <= 1:
        return 0
    fb1 = 0
    fb2 = 1
    i=2
    result = [0]
    while i <= num:
        result.append(fb1+fb2)
        fb1=result[len(result)-2]
        fb2=result[len(result)-1]
        i+=1

    return result

# print(fibo(7))

# 4. Counting Letters
def countLettersInStr(subStr, str):
    result=[]
    count=0
    mainStr = str
    idx= mainStr.find(subStr)
    while  idx> -1:
        result.extend(mainStr[0:idx])
        if count==0:
            result.extend([subStr])
        count +=1
        mainStr=mainStr.replace(mainStr[0:len(subStr)+idx],'',1) #fix: only remove once
        idx=mainStr.find(subStr)

    result.extend(mainStr)
    replaceStr= ''.join(result)

    return replaceStr, count


print(countLettersInStr('an', 'bananaanan an ccc'))

# 5. Palindrome
def palindrome(str):
    charList=[]
    reverseList=[]
    charList +=str
    reverseList +=str
    charList.reverse()
    
    if charList==reverseList:
        return True
    else:
        return False

# print(palindrome("malayalam"))

# 6. Largest number 

def maxNum(numList):
    print (numList)
    print(max(numList))

# list1 = [10, 20, 4]
# list2 = [20, 10, 20, 4, 100]
# maxNum(list1)
# maxNum(list2)


# 7. TIC-TAC-TOE
board =[[' ',' ',' ', ' '], [' ',' ',' ', ' '], [' ',' ',' ', ' '], [' ',' ',' ', ' ']]

players = ['x', 'o']
currentPos = [0,0]

def displayBoard(aBoard):
    for row in aBoard:
        print('-----------------')
        currentRow = ''
        for col in row:
            currentRow += '| '
            currentRow += col
            currentRow += ' '
        currentRow += '|'
        print(currentRow)
    print('-----------------')

# get rol/col position for inputing
def getRolCol(axis):
    x = int(input('Please input {} number in range 1-4: '.format(axis)))
    while x <1 or x > 4:
        x = int(input('Input is not valid! Please enter {} number in range 1-4: '.format(axis)))
    if axis=='row':
        currentPos[0]=x-1
    else:
        currentPos[1]=x-1

# check if the cell is occupied?
def checkCellEmpty(cell):
    if cell==' ':
        return True
    else:
        return False

# update the board for current player
def updateBoard(aBoard, player):
    aBoard[currentPos[0]][currentPos[1]]=player

# check if there is any player won?
def winner(aBoard,player):

    theWinner = player*4

    # check row - based on current position
    rowVal = ''.join(aBoard[currentPos[0]])  
    if rowVal == theWinner:
        return True

    # for row in aBoard:
    #     rowVal = ''.join(row)
    #     if rowVal == theWinner:
    #         return True

    # check column - based on the current position
    colVal =''
    for row in range(0,4):
        colVal +=aBoard[row][currentPos[1]]
    if colVal == theWinner:
        return True
        
    # check diagonal lines
    diaVal1 = ''
    diaVal2 = ''
    
    for p in range(0,4):
        diaVal1 += aBoard[p][p]
        diaVal2 += aBoard[p][4-p-1]

    if diaVal1 == theWinner or diaVal2 == theWinner:
        return True
        
    return False

# check if the board is full?
def checkBoardFull(aBoard):
    boardVal=''
    for x in range(0,4):
        for y in range(0,4):
            boardVal +=aBoard[x][y]

    if boardVal.find(' ') < 0:
        return True
    else:
        return False

# reset the board for another round
def resetBoard(aBoard):
    for x in range(0,4):
        for y in range(0,4):
            aBoard[x][y] =' '


# main program
def ticTacToe():    

    while True: #one round playing:
        print('Tic tac toe game starts!')
        displayBoard(board)

        isWon = False
        isBoardFull= False
        
        while not isWon and not isBoardFull:
            for player in players:
                print ('Player {} selects (x,y) positions in range(1-4)'.format(player.upper()))
                getRolCol('row')
                getRolCol('col')
                while checkCellEmpty(board[currentPos[0]][currentPos[1]]) == False:
                    print('ERROR! This cell is occupied! Player {} selects another (x,y) positions in range(1-4)'.format(player.upper())) 
                    getRolCol('row')
                    getRolCol('col')

                updateBoard(board,player)
                displayBoard(board)

                isWon = winner(board,player)
                if isWon:
                    print('SUPER! Player {} won! The game is over!'.format(player.upper()))
                    break

                isBoardFull=checkBoardFull(board)
                if isBoardFull:
                    print('The game is over! No player is won!')
                    break
            
        
        isContinued = input('Do you want to play another round? (y/n) ')
        if isContinued!= 'y':
            break
        resetBoard(board)

    print('The game is finished! Thank you for playing!')

ticTacToe()