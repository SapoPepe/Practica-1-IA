'''
Created on 25 Feb 2021

@author: Francisco Dominguez
'''
from pyAISearchSolver import AISearchSolver

class AIMinMax(AISearchSolver):
    def __init__(self, problem, max_depth=10):
        super().__init__(problem)
        self.max_depth = max_depth

    def maxValue(self, state, depth=0):
        if state.isTerminal() or depth >= self.max_depth:
            return state.utility()
        maxUpToNow = -10e100
        successors = self.problem.expand(state)
        for s in successors:
            maxUpToNow = max(maxUpToNow, self.minValue(s, depth + 1))
        return maxUpToNow

    def minValue(self, state, depth=0):
        if state.isTerminal() or depth >= self.max_depth:
            return state.utility()
        minUpToNow = 10e100
        successors = self.problem.expand(state)
        for s in successors:
            minUpToNow = min(minUpToNow, self.maxValue(s, depth + 1))
        return minUpToNow