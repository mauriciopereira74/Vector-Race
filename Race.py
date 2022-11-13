from Node import Node
from Graph import Grafo
from queue import Queue
from readFile import readFile

class Race():

    def __init__(self, startX, startY, velocidadeX, velocidadeY):
        # Grafo
        self.g = Grafo(directed=True)  # Verificar directed
        # Posição Atual
        self.posicaoX = startX  # PInicialX
        self.posicaoY = startY  # PInicialY
        # Velocidade
        self.velocidadeX = velocidadeX  # 0
        self.velocidadeY = velocidadeY  # 0

    # Retorna o inteiro correspondente à posiçãoX seguinte
    def nextPX(self, aceleracaoX):
        return self.posicaoX + self.velocidadeX + aceleracaoX

    # Retorna o inteiro correspondente à posiçãoY seguinte
    def nextPY(self, aceleracaoY):
        return self.posicaoY + self.velocidadeY + aceleracaoY

    # Retorna o inteiro correspondente à velocidadeX seguinte
    def nextVX(self, aceleracaoX):
        return self.velocidadeX + aceleracaoX

    # Retorna o inteiro correspondente à velocidadeY seguinte
    def nextVY(self, aceleracaoY):
        return self.velocidadeY + aceleracaoY

    # Dado uma Aceleração determina se pode avançar para a posição seguinte alterando os respetivos valores associados a cada letra e retorna a nova posicao
    def movSeguinte(self, aceleracaoX, aceleracaoY):
        file = readFile()
        circuito = file.ler()

        if circuito[self.nextPX(aceleracaoX)][self.nextPX(aceleracaoY)] == "-":
            self.posicaoX = self.nextPX(aceleracaoX)
            self.posicaoY = self.nextPX(aceleracaoY)
            self.velocidadeX = self.nextVX(aceleracaoX)
            self.velocidadeY = self.nextVY(aceleracaoY)
            return (self.posicaoX, self.posicaoY)
        elif circuito[self.nextPX(aceleracaoX)][self.nextPX(aceleracaoY)] == "X":
            self.velocidadeX = 0
            self.velocidadeY = 0
            return (self.posicaoX, self.posicaoY)
        elif circuito[self.nextPX(aceleracaoX)][self.nextPX(aceleracaoY)] == "F":
            self.posicaoX = self.nextPX(aceleracaoX)
            self.posicaoY = self.nextPX(aceleracaoY)
            # self.velocidadeX = self.nextVX(aceleracaoX)  ou 0
            # self.velocidadeY = self.nextVY(aceleracaoY)  ou 0
            return (self.posicaoX, self.posicaoY)
        else:
            print("Fora dos limites - ERROR")

    # Dadas as 9 possibilidades de acelerações cria a lista respetiva com as possições
    def listaMov(self):
        lista = []
        return lista + \
               [self.movSeguinte(1, 1)] +  \
               [self.movSeguinte(1, 0)] +  \
               [self.movSeguinte(1, -1)] + \
               [self.movSeguinte(0, 0)] +  \
               [self.movSeguinte(0, 1)] +  \
               [self.movSeguinte(0, -1)] + \
               [self.movSeguinte(-1, 1)] + \
               [self.movSeguinte(-1, 0)] + \
               [self.movSeguinte(-1, -1)]

    def cria_grafo(self):
        # Criar um grafo partindo do estado inicial
        # com todas as transições possiveis
        estados = []
        estados.append((self.posicaoX, self.posicaoY))

        visitados = []
        visitados.append((self.posicaoX, self.posicaoY))

        while estados != []:
            estados = estados.pop()
            expansao = self.listaMov()
            for e in expansao:
                self.g.add_edge(estados, e, 1)  # Em principio posso retirar as heuristicas
                if e not in visitados:
                    estados.append(e)
                    visitados.append(e)

        # return ?
