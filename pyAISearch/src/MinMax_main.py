from collections import defaultdict

from class_MinMax import AITicTocProblem, AITicTocState
from pyAIMinMax import AIMinMax
import copy

tree = []
user_moves = []
ai_moves = []

def chooseMinLocation(mm, state):
    minV = 1e100
    minP = None
    for pos in state.freeLocations():
        newState = state.movePlayer(pos)
        v = mm.maxValue(newState)
        if newState.win("A"): 
            e = float('inf')
        elif newState.win("B"): 
            e = -float('inf')
        else:
            distancia_A = 4 - newState.board[0].index("A")
            distancia_B = newState.board[0].index("B")
            e = distancia_B - distancia_A
        tree.append((copy.deepcopy(state), copy.deepcopy(newState), e))
        
        if v < minV:
            minV = v
            minP = pos
    return minP, minV

def play(mm):
    s = AITicTocState("A")
    while not s.isTerminal():
        print(s)
        r = 0
        c = int(input("col="))
        freeLocations = s.freeLocations()
        while (r, c) not in freeLocations:
            r = 0
            c = int(input("col="))
        s.setPlayer((r, c))
        s.changePlayer()
        user_moves.append(copy.deepcopy(s))
        if s.isTerminal(): break
        print(s)
        pos, v = chooseMinLocation(mm, s)
        s.setPlayer(pos)
        ai_moves.append(copy.deepcopy(s))
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

def print_tree(tree, user_moves, ai_moves, final_move):
    arbol = defaultdict(list)

    for padre, hijo, v in tree:
        found = False
        for key in arbol.keys():
            if key.board == padre.board:
                arbol[key].append((hijo, v))
                found = True
                break
        if not found:
            arbol[padre].append((hijo, v))

    nivel = 0
    ai_move_index = 0

    print()
    print("Árbol completo:")
    for i, move in enumerate(user_moves):
        current_parent = None
        for key in arbol.keys():
            if key.board == move.board:
                current_parent = key
                break
    
        if nivel == 0:
            print("Estado inicial:")
        else:
            print("Movimiento de A:")
        print(nivel * "\t" + str(move.board))

        print("Posibles movimientos de B:")
        if current_parent:
            for child, value in arbol[current_parent]:
                print((nivel + 1) * "\t" + f"{child.board} (e: {value})")
       
        if ai_move_index < len(ai_moves):
            print("Movimiento elegido por B:")
            print((nivel + 1) * "\t" + str(ai_moves[ai_move_index].board))
            ai_move_index += 1

        nivel += 1

    print("\nEstado final: " + str(final_move.board))

if __name__ == '__main__':
    p = AITicTocProblem()
    mm = AIMinMax(p)
    final_move = play(mm)
    print_tree(tree, user_moves, ai_moves, final_move)