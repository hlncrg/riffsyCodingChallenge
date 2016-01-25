def printBoard(board):
    for i in board[::-1]:#reverse the order of the rows
        print i#since the zero row is the bottom row in the game
    return

def checkSquare(tot,square):
    if square=='o' and tot>=0:#if the current square has a o and the previous square was an o
        return tot+1#add from tot
    elif square=='x' and tot<=0:#if the current square has a x and the previous square was an x
        return tot-1#subtract from tot 
    elif square=='o' and tot<=0:#if the current square has a o and the previous square was an x
        return 1#restart the counter
    elif square=='x' and tot>=0:#if the current square has a x and the previous square was an o
        return -1#restart the counter
    elif square=='*':#if the square it empty
        return 0#return zero

def checkWin(board,numRow=6,numCol=7):
    #check for four in Columns
    for i in range(numRow):
        tot=0
        for j in range(numCol):
            tot=checkSquare(tot,board[i][j])
            if tot==4 or tot==-4:
                return 'win'
    #check for four in rows
    for j in range(numCol):
        tot=0
        for i in range(numRow):
            tot=checkSquare(tot,board[i][j])
            if tot==4 or tot==-4:
                return 'win'
    #check for four in diag            
    for j in range(numCol):
        for i in range(numRow):
            #one way diag
            tot=0
            for m in range(4):
                if j+m<=numCol-1 and i+m<=numRow-1:
                    tot=checkSquare(tot,board[i+m][j+m])
                    if tot==4 or tot==-4:
                        return 'win'
            #other way diag
            tot=0
            for m in range(4):
                if j-m>0 and i+m<=numRow-1:
                    tot=checkSquare(tot,board[i+m][j-m])
                    if tot==4 or tot==-4:
                        return 'win'
    #if none of the spaces are empty and no one has won
    #stop the game
    if sum([sum([1 if j=='*' else 0 for j in i]) for i in board])==0:
        print 'no one wins'

def placePiece(typePiece,col,board,numRow=6):
    print typePiece,'place at: ', col
    for i in range(numRow):
        #find the row with the empty space
        #for the column given
        if board[i][col]=='*':
            board[i][col]=typePiece
            return 0
    #if the colum is full, say so
    print 'can not place'
    return -1

import random
random.seed(7)#set to different values for different games
numRow=6#number of rows of the board
numCol=7#number of columns of the board
board=[['*' for j in range(numCol)] for i in range(numRow)]
#fill the board with empties
while sum([sum([1 if j=='*' else 0 for j in i]) for i in board])!=0:
#while there are empty spaces in the board continue the game
    while placePiece('x',random.randrange(0,numCol),board)==-1:
    #continue to place pieces on the board if you try to place in a 
    #column is full
        if sum([sum([1 if j=='*' else 0 for j in i]) for i in board])==0:
        #if the board is full, stop
            break
    printBoard(board)#board at the current step
    print
    if checkWin(board)=='win':
        print 'end of game'
        break
    while placePiece('o',random.randrange(0,numCol),board)==-1:#ditto for the other player
        if sum([sum([1 if j=='*' else 0 for j in i]) for i in board])==0:
            break
    printBoard(board)
    print 
    if checkWin(board)=='win':
        print 'end of game'
        break

