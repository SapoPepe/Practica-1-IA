from class_Hanoi import HanoiPlanning, HanoiState
from pyAISearchSolverGraph import AISearchSolverGraph

if __name__ == '__main__':
    pp=HanoiPlanning()
    sg=AISearchSolverGraph(pp)
    found=sg.search()
    if not found:
        print("Solution not found")
    else:
        print("The solution is,....")
        cn=sg.getCurrentNode()
        while cn.getFather():
            print(cn.getState())
            cn=cn.getFather()