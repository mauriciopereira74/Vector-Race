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
import random

def main():
    global default 
    default = "circuito0.txt"
    readClass = readFile("")
    posInit = readClass.PInicialXY()
    posInit2Aux = readClass.PInicialXY2()
    if len(posInit2Aux) == 1:
        posInit2 = None
    else: posInit2 = posInit2Aux[1]
    posFinal = readClass.PFinalXY()
    posCheckpoint = readClass.PCheckXY()
    problema = Race("", posInit, posFinal, posCheckpoint, "(0,0)", posInit2Aux[1])
    
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
    saidaComp = -1
    saidaMapas = -1
    colisao = -1
    colisaoInt = -1
    global default2
    default2 = -1

    while saida != 0:
        if default2!=-1:
            circuito_path = default
            readClass = readFile(circuito_path)
            posInit = readClass.PInicialXY()
            posFinal = readClass.PFinalXY()
            posCheckpoint = readClass.PCheckXY()
            problema = Race(circuito_path, posInit, posFinal, posCheckpoint, "(0,0)", None)
        print("\n|----------------- MENU ----------------|")
        print("|---------------------------------------|")
        print("|------- 99 -> Escolher Circuito -------|")
        if len(default) == 13:
            print(f"|--------- Atual: {default} --------|")
        elif len(default) == 14:
            print(f"|-------- Atual: {default} --------|")
        elif len(default) == 15:
            print(f"|------- Atual: {default} --------|")
        elif len(default) == 16:
            print(f"|------- Atual: {default} -------|")
        elif len(default) == 17:
            print(f"|------ Atual: {default} -------|")
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
                onlyfiles.sort()
                print("\n|--------------- CIRCUITOS -------------|")
                print("|---------------------------------------|")
                for i, circ in enumerate(onlyfiles, start = 1):
                    res = f" {i} -> {circ} "
                    if len(res) == 18:
                        print("|----------" + res + "----------|")
                    elif len(res) == 19:
                        print("|----------" + res + "---------|")
                    elif len(res) == 20:
                        print("|----------" + res + "---------|")                    
                    elif len(res) == 21:
                        print("|----------" + res + "--------|")
                    elif len(res) == 22:
                        print("|----------" + res + "-------|")
                    elif len(res) == 23:
                        print("|----------" + res + "------|")
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
                if saidaCir2 == 0:
                    print("Saindo...")
                    saida = 0
                    break
                elif saidaCir2 in range(1, i+1):   # type: ignore
                    circuito_path = onlyfiles[(saidaCir2-1)]
                    readClass = readFile(circuito_path)
                    posInit = readClass.PInicialXY()
                    posFinal = readClass.PFinalXY()
                    posCheckpoint = readClass.PCheckXY()
                    problema = Race(circuito_path, posInit, posFinal, posCheckpoint, "(0,0)", None)
                    default = circuito_path
                    break;
                else:
                    print("Introduza um número válido\n")
                    continue

        elif saida == 0:
            print("Saindo...")
            break
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
                if len(default) == 15:
                    print(f"|---- 1 -> Imprimir {default} ----|")
                elif len(default) == 13:
                    print(f"|------ 1 -> Imprimir {default} ----|")
                print("|---------------------------------------|")
                if len(default) == 15:
                    print(f"|- 2 -> VectorRace do {default} --|")
                elif len(default) == 13:
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
                    break
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
                print("|------ 31 -> A* (com Velocidade) ------|")
                print("|---------- 32 -> Heurística A* --------|")
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
                    if posCheckpoint != None:
                        print("Não implementado - Escolha um mapa sem checkpoints")
                        l = input("Prima ENTER para continuar")
                    else:
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
                        l = input("Prima ENTER para continuar")
                    else:
                        caminho1 = []
                        caminho2 = []
                        caminho1 = problema.g.procura_BFS(posInit, posCheckpoint)
                        path1, custo1 = caminho1  # type: ignore
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
                    problema.g.heuristica_aStar(posFinal)
                    if posCheckpoint == None:
                        caminho = []
                        caminho = problema.g.procura_aStar(posInit,posFinal)
                        path, custo = caminho  # type: ignore
                        print("\nCaminho encontrado: ", end="")
                        print(*path, sep=' -> ')
                        print(f"Custo Total: {str(custo)}\n")
                        print(problema.mostraCaminho(caminho[0]))
                        l = input("Prima ENTER para continuar")
                    else:
                        caminho1 = []
                        caminho2 = []
                        caminho1 = problema.g.procura_aStar(posInit, posCheckpoint)
                        path1, custo1 = caminho1  # type: ignore
                        caminho2 = problema.g.procura_aStar(posCheckpoint, posFinal)
                        path2, custo2 = caminho2  # type: ignore
                        path2.pop(0)
                        pathCompleto = path1 + path2
                        custoTotal = custo1 + custo2
                        print("\nCaminho encontrado: ", end="")
                        print(*pathCompleto, sep=' -> ')
                        print(f"Custo Total: {str(custoTotal)}\n")
                        print(problema.mostraCaminho(pathCompleto))
                        l = input("Prima ENTER para continuar")
                elif saida4 == 32:
                    problema.g.heuristica_aStar(posFinal)
                    print(problema.g.m_h)
                elif saida4 == 31:
                    if posCheckpoint != None:
                        print("Não implementado - Escolha um mapa sem checkpoints")
                        l = input("Prima ENTER para continuar")
                    else:
                        problema.g.heuristica_aStar(posFinal)
                        caminho = problema.g.procura_aStar_wVelocity(posInit,posFinal)
                        path, custo = caminho  # type: ignore
                        print("\nCaminho encontrado: ", end="")
                        print(*path, sep=' -> ')
                        print(f"Custo Total: {str(custo)}\n")
                        print(problema.mostraCaminho(path))
                        l = input("Prima ENTER para continuar")
                elif saida4 == 4:
                    if posCheckpoint != None:
                        print("Não implementado - Escolha um mapa sem checkpoints")
                        l = input("Prima ENTER para continuar")
                    else:
                        problema.g.heuristica_greedy(posFinal)
                        caminho = problema.g.greedy(posInit,posFinal)
                        path, custo = caminho  # type: ignore
                        print("\nCaminho encontrado: ", end="")
                        print(*path, sep=' -> ')
                        print(f"Custo Total: {str(custo)}\n")
                        print(problema.mostraCaminho(path))
                        l = input("Prima ENTER para continuar")
                elif saida4 == 41:
                    problema.g.heuristica_greedy(posFinal)
                    print(problema.g.m_h)
                else:
                    print("Introduza um número válido\n")
                    continue
        elif saida == 5:
            while saidaMapas != 0:
                onlyfiles2 = [f for f in listdir("Circuitos/Multiplayer/") if isfile(join("Circuitos/Multiplayer/", f))]
                onlyfiles2.sort()
                print("\n|-------- CIRCUITOS MULTIPLAYER --------|")
                print("|---------------------------------------|")
                for i, circ in enumerate(onlyfiles2, start = 1):
                    res = f" {i} -> {circ} "
                    if len(res) == 18:
                        print("|----------" + res + "-----------|")
                    elif len(res) == 19:
                        print("|----------" + res + "----------|")
                    elif len(res) == 20:
                        print("|----------" + res + "---------|")
                    elif len(res) == 21:
                        print("|----------" + res + "--------|")
                    elif len(res) == 22:
                        print("|----------" + res + "-------|")
                    print("|---------------------------------------|")
                print("|---------------------------------------|")
                print("|------------- 9 -> Voltar -------------|")
                print("|-------------- 0 -> Sair --------------|")
                print("|---------------------------------------|")
                saidaMapas = input("Introduza a sua opção-> ")
                try:
                   saidaMapas = int(saidaMapas)
                except ValueError:
                    print("Introduza um número válido\n")
                    continue
                if saidaMapas == 0:
                    print("Saindo...")
                    break
                elif saidaMapas == 9:
                    print("Menu Anterior...")
                    break
                elif saidaMapas in range(1, i+1):   # type: ignore
                    x = range(1,i)
                    circuito_path2 = f"Multiplayer/{onlyfiles2[(saidaMapas-1)]}"
                    readClass = readFile(circuito_path2)
                    posInit2 = readClass.PInicialXY2()
                    posFinal = readClass.PFinalXY()
                    posCheckpoint = readClass.PCheckXY()
                    problema = Race(circuito_path2, posInit2[0], posFinal, posCheckpoint, "(0,0)", posInit2[1])
                    default2 = onlyfiles2[(saidaMapas-1)]
                else:
                    print("Introduza um número válido\n")
                    continue
                while colisaoInt != 0:
                    print("\n|--------------- COLISÃO ---------------|")
                    print("|---- Carro que se avança primeiro: ----|")
                    print("|---------------------------------------|")
                    print("|--------- 1 - Forma Aleatória ---------|")
                    print("|---------------------------------------|")
                    print("|----------- 2 -> Menor Custo ----------|")
                    print("|---------------------------------------|")
                    print("|------------- 9 -> Voltar -------------|")
                    print("|-------------- 0 -> Sair --------------|")
                    print("|---------------------------------------|")
                    colisaoInt = input("\nIntroduza a sua Opção -> ")
                    try:
                        colisaoInt = int(colisaoInt)
                        # selectedAlg = int(saida51)
                    except ValueError:
                        print("Introduza um número válido\n")
                        continue
                    if colisaoInt == 9:
                        print("Menu Anterior...")
                        break
                    elif colisaoInt == 0:
                        print("Saindo...")
                        saidaMapas = 0
                        saida = 0
                        break
                    elif colisaoInt == 1:
                        colisao = 1
                    elif colisaoInt == 2:
                        colisao = 2
                    else:
                        print("Introduza um número válido\n")
                        continue
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
                            # selectedAlg = int(saida51)
                        except ValueError:
                            print("Introduza um número válido\n")
                            continue
                        if saida51 == 9:
                            print("Menu Anterior...")
                            break
                        elif saida51 == 0:
                            print("Saindo...")
                            colisaoInt = 0
                            saidaMapas = 0
                            saida = 0
                            break
                        elif saida51 == 1:
                            caminho = problema.g.procura_DFS(posInit2[0],posFinal)
                            path, custo = caminho  # type: ignore
                            print("\nCaminho encontrado: ", end="")
                            print(*path, sep=' -> ')
                            print(f"Custo Total: {str(custo)}\n")
                            print(problema.mostraCaminho(path))
                        elif saida51 == 2:
                            caminho = []
                            caminho = problema.g.procura_BFS(posInit2[0],posFinal)
                            path, custo = caminho  # type: ignore
                            print("\nCaminho encontrado: ", end="")
                            print(*path, sep=' -> ')
                            print(f"Custo Total: {str(custo)}\n")
                            print(problema.mostraCaminho(caminho[0]))
                        elif saida51 == 3:
                            problema.g.heuristica_aStar(posFinal)
                            caminho = problema.g.procura_aStar(posInit2[0],posFinal)
                            path, custo = caminho  # type: ignore
                            print("\nCaminho encontrado: ", end="")
                            print(*path, sep=' -> ')
                            print(f"Custo Total: {str(custo)}\n")
                            print(problema.mostraCaminho(path))
                        elif saida51 == 4:
                            problema.g.heuristica_greedy(posFinal)
                            caminho = problema.g.greedy(posInit2[0],posFinal)
                            path, custo = caminho  # type: ignore
                            print("\nCaminho encontrado: ", end="")
                            print(*path, sep=' -> ')
                            print(f"Custo Total: {str(custo)}\n")
                            print(problema.mostraCaminho(path))
                        else:
                            print("Introduza um número válido\n")
                            continue

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
                            if saida52 == 0:
                                print("Saindo...")
                                saida51 = 0
                                colisaoInt = 0
                                saidaMapas = 0
                                saida = 0
                            elif saida52 == 9:
                                print("Menu Anterior...")
                                break
                            elif saida52 == 1:
                                caminho2 = problema.g.procura_DFS(posInit2[1],posFinal)
                                path2, custo2 = caminho2  # type: ignore
                                print("\nCaminho encontrado: ", end="")
                                print(*path2, sep=' -> ')
                                print(f"Custo Total: {str(custo2)}\n")
                                print(problema.mostraCaminho(path2))
                                x = True
                            elif saida52 == 2:
                                caminho2 = []
                                caminho2 = problema.g.procura_BFS(posInit2[1],posFinal)
                                path2, custo2 = caminho2  # type: ignore
                                print("\nCaminho encontrado: ", end="")
                                print(*path2, sep=' -> ')
                                print(f"Custo Total: {str(custo2)}\n")
                                print(problema.mostraCaminho(caminho2[0]))
                                x = True
                            elif saida52 == 3:
                                problema.g.heuristica_aStar(posFinal)
                                caminho2 = problema.g.procura_aStar(posInit2[1],posFinal)
                                path2, custo2 = caminho2  # type: ignore
                                print("\nCaminho encontrado: ", end="")
                                print(*path2, sep=' -> ')
                                print(f"Custo Total: {str(custo2)}\n")
                                print(problema.mostraCaminho(path2))
                                x = True
                            elif saida52 == 4:
                                problema.g.heuristica_greedy(posFinal)
                                caminho2 = problema.g.greedy(posInit2[1],posFinal)
                                path2, custo2 = caminho2  # type: ignore
                                print("\nCaminho encontrado: ", end="")
                                print(*path2, sep=' -> ')
                                print(f"Custo Total: {str(custo2)}\n")
                                print(problema.mostraCaminho(path2))
                                x = True
                            else:
                                print("Introduza um número válido\n")
                                continue

                            if x:
                                collisions = []
                                while problema.check_collision(path, path2, posFinal)!=-1:
                                    collisionidx = problema.check_collision(path, path2, posFinal)
                                    collisions.append(path[collisionidx])
                                    if saida51 == 1:
                                        caminho = problema.g.procura_DFS(path[collisionidx-1],posFinal)
                                        pathNovo, custoNovo = caminho  # type: ignore
                                    elif saida51 == 2:
                                        caminho = []
                                        caminho = problema.g.procura_BFS(path[collisionidx-1],posFinal)
                                        pathNovo, custoNovo = caminho  # type: ignore
                                    elif saida51 == 3:
                                        problema.g.heuristica_aStar(posFinal)
                                        # problema.g.shortenClosedListToCollision_a(path[collisionidx])
                                        caminho = problema.g.procura_aStar(path[collisionidx-1],posFinal)
                                        pathNovo, custoNovo = caminho  # type: ignore
                                    elif saida51 == 4:
                                        problema.g.heuristica_greedy(posFinal)
                                        # problema.g.shortenClosedListToCollision_greedy(path[collisionidx])
                                        caminho = problema.g.greedy(path[collisionidx-1],posFinal)
                                        pathNovo, custoNovo = caminho  # type: ignore


                                    if saida52 == 1:
                                        caminho2 = problema.g.procura_DFS(path2[collisionidx-1],posFinal)
                                        path2Novo, custo2Novo = caminho2  # type: ignore
                                    elif saida52 == 2:
                                        caminho2 = []
                                        caminho2 = problema.g.procura_BFS(path2[collisionidx-1],posFinal)
                                        path2Novo, custo2Novo = caminho2  # type: ignore
                                    elif saida52 == 3:
                                        problema.g.heuristica_aStar(posFinal)
                                        # problema.g.shortenClosedListToCollision_a(path[collisionidx])
                                        caminho2 = problema.g.procura_aStar(path2[collisionidx-1],posFinal)
                                        path2Novo, custo2Novo = caminho2  # type: ignore
                                    elif saida52 == 4:
                                        problema.g.heuristica_greedy(posFinal)
                                        # problema.g.shortenClosedListToCollision_greedy(path[collisionidx])
                                        caminho2 = problema.g.greedy(path2[collisionidx-1],posFinal)
                                        path2Novo, custo2Novo = caminho2  # type: ignore


                                    #  Forma aleatória
                                    if colisao == 1:
                                        randomDecr = random.randint(0, 1)

                                        if randomDecr == 0:
                                             randomDecr2 = 1
                                        else: randomDecr2 = 0
                                    # menor custo até ao momento
                                    elif colisao == 2:
                                        if custo > custo2:
                                            randomDecr2 = 1
                                            randomDecr = 0
                                        else:
                                            randomDecr = 1
                                            randomDecr2 = 0
                                    # menor heuristica
                                    # elif colisao == 3:
                                    #     if custo > custo2:
                                    #         randomDecr2 = 1
                                    #         randomDecr = 0
                                    #     else:
                                    #         randomDecr = 1
                                    #         randomDecr2 = 0


                                    # decide um número entre 0 e 1 aleatoriamente
                                    # de forma a que ao encortar o path final até ao index da peca de colisao,
                                    #  a peca colisao seja adicionada duas vezes ao path
                                    # de forma a que um carro espereo pelo outro
                                    path = path[:(collisionidx - randomDecr)]
                                    path += pathNovo
                                    custo += custoNovo

                                    path2 = path2[:(collisionidx - randomDecr2)]
                                    path2 += path2Novo
                                    custo2 += custo2Novo

                                    print("\nCaminho encontrado: ", end="")
                                    print(*path, sep=' -> ')
                                    print(f"Custo Total: {str(custo)}\n")
                                    print(problema.mostraCaminho(path))

                                    print("\nCaminho encontrado: ", end="")
                                    print(*path2, sep=' -> ')
                                    print(f"Custo Total: {str(custo2)}\n")
                                    print(problema.mostraCaminho(path2))

                                print(collisions)
                                print("A abrir a UI...")
                                app = Application3(circuito_path2, path, path2, saida51, saida52, custo, custo2, collisions)
                                app.mainloop()
                                l = input("Prima ENTER para continuar")
                #         if saida52 == 0:
                #             saida = 0
                #             break
                #         else:
                #             print("Introduza um número válido\n")
                #             continue
                #     if saida51 == 0:
                #         saida = 0
                #         break
                #     else:
                #         print("Introduza um número válido\n")
                #         continue
                # if colisaoInt == 0:
                #     saida = 0
                #     break
                # else:
                #     print("Introduza um número válido\n")
                #     continue

if __name__ == "__main__":
    main()
