from Graph import Grafo
from readFile import readFile


class Race():

    global file
    global circuito
    global lines
    global cols
    file = readFile()
    circuito = file.ler()
    lines = len(circuito)
    cols = len(circuito[1])
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
        res = self.posicao[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[0]

    # Função que dado uma String retorna a Posição Y da String
    def partePY(self):
        # Tirar primeiro e último elemento
        res = self.posicao[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[1]

    # Função que dado uma String retorna a Velocidade X da String
    def parteVX(self):
        # Tirar primeiro e último elemento
        res = self.velocidade[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[0]

    # Função que dado uma String retorna a Velocidade Y da String
    def parteVY(self):
        # Tirar primeiro e último elemento
        res = self.velocidade[1:-1]

        # Partir a string na virgula
        res = res.split(',')

        # Retorna o primeiro elemento em String
        return res[1]

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

    # Retorna o inteiro correspondente à posiçãoX seguinte
    def nextPX(self, aceleracaoX):
        res = int(self.partePX()) + self.nextVX(aceleracaoX)
        if res < 0: res = 0
        elif res >=  lines: res = (lines-1)
        # retorna em Inteiro
        return res

    # Retorna o inteiro correspondente à posiçãoY seguinte
    def nextPY(self, aceleracaoY):
        res = int(self.partePY()) + self.nextVY(aceleracaoY)
        if res < 0: res = 0
        elif res >=  cols: res = (cols-1)
        # retorna em Inteiro
        return res

    # Construir a String Posição Seguinte
    def posicaoNext(self, vx, vy, aceleracaoX, aceleracaoY):
        res = "(" + str(self.nextPX2(vx, aceleracaoX)) + "," + str(self.nextPY2(vy, aceleracaoY)) + ")"
        return res

    # Construir a String Velocidade Seguinte
    def velocidadeNext(self, vx, vy, aceleracaoX, aceleracaoY):
        res = "(" + str(self.nextVX2(vx, aceleracaoX)) + "," + str(self.nextVY2(vy, aceleracaoY)) + ")"
        return res

    # Dado uma Aceleração determina se pode avançar para a posição seguinte alterando os respetivos valores associados a cada letra e retorna a nova posicao
    # def movSeguinte(self, aceleracaoX, aceleracaoY):
        # file = readFile()
        # circuito = file.ler()
# 
        # if circuito[self.nextPX(aceleracaoX)][self.nextPY(aceleracaoY)] == "-":
            # self.posicao = self.posicaoNext(aceleracaoX, aceleracaoY)
            # self.velocidade = self.velocidadeNext(aceleracaoX, aceleracaoY)
            # return self.posicaoNext(aceleracaoX, aceleracaoY)
        # elif circuito[self.nextPX(aceleracaoX)][self.nextPY(aceleracaoY)] == "X":
            # self.velocidade = "(0,0)"
            # Não devia retornar nada porque ele mantém se na mesma posição
            # return [self.posicaoX, self.posicaoY]
        # elif circuito[self.nextPX2(aceleracaoX)][self.nextPY2(aceleracaoY)] == "F":
            # self.velocidade = self.velocidadeNext(aceleracaoX, aceleracaoY)
            # self.posicao = self.posicaoNext(aceleracaoX, aceleracaoY)
            # self.velocidadeX = self.nextVX(aceleracaoX)  ou 0
            # self.velocidadeY = self.nextVY(aceleracaoY)  ou 0
            # return self.posicaoNext(aceleracaoX, aceleracaoY)


    
    def nextVX2(self, velocidadeX, aceleracaoX):
        res = velocidadeX + aceleracaoX
        # retorna em Inteiro
        return res

    # Retorna o inteiro correspondente à velocidadeY seguinte
    def nextVY2(self, velocidadeY, aceleracaoY):
        res = velocidadeY + aceleracaoY
        # retorna em Inteiro
        return res


    def nextPX2(self, velocidadeX, aceleracaoX):
        res = int(self.partePX()) + self.nextVX2(velocidadeX, aceleracaoX)
        if res < 0: res = 0
        elif res >=  lines: res = (lines-1)
        # retorna em Inteiro
        return res

    # Retorna o inteiro correspondente à posiçãoY seguinte
    def nextPY2(self, velocidadeY, aceleracaoY):
        res = int(self.partePY()) + self.nextVY2(velocidadeY, aceleracaoY)
        if res < 0: res = 0
        elif res >=  cols: res = (cols-1)
        # retorna em Inteiro
        return res

    def movSeguinte2(self,vx_atual , vy_atual, aceleracaoX, aceleracaoY):
        file = readFile()
        circuito = file.ler()

        if circuito[self.nextPX2(vx_atual, aceleracaoX)][self.nextPY2(vy_atual, aceleracaoY)] == "-":
            self.posicao = self.posicaoNext(vx_atual, vy_atual, aceleracaoX, aceleracaoY)
            self.velocidade = self.velocidadeNext(vx_atual, vy_atual, aceleracaoX, aceleracaoY)
            return self.posicaoNext(vx_atual, vy_atual, aceleracaoX, aceleracaoY)
        elif circuito[self.nextPX2(vx_atual, aceleracaoX)][self.nextPY2(vy_atual, aceleracaoY)] == "X":
            self.velocidade = "(0,0)"
            # Não devia retornar nada porque ele mantém se na mesma posição
            # return [self.posicaoX, self.posicaoY]
        elif circuito[self.nextPX2(vx_atual, aceleracaoX)][self.nextPY2(vy_atual, aceleracaoY)] == "F":
            self.velocidade = self.velocidadeNext(vx_atual, vy_atual, aceleracaoX, aceleracaoY)
            self.posicao = self.posicaoNext(vx_atual, vy_atual, aceleracaoX, aceleracaoY)
            # self.velocidadeX = self.nextVX(aceleracaoX)  ou 0
            # self.velocidadeY = self.nextVY(aceleracaoY)  ou 0
            return self.posicaoNext(vx_atual, vy_atual, aceleracaoX, aceleracaoY)

    # Dadas as 9 possibilidades de acelerações cria a lista respetiva com as possições
    def listaMov(self):
        lista = []
        for x in range(int(self.parteVX())):
            print(lista)
            for y in range(int(self.parteVY())):
                lista.append(self.movSeguinte2(x, y, 1, 1))
                lista.append(self.movSeguinte2(x, y, 1, 1))
                lista.append(self.movSeguinte2(x, y, 1, 0))
                lista.append(self.movSeguinte2(x, y, 1, -1))
                lista.append(self.movSeguinte2(x, y, 0, 0))
                lista.append(self.movSeguinte2(x, y, 0, 1))
                lista.append(self.movSeguinte2(x, y, 0, -1))
                lista.append(self.movSeguinte2(x, y, -1, 1))
                lista.append(self.movSeguinte2(x, y, -1, 0))
                lista.append(self.movSeguinte2(x, y, -1, -1))                

        return (list(set(lista))) #remove sups !TODO

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
        for i in range(len(circuito)):
            for j in range(len(circuito[i])):
                if circuito[i][j] == "P":
                    a = i
                    b = j


        estados = []
        string = "(" + str(a) + "," + str(b) + ")"
        estados.append(string)

        visitados = []
        visitados.append(string)

        while estados != [] :
            #estado = estados[0]
            estado = estados.pop()
            expansao = self.listaMov()  # Mudar expande
            for e in expansao:
                if e != None:
                    self.g.add_edge(estado, e)
                    if e not in visitados:
                        estados.append(e)
                        visitados.append(e)

        # return ?
