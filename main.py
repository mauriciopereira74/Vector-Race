from Race import Race
from readFile import readFile
from tkinter import *
from track import *
from vectorrace_ler import *
from vectorrace_criar import *
from tk import TrackView
from os import listdir
from os.path import isfile, join

def main():
    global default 
    default = "circuito0.txt"
    readClass = readFile("")
    posInit = readClass.PInicialXY()
    posFinal = readClass.PFinalXY()
    problema = Race("", posInit, "(0,0)")
    problema.cria_grafo("")
    saida = -1
    saida1 = -1
    saida2 = -1
    saida3 = -1
    saida4 = -1
    saidaCir = -1
    saidaCir2 = -2

    while saida != 0:
        print("|----------------- MENU ----------------|")
        print("|---------------------------------------|")
        print("|------- 99 -> Escolher Circuito -------|")
        print(f"|--------- Atual: {default} --------|")
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
        saida = input("\nIntroduza a sua Opção -> ")
        try:
            saida = int(saida)
        except ValueError:
            print("Introduza um número válido\n")
            continue
            #l = input("Prima ENTER para continuar")
        if saida == 99:
            while saidaCir != 0:
                print("|--------------- CIRCUITOS -------------|")
                print("|---------------------------------------|")
                onlyfiles = [f for f in listdir("Circuitos/") if isfile(join("Circuitos/", f))]
                i=1
                for i, circ in enumerate(onlyfiles):
                    res = f" {i} -> {circ} "
                    if len(res) == 18:
                        print("|----------" + res + " ----------|")
                    elif len(res) == 19:
                        print("|----------" + res + " ---------|")
                    elif len(res) == 20:
                        print("|----------" + res + " --------|")
                    elif len(res) == 22:
                        print("|----------" + res + " -------|")
                    print("|---------------------------------------|")
                print("|---------------------------------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saidaCir2 = input("Introduza a sua opção-> ")
                try:
                   saidaCir2 = int(saidaCir2)
                except ValueError:
                    print("Introduza um número válido\n")
                    continue
                print(i)
                print(saidaCir2 in range(i))
                print(range(i))
                print(saidaCir2)
                tmp = range(0, i+1)
                print(tmp)
                if saidaCir2 in tmp:
                    circuito_path = onlyfiles[(saidaCir2)]
                    readClass = readFile(circuito_path)
                    posInit = readClass.PInicialXY()
                    problema = Race(circuito_path, posInit, "(0,0)")
                    problema.cria_grafo(circuito_path)
                    default = f"circuito{saidaCir2}.txt"
                    print(default)
                    break;
                else:
                    print("Introduza um número válidooooo\n")
                    continue
        if saida == 0:
            print("Menu Anterior...")
            break;
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
                print("|------------- 9 -> Voltar -------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida2 = input("\nIntroduza a sua Opção -> ")
                try:
                   saida2 = int(saida2)
                except ValueError:
                    print("Introduza um número válido\n")
                    continue                
                if saida2 == 9:
                    print("Menu Anterior...")
                    break;
                elif saida2 == 0:
                    print("Saindo...")
                    saida = 0
                elif saida2 == 1:
                    print("\nCircuito.txt")
                    string = readClass.demonstra()
                    print(string + "\n")
                    l = input("Prima ENTER para continuar")
                elif saida2 == 2:
                    app = Application()
                    app.mainloop()
                    l = input("Prima ENTER para continuar")
                elif saida2 == 3:
                    app2 = Application2()
                    app2.mainloop()
                    l = input("Prima ENTER para continuar")
                else: 
                    print("Introduza um número válido\n")
                    continue

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
                print("|------------- 9 -> Voltar -------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida3 = input("\nIntroduza a sua Opção -> ")
                try:
                   saida3 = int(saida3)
                except ValueError:
                    print("Introduza um número válido\n")
                    continue                
                if saida3 == 9:
                    print("Menu Anterior...")
                    break;
                elif saida3 == 0:
                    print("Saindo...")
                    saida = 0
                elif saida3 == 1:
                    print(problema.g)
                    print(problema.g.m_graph)
                    l = input("Prima ENTER para continuar")
                elif saida3 == 2:
                    problema.g.desenha()
                    l = input("Prima ENTER para continuar")
                elif saida3 == 3:
                    print(problema.g.m_graph.keys())
                    l = input("Prima ENTER para continuar")
                elif saida3 == 4:
                    print(problema.g.imprime_aresta())
                    l = input("Prima ENTER para continuar")
                else:
                    print("Introduza um número válido\n")
                    continue                
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
                print("|------------- 9 -> Voltar -------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida4 = input("\nIntroduza a sua Opção -> ")
                try:
                    saida4 = int(saida4)
                except:
                    print("Introduza um número válido\n")
                    continue
                if saida4 == 9:
                    print("Menu Anterior...")
                    break;
                elif saida4 == 0:
                    print("Saindo...")
                    saida = 0
                elif saida4 == 1:
                    caminho = problema.g.procura_DFS(posInit,posFinal)
                    path, custo = caminho  # type: ignore
                    print("\nCaminho encontrado: ", end="")
                    print(*path, sep=' -> ')
                    print(f"Custo Total: {str(custo)}\n")
                    print(problema.mostraCaminho(path))
                    l = input("Prima ENTER para continuar")
                elif saida4 == 2:
                    caminho = problema.g.procura_BFS(posInit,posFinal)
                    path, custo = caminho  # type: ignore
                    print("\nCaminho encontrado: ", end="")
                    print(*path, sep=' -> ')
                    print(f"Custo Total: {str(custo)}\n")
                    print(problema.mostraCaminho(caminho[0]))
                    l = input("Prima ENTER para continuar")
                elif saida4 == 3:
                    print("Nada (para já)")
                elif saida4 == 4:
                    print("Nada (para já)")
                else:
                    print("Introduza um número válido\n")
                    continue        
            #inicio = input("Nodo inicial->")
            # fim = input("Nodo final->")
            # caminho = problema.solucaoBFS(posInit, posFinal)
            # print(caminho)
            # if caminho != None:
            #     a = caminho[0]
            #     lista = problema.imprimeA(a)
            #     print(lista)
            #l = input("prima ENTER para continuar")
        else:
            print("Introduza um número válido\n")
            continue;
            # print("Introduza um número válido\n")
            # l = input("Prima ENTER para continuar")

if __name__ == "__main__":
    main()