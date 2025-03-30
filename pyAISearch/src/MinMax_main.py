from pyAITicTocProblem import AITicTocProblem,AITicTocState
from pyAIMinMax import AIMinMax
def chooseMaxLocation(mm,state):
    maxV=-1000
    for pos in state.freeLocations():
        newState=state.movePlayer(pos)
        v=mm.minValue(newState)
        if v>maxV:
            maxV=v
            maxP=pos
    return maxP,v
def play(mm):
    s=AITicTocState("O")

if __name__ == '__main__':
    p=AITicTocProblem()
    mm=AIMinMax(p)
    play(mm)