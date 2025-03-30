import copy
from pyAISearchProblem.pyProblem import AISearchProblem
class AITicTocState(object):
    def __init__(self,startPlayer="A"):
        self.board=[[" "," "," "," "," "]]
        self.depth=0
        self.player=startPlayer #can be "O"
    def setPiece(self,loc,c):
        self.board[loc[0]][loc[1]]=c
    def setPlayer(self,loc):
        self.setPiece(loc,self.player)
    def movePlayer(self,pos):
        newState=copy.deepcopy(self)
        newState.setPlayer(pos)
        newState.incDepth()
        newState.changePlayer()
        return newState
    def winPlayer(self,c):
        lenght = len(self.board)-1
        if (self.board[0][0] == c and c == "B") or (self.board[0][lenght] == c and c == "A"): return True
        return False
    def win(self,c):
        return self.winPlayer(c)
    def isFree(self,loc):
        return self.board[loc[0]][loc[1]]==" "
    def freeLocations(self):
        holes=[]
        row = 0
        lenght = len(self.board)
        for col in range(lenght):
            if self.isFree((row,col)): holes.append((row,col))
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
        return str(self.board)
class AITicTocProblem(AISearchProblem):
    def __init__(self, startPlayer="A"):
        self.currentState=AITicTocState(startPlayer)
    def expand(self,state):
        successors=[]
        for pos in state.freeLocations():
            newState=state.movePlayer(pos)
            successors.append(newState)
        return successors