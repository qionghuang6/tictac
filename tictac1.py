#! /usr/bin/python3

''' Layout positions:
0 1 2
3 4 5
6 7 8
'''
# layouts look like "_x_ox__o_"

Wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def isVictory(boardStr):
    for combo in Wins:
        if(boardStr[combo[0]] == boardStr[combo[1]] and boardStr[combo[1]] == boardStr[combo[2]] and boardStr[combo[0]] != '_'):
            return True, boardStr[combo[0]] 
    if("_" not in boardStr):
        return True, 'A'
    return False, '_'

AllBoards = {} # this is a dictionary with key = a layout, and value = its corresponding BoardNode

class BoardNode:
    def __init__(self,layout):
        self.layout = layout
        self.endState = None # if this is a terminal board, endState == 'x' or 'o' for wins, of 'd' for draw, else None
        self.children = [] # all layouts that can be reached with a single move

    def print_me(self):
        print ('layout:',self.layout, 'endState:',self.endState)
        print ('children:',self.children)

def CreateAllBoards(layout,parent):
    thisNode = BoardNode(layout)
    AllBoards[layout] = thisNode
    isWin, side = isVictory(layout)
    if(isWin):
        if(side == 'x'):
            thisNode.endState = 'x'
        if(side == 'o'):
            thisNode.endState = 'o'
        if(side == 'A'):
            thisNode.endState = 'd'
    else:
        for i in range(0,9):
            if(layout[i] == '_'):
                tstr = list(layout)
                tstr[i] = parent
                thisNode.children.append("".join(tstr))
                if (parent == 'x'):
                    CreateAllBoards("".join(tstr),'o')
                else:
                    CreateAllBoards("".join(tstr),'x')


def main():
    CreateAllBoards('_________', 'x')
    children = 0
    xWins = 0
    oWins = 0
    draws = 0
    for boardNode in AllBoards.values():
        children += len(boardNode.children)
        if(boardNode.endState == 'x'):
            xWins += 1
        if(boardNode.endState == 'o'):
            oWins += 1
        if(boardNode.endState == 'd'):
            draws += 1
    notends = len(AllBoards) - xWins - oWins - draws
    print(len(AllBoards), "boards", children, "children")
    print(xWins, "xWins", oWins, "oWins", draws, "draws", notends, "not-ends")

main()