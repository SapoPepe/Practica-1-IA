import copy
from pyAISearchProblem.pyProblem import AISearchProblem
class AITicTocState(object):
    def __init__(self,startPlayer="A"):
        self.board=[["A"," "," "," ","B"]]
        self.depth=0
        self.player=startPlayer #can be "O"
    def setPiece(self,loc,c):
        self.board[loc[0]][loc[1]]=c
    def setPlayer(self,loc):
        for pos in range(len(self.board[0])):
            if self.board[0][pos] == self.player: self.board[0][pos] = " "
        self.setPiece(loc,self.player)
    def movePlayer(self,pos):
        newState=copy.deepcopy(self)
        newState.setPlayer(pos)
        newState.incDepth()
        newState.changePlayer()
        return newState
    def winPlayer(self,c):
        lenght = len(self.board[0])-1
        if (self.board[0][0] == c and c == "B") or (self.board[0][lenght] == c and c == "A"): return True
        return False
    def win(self,c):
        return self.winPlayer(c)
    def isFree(self,loc):
        return self.board[loc[0]][loc[1]]==" "
    def freeLocations(self):
        holes=[]
        row = 0
        pos = self.board[0].index(self.player)
        length = len(self.board[0])

        if pos - 1 >= 0 and self.isFree((row, pos - 1)):
            holes.append((row, pos - 1))
        elif pos - 2 >=0 : holes.append((row, pos-2))

        if pos + 1 < length and self.isFree((row, pos + 1)):
            holes.append((row, pos + 1))
        elif pos + 2 < length: holes.append((row, pos+2))


        return holes
    def changePlayer(self):
        if self.player=="A":
            self.player="B"
            return
        self.player="A"
    def incDepth(self):
        self.depth+=1
    def isTerminal(self):
        return self.win("A") or self.win("B")
    def utility(self):
        if self.win("A"): return  100
        if self.win("B"): return -100
    def __str__(self):
        return str(self.board[0])
class AITicTocProblem(AISearchProblem):
    def __init__(self, startPlayer="A"):
        self.currentState=AITicTocState(startPlayer)
    def expand(self,state):
        successors=[]
        for pos in state.freeLocations():
            newState=state.movePlayer(pos)
            successors.append(newState)
        return successors