
from class_MinMax import AITicTocProblem,AITicTocState

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
    s=AITicTocState("A")
    while not s.isTerminal():
        print(s)
        r=0
        c=int(input("col="))
        while not s.isFree((r,c)):
            r=0
            c=int(input("col="))
        s.setPlayer((r,c))
        s.changePlayer()
        if s.isTerminal(): break
        print(s)
        pos,v=chooseMaxLocation(mm, s)
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