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
            print(f"Acción realizada: {cn.action}")
            list_explored = [elem.state.towers for elem in sg.explored]
            print(f"Lista expandidos: {list_explored}")
            print(f"Valor de f:{cn.getF()}")
            print(f"Valor de g: {cn.depth}")
            print(f"Valor de h:{cn.getState().getH()}")
            cn=cn.getFather()
        print()
        print("Estado inicial:")
        print(pp.state)
        list_explored = [elem.state.towers for elem in sg.explored]
        print(f"Lista expandidos: {list_explored}")
        print(f"Valor de f:{cn.getF()}")
        print(f"Valor de g: {cn.depth}")
        print(f"Valor de h:{pp.state.getH()}")


        print("Arbol completo:")


        def imprimir_arbol(lista):
            hijos = [[] for _ in range(len(lista))]

            for i, nodo in enumerate(lista):
                padre = nodo.father
                if padre is not None:  # Ignorar la raíz
                    padre = nodo.father
                    hijos[lista.index(padre)].append(i)


            def imprimir_nodo(indice, profundidad):
                nodo = lista[indice]
                print("\t" * profundidad + f"- Nodo {indice}:\n")
                print(nodo.state.imprimir_por_nivel(profundidad))

                for hijo in hijos[indice]:
                    imprimir_nodo(hijo, profundidad + 1)


            imprimir_nodo(0, 0)


        imprimir_arbol(sg.explored)