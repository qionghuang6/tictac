#! /usr/bin/python3

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

# Transformations (rotations are counter-clockwise)
Rot90 = [6,3,0,7,4,1,8,5,2]
Rot180 = [8,7,6,5,4,3,2,1,0]
Rot270 = [2,5,8,1,4,7,0,3,6]
VertFlip= [2,1,0,5,4,3,8,7,6]
Transformations = [[Rot90],[Rot180],[Rot270],[VertFlip],[Rot90,VertFlip],[Rot180,VertFlip],[Rot270,VertFlip]]

def isVictory(boardStr):
    for combo in Wins:
        if(boardStr[combo[0]] == boardStr[combo[1]] and boardStr[combo[1]] == boardStr[combo[2]] and boardStr[combo[0]] != '_'):
            return True, boardStr[combo[0]] 
    if("_" not in boardStr):
        return False, 'A'
    return False, '_'

def advance(board):
    newBoards = list()
    xCount = board.count('x')
    oCount = board.count('o')
    for i in range(0,9):
        if(board[i] == '_'):
            tstr = list(board)
            if(xCount > oCount):
                tstr[i] = 'o'
            else:
                tstr[i] = 'x'
            newBoards.append("".join(tstr))
    return newBoards

def makeVariant(current, instructions):
    newList = list()
    for i in range(0,9):
        newList.append(current[instructions[i]])
    return newList

def main():
    gameCount = 0
    boardCount = 0
    oWin = 0
    xWin = 0
    currentboards = list()
    nextboards = list()
    for i in range(0,9):
        newboard = list()
        for j in range(0,9):
            if(i == j):
                newboard.append('x')
            else:
                newboard.append('_')
        currentboards.append(''.join(newboard))
    allboards = currentboards[:]
    while(len(currentboards) > 0):
        print("Current boards: ", len(currentboards))
        for board in currentboards:
            boardCount += 1
            isWin, side = isVictory(board)
            if(isWin and side == 'x'):
                xWin += 1
            if(isWin and side == 'o'):
                oWin += 1
            if(side == 'o' or side == 'x' or side == 'A'):
                # finalboards.append(board)
                gameCount += 1
            else:
                nextboards.extend(advance(board))
        currentboards = nextboards
        allboards.extend(nextboards)
        nextboards = list()

    print(gameCount, "games", boardCount, "boards", xWin , "xWins", oWin, "oWins")
    
    uniqueboards = set(allboards)
    for board in allboards:
        if(board in uniqueboards):
            thisboard = list(board)
            for transet in Transformations:
                variant = thisboard[:]
                for change in transet:
                    variant = makeVariant(variant, change)
                uniqueboards.discard("".join(variant))
    print(len(uniqueboards), "uniqueboards")

main()