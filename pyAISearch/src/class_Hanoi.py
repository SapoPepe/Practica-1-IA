import math
import copy
import numpy as np
from pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearchProblem.pyState import AISearchState


class HanoiState(AISearchState):
    '''
    La base de la torre es el la casilla 0 de la lista y la cima la casilla n-1
    '''
    def __init__(self):
        self.towers = [[], [], []]
        self.nivel = 0
        self.bloques_incorrectos = 0

    def __str__(self):
        s = "Torres de Hanoi:\n"
        for i, tower in enumerate(self.towers):
            s += f"Torre {i}: {tower}\n"
        return s

    ''' return heuristic '''

    def getH(self):
        incorrectos = 0
        for i in range(len(self.towers)):
            for j in range(len(self.towers[i])):
                if self.towers[i][j] == "C" and j+1 != len(self.towers[i]): incorrectos += 1    # Si la C no se encuentra en la última posición de la torre se considera incorrecto
                if self.towers[i][j] == "B" and j != 1 and j+1 != "C": incorrectos += 1         # Si la B no se encuenta en la segunda posición y no tiene debajo a C, se considera incorrecto
                if self.towers[i][j] == "A" and j != 2 and j+1 != "B": incorrectos += 1         # Si la A no se encuenta en la tercera posición y no tiene debajo a B, se considera incorrecto

        return incorrectos

    def __eq__(self, s):
        return (self.nivel + self.bloques_incorrectos == s.nivel + s.bloques_incorrectos)



class HanoiPlanning(AISearchProblem):
    '''
    Find a path from origin to target location
    '''

    def __init__(self):
        self.state = HanoiState()
        self.towers = [["B", "C", "A"], [], []]

        self.target = 0                             #Se comparará con el número de bloques incorrectos
        # Mover de una torre a otra (origen, destino)
        self.actions = [(0,1), (0,2), (1,0), (1,2), (2,0), (2,1)]

    def getStateInit(self):
        return self.state

    def canTakeAction(self, a, state):


    def takeAction(self, a, state):


    # return a collection of action,state,cost
    def sucessors(self, state):
        sucessors = []
        for a in self.actions:
            if self.canTakeAction(a, state):
                newState = self.takeAction(a, state)
                sucessors.append((a, newState, 1))
        return sucessors

    def isGoal(self, state):
        return state.getBloquesIncorrectos() == self.target
