from Graph import Grafo
from readFile import readFile


class Race():
    global file
    global circuito
    global lines
    global cols
    file = readFile()
    circuito = file.ler()
    lines = len(circuito[1])
    cols = len(circuito)

    #               Y  X
    # print(circuito[1][0])

    def __init__(self, start, velocidade):
        # Grafo
        self.g = Grafo(directed=True)  # Verificar directed
        # Posição Atual
        self.posicao = start
        # Velocidade
        self.velocidade = velocidade

    # PosiçãoX -> String
    def posicaoX(self):
        res = self.posicao[1:-1]
        res = res.split(',')
        return res[0]

    # PosiçãoY -> String
    def posicaoY(self):
        res = self.posicao[1:-1]
        res = res.split(',')
        return res[1]

    ################################################################

    # VelocidadeX -> String
    def velocidadeX(self):
        res = self.velocidade[1:-1]
        res = res.split(',')
        return res[0]

    # VelocidadeY -> String
    def velocidadeY(self):
        res = self.velocidade[1:-1]
        res = res.split(',')
        return res[1]

    # Próxima PosiçãoX -> Inteiro
    def nextPosicaoX(self, aceleracaoX):
        res = int(self.posicaoX()) + int(self.velocidadeX()) + aceleracaoX
        if res < 0:
            res = 0
        elif res >= lines:
            res = (lines - 1)
        return res

    # Próxima PosiçãoY -> Inteiro
    def nextPosicaoY(self, aceleracaoX):
        res = int(self.posicaoY()) + int(self.velocidadeY()) + aceleracaoX
        if res < 0:
            res = 0
        elif res >= cols:
            res = (cols - 1)
        return res

    # Próxima VelocidadeX -> Inteiro
    def nextVelocidadeX(self, aceleracaoX):
        res = int(self.velocidadeX()) + aceleracaoX
        return res

    # Próxima VelocidadeY -> Inteiro
    def nextVelocidadeY(self, aceleracaoY):
        res = int(self.velocidadeY()) + aceleracaoY
        return res

    # Posicao Seguinte -> String
    def posicaoNext(self, aceleracaoX, aceleracaoY):
        res = "(" + (str(self.nextPosicaoX(aceleracaoX))) + "," + (str(self.nextPosicaoY(aceleracaoY))) + ")"
        return res

    # Velocidade Seguinte -> String
    def velocidadeNext(self, aceleracaoX, aceleracaoY):
        res = "(" + (str(self.nextVelocidadeX(aceleracaoX))) + "," + (str(self.nextVelocidadeY(aceleracaoY))) + ")"
        return res


    def listaMov(self):
        listaaceleracoes = [-1, 0, 1]

        #lista de todas as possibilidades de velocidades
        listaVs = []
        for x in listaaceleracoes:
            for y in listaaceleracoes:
                listaVs.append([int(self.parteVX())+x,int(self.parteVY())+y])

        #lista de todas as possibilidades de pontos, tendo em conta todas as velocidades
        listaPs = []
        for v in listaVs:
            listaPs.append([int(self.partePX())+v[0],int(self.partePY())+v[1]])
        

        pontosPossiveis = []
        velocidadeMesmoIndiceQuePonto = []
        for idx, p in enumerate(listaPs):
            #print(f"{p[0]}+{p[1]}   -  {circuito[p[0]][p[1]]}")
            if 0 <= p[0] < lines and 0 <= p[1] < cols:
                if circuito[p[0]][p[1]] == "-":
                    self.posicao = self.posicaoNextString(p)
                    self.velocidade = self.velocidadeNextString(listaVs[idx])
                    velocidadeMesmoIndiceQuePonto.append(self.velocidadeNextString(listaVs[idx]))
                    pontosPossiveis.append(self.posicao)
                elif circuito[p[0]][p[1]] == "X":
                    self.velocidade = "(0,0)"
                elif circuito[p[0]][p[1]] == "F":
                    self.posicao = self.posicaoNextString(p)
                    pontosPossiveis.append(self.posicao)
                    velocidadeMesmoIndiceQuePonto.append(self.velocidadeNextString(listaVs[idx]))
                    self.velocidade = self.velocidadeNextString(listaVs[idx])
                
        for idx, ponto in enumerate(pontosPossiveis):
            print(f"ir para {ponto} com velocidade {velocidadeMesmoIndiceQuePonto[idx]}")
            print("\n")
        return pontosPossiveis

    # Criar um grafo partindo do estado inicial com todas as transições possiveis
    def cria_grafo(self):#
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
           estado = estados.pop()
           expansao = self.listaMov()  # Mudar expande
           for e in expansao:
               if e != None:
                   self.g.add_edge(estado, e)
                   if e not in visitados:
                       estados.append(e)
                       visitados.append(e)
