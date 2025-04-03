from collections import defaultdict

from class_MinMax import AITicTocProblem,AITicTocState
from pyAIMinMax import AIMinMax
import copy

tree = []
user_moves = []

def chooseMinLocation(mm, state):
    minV = 1000
    minP = None
    for pos in state.freeLocations():
        newState = state.movePlayer(pos)
        tree.append((copy.deepcopy(state), copy.deepcopy(newState)))
        v = mm.maxValue(newState)
        if v < minV:
            minV = v
            minP = pos
    return minP, minV

def play(mm):
    s=AITicTocState("A")
    while not s.isTerminal():
        print(s)
        user_moves.append(copy.deepcopy(s))
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
    final_move = copy.deepcopy(s)
    if s.win("A"):
        print("A wins")
    if s.win("B"):
        print("B wins")
    if not s.win("A") and not s.win("B"):
        print("Draw")
    return final_move

def print_tree(tree, user_moves,final_move):
    arbol = defaultdict(list)

    found = False
    key_tree = None
    for padre, hijo in tree:
        for key in arbol.keys():
            if key.board == padre.board:
                found = True
                key_tree = key
        if found:
            arbol[key_tree].append(hijo)
            found = False
        else:
            arbol[padre].append(hijo)

    nivel = 0

    print()
    print("Árbol completo:")
    for move in user_moves:
        if nivel == 0:
            print("Estado inicial:")
        else:
            print("Movimiento elegido:")
        print(nivel * "\t" + str(move.board))
        print("Movimiento del usuario:")
        print(nivel * "\t" + str(list(arbol.keys())[nivel]))
        print("Posibles movimientos de la IA:")
        for state in arbol[list(arbol.keys())[nivel]]:
            print((nivel + 1) * "\t" + str(state))
        nivel += 1

    print("Estado final: " + str(final_move.board))

if __name__ == '__main__':
    p=AITicTocProblem()
    mm=AIMinMax(p)
    final_move=play(mm)
    print_tree(tree, user_moves, final_move)