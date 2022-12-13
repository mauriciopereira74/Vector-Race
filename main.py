from Race import Race
from readFile import readFile
from tkinter import *
from track import *
from vectorrace_ler import *
from vectorrace_criar import *
from vectorrace_comp import *
from tk import TrackView
from os import listdir
from os.path import isfile, join

def main():
    global default 
    default = "circuito0.txt"
    readClass = readFile("")
    posInit = readClass.PInicialXY()
    posFinal = readClass.PFinalXY()
    posCheckpoint = readClass.PCheckXY()
    problema = Race("", posInit, posFinal, posCheckpoint, "(0,0)")
    
    saida = -1
    saida2 = -1
    saida3 = -1
    saida4 = -1
    saida5 = -1
    saida51 = -1
    saida52 = -1
    saida53 = -1
    saidaCir = -1
    saidaCir2 = -2
    selectedAlg = 0

    while saida != 0:
        print("\n|----------------- MENU ----------------|")
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
        print("|------ 5 -> Ambiente Competitivo ------|")
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
                onlyfiles = [f for f in listdir("Circuitos/") if isfile(join("Circuitos/", f))]
                print("\n|--------------- CIRCUITOS -------------|")
                print("|---------------------------------------|")
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
                if saidaCir2 in range(0, i+1):   # type: ignore
                    circuito_path = onlyfiles[(saidaCir2)]
                    readClass = readFile(circuito_path)
                    posInit = readClass.PInicialXY()
                    posFinal = readClass.PFinalXY()
                    posCheckpoint = readClass.PCheckXY()
                    problema = Race(circuito_path, posInit, posFinal, posCheckpoint, "(0,0)")
                    default = f"circuito{saidaCir2}.txt"
                    break;
                else:
                    print("Introduza um número válido\n")
                    continue

        elif saida == 0:
            print("Saindo...")
            break;
        elif saida == 1:
            # while saida2 != 0:
            print("\n|------- FORMULACAO DO PROBLEMA --------|")
            a = """
Estado Inicial: Ponto de Partida (x,y), posição inicial onde o Jogador P se encontra definido nas coordenadas cartesianas.
Estado Final/Teste Objetivo: Cruzar a meta, ou seja, o Jogador P sobrepor a meta F, igualmente definido por coordenadas cartesianas.
Operadores:
	-> Esquerda: O jogador com Velocidade v e Aceleração a deseja movimentar-se para a esquerda. 
Se a posição estiver livre, identificada por -, o Jogador movimenta-se, aumentando a sua Velocidade e atualizando a sua Posição. 
Caso esteja ocupada, identificada por X, o Jogador fica com Velocidade igual zero e mantém-se na mesma posição;
	-> Direita: O jogador com Velocidade v e Aceleração a deseja movimentar-se para a direita. 
Se a posição estiver livre, identificada por -, o Jogador movimenta-se, aumentando a sua Velocidade e atualizando a sua Posição. 
Caso esteja ocupada, identificada por X, o Jogador fica com Velocidade igual zero e mantém-se na mesma posição;
	-> Cima: O jogador com Velocidade v e Aceleração a deseja movimentar-se para cima. 
Se a posição estiver livre, identificada por -, o Jogador movimenta-se, aumentando a sua Velocidade e atualizando a sua Posição. 
Caso esteja ocupada, identificada por X, o Jogador fica com Velocidade igual zero e mantém-se na mesma posição;
	-> Baixo: O jogador com Velocidade v e Aceleração a deseja movimentar-se para baixo. 
Se a posição estiver livre, identificada por -, o Jogador movimenta-se, aumentando a sua Velocidade e atualizando a sua Posição.
Caso esteja ocupada, identificada por X, o Jogador fica com Velocidade igual zero e mantém-se na mesma posição.
Estado Possíveis:
	-> Parado após bater em obstáculo;
	-> Parado após sair dos limites da pista;
	-> Movimentar-se para a frente;
	-> Movimentar-se para trás;
	-> Movimentar-se para a esquerda;
	-> Movimentar-se para a direita;
	-> Movimentar-se para a diagonal superior esquerda;
	-> Movimentar-se para a diagonal superior direita;
	-> Movimentar-se para a diagonal inferior esquerda;
	-> Movimentar-se para a diagonal inferior direita.
Custo da Solução: Cada ação bem sucedida custa uma unidade, caso saia dos limites da pista este tem um custo de vinte e cinco unidades.
            """
            print(a)
            l = input("Prima ENTER para continuar")
        elif saida == 2:
            while saida2 != 0:
                print("\n|----------- VECTOR RACE MENU ----------|")
                print("|---------------------------------------|")
                print(f"|------ 1 -> Imprimir {default} ----|")
                print("|---------------------------------------|")
                print(f"|-- 2 -> VectorRace do {default} ---|")
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
                    print(f"\nCircuitos/{default}")
                    string = readClass.demonstra()
                    print(string + "\n")
                    l = input("Prima ENTER para continuar")
                elif saida2 == 2:
                    app = Application(default)
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
                print("\n|---------------- GRAFOS ---------------|")
                print("|---------------------------------------|")
                print("|--------- 1 -> Imprimir Grafo ---------|")
                print("|---------------------------------------|")
                print("|--------- 2 -> Desenhar Grafo ---------|")
                print("|---------------------------------------|")
                print("|---- 3 -> Imprimir nodos de Grafo -----|")
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
                print("\n|-------------- ALGORITMOS -------------|")
                print("|--------ALGORITMOS NÃO INFORMADOS------|")
                print("|- 1 -> Algoritmo em Profundidade(DFS) -|")
                print("|---- 2 -> Algoritmo em Largura(BFS) ---|")
                print("|---------------------------------------|")
                print("|--------- ALGORITMOS INFORMADOS -------|")
                print("|---------- 3 -> Algoritmo A* ----------|")
                print("|---------- 31 -> Heurística A* --------|")
                print("|---------------------------------------|")
                print("|-------- 4 -> Algoritmo Greedy --------|")
                print("|-------- 41 -> Heurística Greedy ------|")
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
                    if posCheckpoint == None:
                        caminho = []
                        caminho = problema.g.procura_BFS(posInit,posFinal)
                        path, custo = caminho  # type: ignore
                        print("\nCaminho encontrado: ", end="")
                        print(*path, sep=' -> ')
                        print(f"Custo Total: {str(custo)}\n")
                        print(problema.mostraCaminho(caminho[0]))
                    else:
                        caminho1 = []
                        caminho2 = []
                        caminho1 = problema.g.procura_BFS(posInit, posCheckpoint)
                        path1, custo1 = caminho1  # type: ignore
                        print(caminho1)
                        caminho2 = problema.g.procura_BFS(posCheckpoint, posFinal)
                        path2, custo2 = caminho2  # type: ignore
                        path2.pop(0)
                        pathCompleto = path1 + path2
                        custoTotal = custo1 + custo2
                        print("\nCaminho encontrado: ", end="")
                        print(*pathCompleto, sep=' -> ')
                        print(f"Custo Total: {str(custoTotal)}\n")
                        print(problema.mostraCaminho(pathCompleto))
                    l = input("Prima ENTER para continuar")
                elif saida4 == 3:
                    caminho = problema.g.procura_aStar(posInit,posFinal)
                    path, custo = caminho  # type: ignore
                    problema.g.heuristica_aStar(posFinal)
                    print(problema.g.m_h)
                    print("\nCaminho encontrado: ", end="")
                    print(*path, sep=' -> ')
                    print(f"Custo Total: {str(custo)}\n")
                    print(problema.mostraCaminho(path))
                    l = input("Prima ENTER para continuar")
                elif saida4 == 31:
                    problema.g.heuristica_aStar(posFinal)
                    print(problema.g.m_h)
                elif saida4 == 4:
                    problema.g.heuristica_aStar(posFinal)
                    print(problema.g.m_h)
                    caminho = problema.g.greedy(posInit,posFinal)
                    path, custo = caminho  # type: ignore
                    print("\nCaminho encontrado: ", end="")
                    print(*path, sep=' -> ')
                    print(f"Custo Total: {str(custo)}\n")
                    print(problema.mostraCaminho(path))
                    l = input("Prima ENTER para continuar")
                elif saida4 == 41:
                    problema.g.heuristica_aStar(posFinal)
                    print(problema.g.m_h)
                else:
                    print("Introduza um número válido\n")
                    continue
        elif saida == 5:
            # while saida5 != 0:
                # print("\n|-------- AMBIENTE COMPETITIVO ---------|")
                # print("|---------------------------------------|")
                # print("|------------ 1 -> Jogador1 ------------|")
                # print("|---------------------------------------|")
                # print("|------------ 2 -> Jogador2 ------------|")
                # print("|---------------------------------------|")
                # print("|------------- 3 -> Jogar --------------|")
                # print("|---------------------------------------|")
                # print("|------------- 9 -> Voltar -------------|")
                # print("|-------------- 0 -> Sair --------------|")
                # print("|---------------------------------------|")
                # saida5 = input("\nIntroduza a sua Opção -> ")
                # try:
                #    saida5 = int(saida5)
                # except ValueError:
                    # print("Introduza um número válido\n")
                    # continue
                # if saida5 == 9:
                    # print("Menu Anterior...")
                    # break;
                # elif saida5 == 0:
                    # print("Saindo...")
                    # saida = 0
                # elif saida5 == 1:
            while saida51 != 0:
                print("\n|-------------- JOGADOR 1 --------------|")
                print("|---------------------------------------|")
                print("|------- ALGORITMOS NÃO INFORMADOS -----|")
                print("|- 1 -> Algoritmo em Profundidade(DFS) -|")
                print("|---- 2 -> Algoritmo em Largura(BFS) ---|")
                print("|---------------------------------------|")
                print("|--------- ALGORITMOS INFORMADOS -------|")
                print("|---------- 3 -> Algoritmo A* ----------|")
                print("|-------- 4 -> Algoritmo Greedy --------|")
                print("|---------------------------------------|")
                print("|------------- 9 -> Voltar -------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saida51 = input("\nIntroduza a sua Opção -> ")
                try:
                    saida51 = int(saida51)
                    selectedAlg = int(saida51)
                except ValueError:
                    print("Introduza um número válido\n")
                    continue
                if saida51 == 9:
                    print("Menu Anterior...")
                    break
                elif saida51 == 0:
                    print("Saindo...")
                    saida = 0
                    break
                elif saida51 == 1:
                    caminho = problema.g.procura_DFS(posInit,posFinal)
                    path, custo = caminho  # type: ignore
                    print("\nCaminho encontrado: ", end="")
                    print(*path, sep=' -> ')
                    print(f"Custo Total: {str(custo)}\n")
                    print(problema.mostraCaminho(path))
                elif saida51 == 2:
                    caminho = []
                    caminho = problema.g.procura_BFS(posInit,posFinal)
                    path, custo = caminho  # type: ignore
                    print("\nCaminho encontrado: ", end="")
                    print(*path, sep=' -> ')
                    print(f"Custo Total: {str(custo)}\n")
                    print(problema.mostraCaminho(caminho[0]))
                elif saida51 == 3:
                    print("teste")
                elif saida51 == 4:
                    print("teste")

                while saida52 != 0:
                    print("\n|-------------- JOGADOR 2 --------------|")
                    print("|---------------------------------------|")
                    print("|------- ALGORITMOS NÃO INFORMADOS -----|")
                    print("|- 1 -> Algoritmo em Profundidade(DFS) -|")
                    print("|---- 2 -> Algoritmo em Largura(BFS) ---|")
                    print("|---------------------------------------|")
                    print("|--------- ALGORITMOS INFORMADOS -------|")
                    print("|---------- 3 -> Algoritmo A* ----------|")
                    print("|-------- 4 -> Algoritmo Greedy --------|")
                    print("|---------------------------------------|")
                    print("|------------- 9 -> Voltar -------------|")
                    print("|-------------- 0 -> Sair --------------|")
                    print("|---------------------------------------|")
                    saida52 = input("\nIntroduza a sua Opção -> ")
                    try:
                        saida52 = int(saida52)
                    except ValueError:
                        print("Introduza um número válido\n")
                        continue
                    if saida52 == selectedAlg:
                        print("Escolha um algoritmo diferente do anterior...\n")
                        continue
                    elif saida52 == 0:
                        print("Saindo...")
                        saida = 0
                        break
                    elif saida52 == 9:
                        print("Menu Anterior...")
                        break
                    elif saida52 == 1:
                        caminho2 = problema.g.procura_DFS(posInit,posFinal)
                        path2, custo2 = caminho2  # type: ignore
                        print("\nCaminho encontrado: ", end="")
                        print(*path2, sep=' -> ')
                        print(f"Custo Total: {str(custo2)}\n")
                        print(problema.mostraCaminho(path2))
                        x = True
                    elif saida52 == 2:
                        caminho2 = []
                        caminho2 = problema.g.procura_BFS(posInit,posFinal)
                        path2, custo2 = caminho2  # type: ignore
                        print("\nCaminho encontrado: ", end="")
                        print(*path2, sep=' -> ')
                        print(f"Custo Total: {str(custo2)}\n")
                        print(problema.mostraCaminho(caminho2[0]))
                        x = True
                    elif saida52 == 3:
                        print ("hello3")
                        x = True
                    elif saida52 == 4:
                        print ("hello4")
                        x = True
                    else:
                        print("Introduza um número válido\n")
                        continue
                    if saida52 == 0:
                        saida = 0
                        break
                    elif saida52 != selectedAlg and x:
                        print("A abrir a UI...")
                        #funcao(saida51, saida52, path, path2, default)
                        #codigo que chama a UI
                        app = Application3(default, path, path2)
                        app.mainloop()
                        l = input("Prima ENTER para continuar")
                if saida52 == 0:
                    saida = 0
                    break
                else:
                    saida = 0
                    print("Introduza um número válido\n")
                    continue

        else:
            print("Introduza um número válido\n")
            continue

if __name__ == "__main__":
    main()
