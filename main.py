from Race import Race
from readFile import readFile
from tkinter import *
from track import *
from vectorrace_ler import *
from vectorrace_criar import *
from tk import TrackView

def main():

    readClass = readFile()
    posInit = readClass.PInicialXY()
    posFinal = readClass.PFinalXY()
    problema = Race(posInit, "(0,0)")
    problema.cria_grafo()
    saida = -1
    saida1 = -1
    saida2 = -1
    saida3 = -1
    saida4 = -1

    while saida != 0:
        print("|----------------- MENU ----------------|")
        print("|---------------------------------------|")
        print("|----- 1 -> Formulação do Problema -----|")
        print("|---------------------------------------|")
        print("|------ 2 -> Circuito VectorRace -------|")
        print("|---------------------------------------|")
        print("|---- 3 -> Pista em Forma de Grafo -----|")
        print("|---------------------------------------|")
        print("|----- 4 -> Estratégia de Procura ------|")
        print("|---------------------------------------|")
        print("|-------------- 0 -> Sair --------------|")
        print("|---------------------------------------|")

        saida = int(input("\nIntroduza a sua Opção -> "))
        if saida == 0:
            print("Saindo..")
        elif saida == 1:
            # while saida2 != 0:
            print("A definir...")
            l = input("Prima ENTER para continuar")
        elif saida == 2:
            while saida2 != 0:
                print("|----------------- MENU ----------------|")
                print("|---------------------------------------|")
                print("|------ 1 -> Imprimir Circuito.txt -----|")
                print("|---------------------------------------|")
                print("|--- 2 -> VectorRace do Circuito.txt ---|")
                print("|---------------------------------------|")
                print("|-------- 3 -> Criar VectorRace --------|")
                print("|---------------------------------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida2 = int(input("\nIntroduza a sua Opção -> "))
                if saida2 == 0:
                    print("Saindo..")
                if saida2 == 1:
                    print("\nCircuito.txt")
                    string = readClass.demonstra()
                    print(string + "\n")
                    l = input("Prima ENTER para continuar")
                if saida2 == 2:
                    app = Application()
                    app.mainloop()
                    l = input("Prima ENTER para continuar")
                if saida2 == 3:
                    app2 = Application2()
                    app2.mainloop()
                    l = input("Prima ENTER para continuar")
                else: 
                    print("Introduza um número válido\n")
                    l = input("Prima ENTER para continuar")

        elif saida == 3:
            while saida3 != 0:
                print("|----------------- MENU ----------------|")
                print("|---------------------------------------|")
                print("|--------- 1 -> Imprimir Grafo ---------|")
                print("|---------------------------------------|")
                print("|--------- 2 -> Desenhar Grafo ---------|")
                print("|---------------------------------------|")
                print("|---- 3 -> Imprimir  nodos de Grafo ----|")
                print("|---------------------------------------|")
                print("|--- 4 -> Imprimir arestas de Grafo ----|")
                print("|---------------------------------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida3 = int(input("\nIntroduza a sua Opção -> "))
                if saida3 == 0:
                    print("Saindo..")
                if saida3 == 1:
                    print(problema.g)
                    print(problema.g.m_graph)
                    l = input("Prima ENTER para continuar")
                if saida3 == 2:
                    problema.g.desenha()
                    l = input("Prima ENTER para continuar")
                if saida3 == 3:
                    print(problema.g.m_graph.keys())
                    l = input("Prima ENTER para continuar")
                if saida3 == 4:
                    print(problema.g.imprime_aresta())
                    l = input("Prima ENTER para continuar")

        elif saida == 4:
            while saida4 != 0:
                caminho = []
                print("|----------------- MENU ----------------|")
                print("|---------------------------------------|")
                print("|- 1 -> Algoritmo em Profundidade(DFS)- |")
                print("|---------------------------------------|")
                print("|---- 2 ->Algoritmo em Largura(BFS) ----|")
                print("|---------------------------------------|")
                print("|---------- 3 -> Algoritmo A* ----------|")
                print("|---------------------------------------|")
                print("|-------- 4 -> Algoritmo Greedy --------|")
                print("|---------------------------------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida4 = int(input("\nIntroduza a sua Opção -> "))
                if saida4 == 0:
                    print("Saindo..")
                if saida4 == 1:
                    #caminho = solucaoDFS(posInit,posFinal)
                    caminho = problema.g.procura_DFS(posInit,posFinal)
                    print(str(caminho) + "\n")
                    print(problema.mostraCaminho(caminho[0]))
                    l = input("Prima ENTER para continuar")
                if saida4 == 2:
                    caminho = problema.g.procura_BFS(posInit,posFinal)
                    print(str(caminho) + "\n")
                    print(problema.mostraCaminho(caminho[0]))
                    l = input("Prima ENTER para continuar")
                if saida4 == 3:
                    print("Nada (para já)")
                if saida4 == 4:
                    print("Nada (para já)")

            #inicio = input("Nodo inicial->")
            # fim = input("Nodo final->")
            # caminho = problema.solucaoBFS(posInit, posFinal)
            # print(caminho)
            # if caminho != None:
            #     a = caminho[0]
            #     lista = problema.imprimeA(a)
            #     print(lista)
            l = input("prima ENTER para continuar")
        else:
            print("Introduza um número válido\n")
            l = input("Prima ENTER para continuar")

if __name__ == "__main__":
    main()