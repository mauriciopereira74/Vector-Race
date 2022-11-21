from Race import Race
from readFile import readFile

def main():

    readClass = readFile()
    posInit = readClass.PInicialXY()
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
                    print("Martim")
                    l = input("Prima ENTER para continuar")
                if saida2 == 3:
                    print("Martim")
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
            inicio = input("Nodo inicial->")
            # fim = input("Nodo final->")
            # caminho = problema.solucaoDFS(inicio, fim)
            # print(caminho)
            # if caminho != None:
            #     a = caminho[0]
            #     lista = problema.imprimeA(a)
            #     print(lista)
            l = input("prima enter para continuar")
        else:
            print("Número Inválido")
            l = input("Prima ENTER para continuar")

if __name__ == "__main__":
    main()
