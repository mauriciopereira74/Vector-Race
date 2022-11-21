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

    # Funcao que dado um circuito devolve em string
    def circuitoAsString(self, circuitoArr):
        res = ""
        for x in circuitoArr:
            for y in x:
                if len(str(y)) == 2: res += " " + f"{y}" + "  "  
                else: res += "  " + f"{y}" + "  "  
            res = res + "\n"
        res = res + "\n"
        return res

    # Função que dado uma String retorna a Posição X da String
    def partePX(self):
        res = self.posicao[1:-1] # Tirar primeiro e último elemento
        res = res.split(',') # Partir a string na virgula
        return res[0] # Retorna o primeiro elemento em String

    # Função que dado uma String retorna a Posição Y da String
    def partePY(self):
        res = self.posicao[1:-1]
        res = res.split(',') 
        return res[1]

    # Função que dado uma String retorna a Velocidade X da String
    def parteVX(self):
        res = self.velocidade[1:-1] 
        res = res.split(',')
        return res[0]

    # Função que dado uma String retorna a Velocidade Y da String
    def parteVY(self):
        res = self.velocidade[1:-1]
        res = res.split(',')
        return res[1]


    def posicaoNextString(self, ponto):
        res = "(" + str(ponto[0]) + "," + str(ponto[1]) + ")"
        return res

    def velocidadeNextString(self, velocidade):
        res = "(" + str(velocidade[0]) + "," + str(velocidade[1]) + ")"
        return res

    def partePX_Custom(self, arr):
        res = arr[0][1:-1] # Tirar primeiro e último elemento
        res = res.split(',') # Partir a string na virgula
        return res[0] # Retorna o primeiro elemento em String

    def partePY_Custom(self, arr):
        res = arr[0][1:-1] # Tirar primeiro e último elemento
        res = res.split(',') # Partir a string na virgula
        return res[1] # Retorna o primeiro elemento em String


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
        velocidades = []
        pontosX = []
        for idx, p in enumerate(listaPs):
            if 0 <= p[0] < lines and 0 <= p[1] < cols:
                if circuito[p[0]][p[1]] == "-":
                     self.posicao = self.posicaoNextString(p)
                     velocidades.append(self.velocidadeNextString(listaVs[idx]))
                     pontosPossiveis.append(self.posicao)
                     #self.velocidade = self.velocidadeNextString(listaVs[idx])
                elif circuito[p[0]][p[1]] == "X":
                     pontosX.append(self.posicaoNextString(p))
                     #self.velocidade = "(0,0)"
                elif circuito[p[0]][p[1]] == "F":
                     self.posicao = self.posicaoNextString(p)
                     pontosPossiveis.append(self.posicao)
                     velocidades.append(self.velocidadeNextString(listaVs[idx]))
                     #self.velocidade = self.velocidadeNextString(listaVs[idx])
        return pontosPossiveis

    # Criar um grafo partindo do estado inicial com todas as transições possiveis
    def cria_grafo(self):#
        readFiles = readFile()
        pFinal = readFiles.PFinalXY() 
        pInicial = readFiles.PInicialXY() 
        print(f"ponto final:  {pFinal}")
        print(f"ponto incial:  {pInicial}")
        
        estados = []
        estados.append(pInicial)
        visitados = []
        visitados.append(pInicial)
        
        while estados != [] :
            estado = estados.pop()
            expansao = self.listaMov()  # Mudar expande
            for e in expansao:
                if e != None:
                    self.g.add_edge(estado, e, 1)
                    if e not in visitados:
                        estados.append(e)
                        visitados.append(e)
    


    def mostraCaminho(self, path):
        i = 1
        localCircuito = []
        for lin in circuito:
            localCircuito.append([c for c in lin])
        for point in path:
            localCircuito[int(self.partePX_Custom([point]))][int(self.partePY_Custom([point]))] = f"{i}"
            i += 1
        return self.circuitoAsString(localCircuito)