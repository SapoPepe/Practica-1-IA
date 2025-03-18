import math
import copy
import numpy as np
from pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearchProblem.pyState import AISearchState


class HanoiState(AISearchState):
    def __init__(self):
        self.towers = [[], ["B", "C", "A"], []]
        self.nivel = 0
        self.bloques_incorrectos = []

    def __str__(self):
        s = " 0123456789\n"
        for row in range(self.map.shape[0]):
            s += str(row)
            for col in range(self.map.shape[1]):
                if (col, row) == self.location:
                    s += "@"
                    continue
                if self.map[row, col] == 0:
                    s += " "
                if self.map[row, col] == 1:
                    s += "#"
            s += "\n"
        return s

    ''' return heuristic '''

    def getH(self):


    ''' compare two states
        in this case two states are equal if their location is the same '''

    def __eq__(self, s):



class HanoiPlanning(AISearchProblem):
    '''
    Find a path from origin to target location
    '''

    def __init__(self):
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

