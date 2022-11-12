from nodo import Node
from Graph import Grafo
from queue import Queue
from readFile import readFile

class Race():

    def __init__(self):
        self.g = Grafo(directed=True)
        self.custo = 0
        self.posicao = "(0,0)"
        self.velocidade = "(0,0)"
        self.aceleracao = "(0,0)"

    # Partindo do estado inicial, utilizando as ações possíveis como transições
    # construir o grafo
    def cria_grafo(self):
        # Criar um grafo partindo do estado inicial com todas as transições possiveis
        estados = []
        estados.append(self.posicao)

        visitados = []
        visitados.append(self.posicao)

        while estados != []:
            estados = estados.pop()
            expansao = self.avancar()
            for e in expansao:
                self.g.add_edge(estados, e, 1)
                if e not in visitados:
                    estados.append(e)
                    visitados.append(e)

    # def avancarGeral(self, aceleracao):
    #     if (int(aceleracao[1]) == 1  and int(aceleracao[3]) == 1):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == 1  and int(aceleracao[3]) == 0):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == 1  and int(aceleracao[3]) == -1):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == 0  and int(aceleracao[3]) == 1):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == 0  and int(aceleracao[3]) == 0):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == 0  and int(aceleracao[3]) == -1):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == -1 and int(aceleracao[3]) == 1):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == -1 and int(aceleracao[3]) == 0):
    #         avancar(aceleracao)
    #     if (int(aceleracao[1]) == -1 and int(aceleracao[3]) == -1):

    def avancar(self, aceleracao):
        lista = []
        posicaoSeguinte = "(" + self.posicaoSeguinteL() + "," + self.posicaoSeguinteC() + ")"
        velocidadeSeguinte = "(" + self.velocidadeSeguinteL() + "," + self.velocidadeSeguinteC() + ")"
        if readFile.circuito[int(posicaoSeguinte[1]), int(posicaoSeguinte[3])] == "-":
            self.custo += 1
            self.posicao = posicaoSeguinte
            self.velocidade = velocidadeSeguinte
            lista.append(posicaoSeguinte)
            # self.aceleracao # Acho que nao vou ter que mudar a aceleracao uma vez que vou ter que verificar todos os valores possiveis de aceleraçao
        if readFile.circuito[int(posicaoSeguinte[1]), int(posicaoSeguinte[3])] == "X":
            self.custo += 25
            # self.posicao => IGUAL
            self.velocidade = 0
            # self.aceleracao
            lista.append(posicaoSeguinte)
        if readFile.circuito[int(posicaoSeguinte[1]), int(posicaoSeguinte[3])] == "F":
            self.custo += 1
            self.posicao = posicaoSeguinte
            # self.velocidade =
            # self.aceleracao =
            lista.append(posicaoSeguinte)
        return lista

    # Devolve a velocidade da linha seguinte
    def velocidadeSeguinteL(self, aceleracao):
        velocidadeSeguinteL = int(self.velocidade[1]) + int(aceleracao[1])
        res = "(" + str(velocidadeSeguinteL) + "," + self.velocidade[3] + ")"
        return res

    # Devolve a velocidade da coluna seguinte
    def velocidadeSeguinteC(self, aceleracao):
        velocidadeSeguinteC = int(self.velocidade[3]) + int(aceleracao[3])
        res = "(" + self.velocidade[1] + "," + str(velocidadeSeguinteC) + ")"
        return res

    # Devolve a posicao da linha seguinte
    def posicaoSeguinteL(self):
        posicaoSeguinteL = int(self.posicao[1]) + int(self.velocidade[1]) + int(self.aceleracao[1])
        res = "(" + str(posicaoSeguinteL) + "," + self.posicao[3] + ")"
        return res

    # Devolve a posicao da coluna seguinte
    def posicaoSeguinteC(self):
        posicaoSeguinteC = int(self.posicao[3]) + int(self.velocidade[3]) + int(self.aceleracao[3])
        res = "(" + self.posicao[1] + "," + str(posicaoSeguinteC) + ")"
        return res

    # ########################################################
    # # Imprimir sequência de ações para um caminho encontrado
    # ########################################################
    # # def imprimeA(self,caminho):
    #     # To do...
