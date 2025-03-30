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
        if (self.board[0][0] == c and c == "B") or (self.board[0][lenght] == c and c == "A"):
            return True
        return False
    def win(self,c):
        return self.winPlayer(c)
    def count(self,c):
        counter=0
        for row in range(3):
            for col in range(3):
                if self.board[row][col]==c:
                    counter+=1
        return counter
    def isFree(self,loc):
        return self.board[loc[0]][loc[1]]==" "
    def freeLocations(self):
        holes=[]
        for row in range(3):
            for col in range(3):
                if self.isFree((row,col)):
                    holes.append((row,col))
        return holes
    def changePlayer(self):
        if self.player=="X":
            self.player="O"
            return
        self.player="X"
    def incDepth(self):
        self.depth+=1
    def isTerminal(self):
        return self.win("X") or self.win("O")
    def utility(self):
        if self.win("X"): return  100
        if self.win("O"): return -100
    def __str__(self):
        s=""
        for row in range(3):
            for col in range(3):
                s+=self.board[row][col]
            s+="\n"
        s+=str(self.depth)+"---"+self.player
        return s
class AITicTocProblem(AISearchProblem):
    def __init__(self, startPlayer="A"):
        self.currentState=AITicTocState(startPlayer)
    def expand(self,state):
        successors=[]
        for pos in state.freeLocations():
            newState=state.movePlayer(pos)
            successors.append(newState)
        return successors