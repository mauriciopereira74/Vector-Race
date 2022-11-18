from Race import Race
from readFile import readFile

def main():

    readClass = readFile()
    posInit = readClass.PInicialXY()
    problema = Race(posInit, "(0,0)")
    problema.cria_grafo()
    saida = -1

    while saida != 0:
        print("|----------------- MENU ----------------|")
        print("|---------------------------------------|")
        print("|------ 1 -> Imprimir Circuito.txt -----|")
        print("|---------------------------------------|")
        print("|------ 2 -> Imprimir VectorRace -------|")
        print("|---------------------------------------|")
        print("|-------- 3 -> Criar VectorRace --------|")
        print("|---------------------------------------|")
        print("|--------- 4 -> Imprimir Grafo ---------|")
        print("|---------------------------------------|")
        print("|--------- 5 -> Desenhar Grafo ---------|")
        print("|---------------------------------------|")
        print("|---- 6 -> Imprimir Nodos de Grafo -----|")
        print("|---------------------------------------|")
        print("|--- 7 -> Imprimir Arestas de Grafo ----|")
        print("|---------------------------------------|")
        print("|-------------- 0 -> Sair --------------|")
        print("|---------------------------------------|")

        saida = int(input("\nIntroduza a sua Opção -> "))
        if saida == 0:
            print("Saindo..")
        elif saida == 1:
            print("\nCircuito")
            string = readClass.demonstra()
            print(string + "\n")
            l = input("Prima ENTER para continuar")
        elif saida == 2:
            print("Nada")
            l = input("Prima ENTER para continuar")
        elif saida == 3:
            print("Nada")
            l = input("Prima ENTER para continuar")
        elif saida == 4:
            print(problema.g.m_graph)
            l = input("Prima ENTER para continuar")
        elif saida == 5:
            problema.g.desenha()
            l = input("Prima ENTER para continuar")
        elif saida == 6:
            print(problema.g.m_graph.keys())
            l = input("Prima ENTER para continuar")
        elif saida == 7:
            print(problema.g.imprime_aresta())
            l = input("Prima ENTER para continuar")
        else:
            print("Número Inválido")
            l = input("Prima ENTER para continuar")

if __name__ == "__main__":
    main()
