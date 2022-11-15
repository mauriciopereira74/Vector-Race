from Graph import Grafo
from readFile import readFile


class Race():

    # Exemplos
    # Posição -> "(10,20)"
    # Velocidade ->  "(1,2)"
    # AceleraçãoX -> 1 e AceleracaoY -> 0
    def __init__(self, start, velocidade):
        # Grafo
        self.g = Grafo(directed=True)  # Verificar directed
        # Posição Atual
        self.posicao = start
        # Velocidade
        self.velocidade = velocidade

    # Função que dado uma String retorna a Posição X da String
    def partePX(self):
        # Tirar primeiro e último elemento
        res = self.posicao.str[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[0]

    # Função que dado uma String retorna a Posição Y da String
    def partePY(self):
        # Tirar primeiro e último elemento
        res = self.posicao.str[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[1]

    # Função que dado uma String retorna a Velocidade X da String
    def parteVX(self):
        # Tirar primeiro e último elemento
        res = self.velocidade.str[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[0]

    # Função que dado uma String retorna a Velocidade Y da String
    def parteVY(self):
        # Tirar primeiro e último elemento
        res = self.velocidade.str[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[1]

    # Retorna o inteiro correspondente à posiçãoX seguinte
    def nextPX(self, aceleracaoX):
        res = int(self.partePX()) + int(self.parteVX()) + aceleracaoX
        # retorna em Inteiro
        return res

    # Retorna o inteiro correspondente à posiçãoY seguinte
    def nextPY(self, aceleracaoX):
        res = int(self.partePY()) + int(self.parteVY()) + aceleracaoX
        # retorna em Inteiro
        return res

    # Retorna o inteiro correspondente à velocidadeX seguinte
    def nextVX(self, aceleracaoX):
        res = int(self.parteVX()) + aceleracaoX
        # retorna em Inteiro
        return res

    # Retorna o inteiro correspondente à velocidadeY seguinte
    def nextVY(self, aceleracaoY):
        res = int(self.parteVY()) + aceleracaoY
        # retorna em Inteiro
        return res

    # Construir a String Posição Seguinte
    def posicaoNext(self, aceleracaoX, aceleracaoY):
        res = "(" + str(self.nextPX(aceleracaoX)) + "," + str(self.nextPY(aceleracaoY)) + ")"
        return res

    # Construir a String Velocidade Seguinte
    def velocidadeNext(self, aceleracaoX, aceleracaoY):
        res = "(" + str(self.nextVX(aceleracaoX)) + "," + str(self.nextVY(aceleracaoY)) + ")"
        return res

    # Dado uma Aceleração determina se pode avançar para a posição seguinte alterando os respetivos valores associados a cada letra e retorna a nova posicao
    def movSeguinte(self, aceleracaoX, aceleracaoY):
        file = readFile()
        circuito = file.ler()

        if circuito[self.nextPX(aceleracaoX)][self.nextPY(aceleracaoY)] == "-":
            self.posicao = self.posicaoNext(aceleracaoX, aceleracaoY)
            self.velocidade = self.velocidadeNext(aceleracaoX, aceleracaoY)
            return self.posicaoNext(aceleracaoX, aceleracaoY)
        elif circuito[self.nextPX(aceleracaoX)][self.nextPY(aceleracaoY)] == "X":
            self.velocidade = "(0,0)"
            # Não devia retornar nada porque ele mantém se na mesma posição
            # return [self.posicaoX, self.posicaoY]
        elif circuito[self.nextPX(aceleracaoX)][self.nextPY(aceleracaoY)] == "F":
            self.posicao = self.posicaoNext(aceleracaoX, aceleracaoY)
            # self.velocidadeX = self.nextVX(aceleracaoX)  ou 0
            # self.velocidadeY = self.nextVY(aceleracaoY)  ou 0
            return self.posicaoNext(aceleracaoX, aceleracaoY)
        else:
            print("Fora dos limites - ERROR")

    # Dadas as 9 possibilidades de acelerações cria a lista respetiva com as possições
    def listaMov(self):
        lista = []

        lista.append(self.movSeguinte(1, 1))
        lista.append(self.movSeguinte(1, 0))
        lista.append(self.movSeguinte(1, -1))
        lista.append(self.movSeguinte(0, 0))
        lista.append(self.movSeguinte(0, 1))
        lista.append(self.movSeguinte(0, -1))
        lista.append(self.movSeguinte(-1, 1))
        lista.append(self.movSeguinte(-1, 0))
        lista.append(self.movSeguinte(-1, -1))

        return lista

    # Criar um grafo partindo do estado inicial com todas as transições possiveis
    def cria_grafo(self):
        # Criar um grafo partindo do estado inicial com todas as transições possiveis
        # posicao = readFile()
        # posicaoX = readFile.PInicialX(self)
        # posicaoY = readFile.PInicialY(self)

        file = readFile()
        circuito = file.ler()

        a = -1
        b = -1
        print(a)
        print(b)
        for i in range(len(circuito)):
            for j in range(len(circuito[i])):
                if circuito[i][j] == "P":
                    return a == i, b == j
        print("tedtetdt")


        estados = []
        string = "(" + str(a) + "," + str(b) + ")"
        estados.append(string)

        visitados = []
        visitados.append(string)

        print(estados)
        print(string)
        while estados != []:
            estados = estados.pop()
            expansao = self.listaMov()  # Mudar expande
            for e in expansao:
                self.g.add_edge(estados, e, 1)
                if e not in visitados:
                    estados.append(e)
                    visitados.append(e)
        print(expansao)

        # return ?
