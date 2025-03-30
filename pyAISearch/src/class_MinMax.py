import copy
from pyAISearchProblem.pyProblem import AISearchProblem
class AITicTocState(object):
    def __init__(self,startPlayer="A"):
        self.board=[["A"," "," "," ","B"]]
        self.depth=0
        self.player=startPlayer #can be "O"
    def removePiece(self, loc, c):
        for i in range(5):
            if self.board[0][i] == c:
                self.board[0][i] = " "
    def setPiece(self,loc,c):
        self.board[loc[0]][loc[1]]=c
    def setPlayer(self, loc):
        # Eliminar posición actual
        current_pos = self.board[0].index(self.player)
        self.board[0][current_pos] = " "
        # Colocar en nueva posición
        self.board[loc[0]][loc[1]] = self.player
    def movePlayer(self,pos):
        newState=copy.deepcopy(self)
        newState.setPlayer(pos)
        newState.incDepth()
        newState.changePlayer()
        return newState
    def winPlayer(self,c):
        length = len(self.board[0])-1
        if (self.board[0][0] == c and c == "B") or (self.board[0][length] == c and c == "A"):
            return True
        return False
    def win(self,c):
        return self.winPlayer(c)
    def isFree(self,loc):
        return self.board[loc[0]][loc[1]]==" "
    def freeLocations(self):
        holes = []
        row = 0
        current_pos = self.board[0].index(self.player)
        length = len(self.board[0])
        
        if self.player == "A":
            # Moverse a la derecha
            if current_pos + 1 < length:
                if self.isFree((row, current_pos + 1)):
                    holes.append((row, current_pos + 1))
                elif current_pos + 2 < length and self.isFree((row, current_pos + 2)):
                    holes.append((row, current_pos + 2))
        else:  # Jugador "B"
            # Moverse a la izquierda
            if current_pos - 1 >= 0:
                if self.isFree((row, current_pos - 1)):
                    holes.append((row, current_pos - 1))
                elif current_pos - 2 >= 0 and self.isFree((row, current_pos - 2)):
                    holes.append((row, current_pos - 2))
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
        if self.win("A"): return  1000
        if self.win("B"): return -1000
        else: return 0
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