
from class_MinMax import AITicTocProblem,AITicTocState
from pyAIMinMax import AIMinMax

def chooseMinLocation(mm, state):
    minV = 1000
    minP = None
    for pos in state.freeLocations():
        newState = state.movePlayer(pos)
        v = mm.maxValue(newState)
        if v < minV:
            minV = v
            minP = pos
    return minP, minV

def play(mm):
    s=AITicTocState("A")
    while not s.isTerminal():
        print(s)
        r=0
        c=int(input("col="))
        freeLocations = s.freeLocations()
        while (r, c) not in freeLocations:
            r=0
            c=int(input("col="))
        s.setPlayer((r,c))
        s.changePlayer()
        if s.isTerminal(): break
        print(s)
        pos, v = chooseMinLocation(mm, s)
        s.setPlayer(pos)
        s.changePlayer()
    print(s)
    if s.win("A"):
        print("A wins")
    if s.win("B"):
        print("B wins")
    if not s.win("A") and not s.win("B"):
        print("Draw")

if __name__ == '__main__':
    p=AITicTocProblem()
    mm=AIMinMax(p)
    play(mm)