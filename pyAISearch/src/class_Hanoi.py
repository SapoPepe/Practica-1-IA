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
        self.towers = [[], ["A", "C", "B"], []]
        self.nivel = 0
        self.bloques_incorrectos = 0

    def __str__(self):
        s = "Torres de Hanoi:\n"
        for i, tower in enumerate(self.towers):
            s += f"Torre {i}: {tower}\n"
        return s

    ''' return heuristic '''

    def getH(self):


        ''' compare two states
        in this case two states are equal if their location is the same
        '''

    def __eq__(self, s):
        return (self.nivel == s.nivel) and (self.bloques_incorrectos == s.bloques_incorrectos)


class HanoiPlanning(AISearchProblem):
    '''
    Find a path from origin to target location
    '''

    def __init__(self):
        self.towers = [["B", "C", "A"], [], []]
        self.target = 0                             #Se comparará con el número de bloques incorrectos
        self.state = HanoiState()


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
