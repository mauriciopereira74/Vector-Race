from Race import Race
from readFile import readFile


def main():
    # file = readFile()
    # circuito = file.ler()
    # a = -1
    # b = -1
    # for i in range(len(circuito)):
    #     for j in range(len(circuito[i])):
    #         if circuito[i][j] == "P":
    #             return a == i, b == j
    #
    # string = "(" + str(a) + "," + str(b) + ")"
    problema = Race("(1,3)", "(0,0)")
    problema.cria_grafo()
    saida = -1

    while saida != 0:
        print("1-Imprimir grafo")
        print("2-Desenhar Grafo")
        print("3-Imprimir nodos de Grafo")
        print("4-Imprimir arestas de Grafo")
        # print("5-DFS")
        # print("6-BFS")
        # print("7 -Outra solução ")
        print("0-Sair")

        saida = int(input("Introduza a sua opção-> "))
        if saida == 0:
            print("Saindo.......")
        elif saida == 1:
            print(problema.g.m_graph)
            l = input("prima enter para continuar")
        elif saida == 2:
            problema.g.desenha()
        elif saida == 3:
            print(problema.g.m_graph.keys())
            l = input("prima enter para continuar")
        elif saida == 4:
            print(problema.g.imprime_aresta())
            l = input("prima enter para continuar")
        # elif saida == 5:
        #     inicio=input("Nodo inicial->")
        #     fim = input("Nodo final->")
        #     caminho=problema.solucaoDFS( inicio, fim)
        #     print(caminho)
        #     if caminho != None:
        #        a = caminho[0]
        #        lista=problema.imprimeA(a)
        #        print(lista)
        #     l = input("prima enter para continuar")
        # elif saida == 6:
        #     inicio = input("Nodo inicial->")
        #     fim = input("Nodo final->")
        #     caminho=problema.solucaoBFS(inicio,fim)
        #     print(caminho)
        #     if caminho != None:
        #         a = caminho[0]
        #         lista = problema.imprimeA(a)
        #         print(lista)
        #     l = input("prima enter para continuar")
        # elif saida == 7:
        #     inicio = input("Nodo inicial->")
        #     fim = input("Nodo final->")
        #     caminho = problema.encontraDFS(inicio, fim)
        #     print(caminho)
        #     if caminho != None:
        #         a = caminho[0]
        #         lista = problema.imprimeA(a)
        #         print(lista)
        #     l = input("prima enter para continuar")
        else:
            print("you didn't add anything")
            l = input("prima enter para continuar")
    print("Martim")


if __name__ == "__main__":
    main()
