from Graph import Grafo
from readFile import readFile
import copy

class Race():

    # Exemplos
    # Posição -> "(10,20)"
    # Velocidade ->  "(1,2)"
    # AceleraçãoX -> 1 e AceleracaoY -> 0
    def __init__(self, circuito_path, startt, endd, checkpoint, velocidade, sndPos):
        # Grafo
        self.g = Grafo(directed=True)  # Verificar directed
        # Posição Atual
        self.posicao = startt
        # Velocidade
        self.velocidade = velocidade

        global file
        global circuito
        global lines
        global cols
        global nestedCircuito
        global start
        global end

        file = readFile(circuito_path)
        circuito = file.ler()
        lines = len(circuito)
        cols = len(circuito[1])
        start = startt
        end = endd
        sndstart = sndPos

        nestedCircuito = []
        for lin in circuito:
            nestedCircuito.append([c for c in lin])

        self.cria_grafo()
        if checkpoint == None:
            print(f"Ponto Final: {end}; Ponto Incial: {start}")
        else:
            print(f"Ponto Final: {end}; Ponto Incial: {start}; Ponto Checkpoint: {checkpoint}")

    # Funcao que dado um circuito devolve em string
    def circuitoAsString(self, circuitoArr):
        res = "    "
        i=0

        while i < len(circuitoArr[0]):
            if len(str(i)) == 2: res += "" + f"{i}" + " "
            else: res += " " + f"{i}" + " "  
            i+=1
        res += "\n" + "-"*len(res) + "\n"
        i=0
        for x in circuitoArr:
            if len(str(i)) == 2: res += f"{i}" + "| "
            else: res += f"{i}" + " | "
            for y in x:
                if len(str(y)) == 2: res += "" + f"{y}" + " "  
                else: res += " " + f"{y}" + " "  
            res = res + "\n"
            i+=1
        res = res + "\n"
        return res

    def mostraCaminho(self, path):
        localCircuito = copy.deepcopy(nestedCircuito)
        for i, point in enumerate(path, start=1):
            localCircuito[int(self.partePX_Custom([point]))][int(self.partePY_Custom([point]))] = f"{i}"
        return self.circuitoAsString(localCircuito)

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

    def PStringtoArr(self, pontoString):
        res = pontoString[1:-1]
        res = res.split(',')
        resint = list(map(int, res))
        return resint

    def ArrToPString(self, pontoArr):
        res = "(" + str(pontoArr[0]) + "," + str(pontoArr[1]) + ")"
        return res




    def check_collision(self, path1, path2, nFinal):
        i = -1
        mins = min(len(path2), len(path1))
        for i in range(mins-1):
            if path1[i] == path2[i]:
                if path1[i] == nFinal:
                    return -1
                else:
                    return i
        return -1
        












    def listaMov(self):
        listaaceleracoes = [-1, 0, 1]

        #lista de todas as possibilidades de velocidades
        self.velocidade = "(0,0)"
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
                pontosPossiveis.append(self.posicaoNextString(p))
                # if nestedCircuito[p[0]][p[1]] == "-":
                      #self.posicao = self.posicaoNextString(p)
                    #  velocidades.append(self.velocidadeNextString(listaVs[idx]))
                    #  pontosPossiveis.append(self.posicaoNextString(p))
                       #self.velocidade = self.velocidadeNextString(listaVs[idx])
                # elif nestedCircuito[p[0]][p[1]] == "X":
                    #  pontosX.append(self.posicaoNextString(p))
                       #self.velocidade = "(0,0)"
                # elif nestedCircuito[p[0]][p[1]] == "F":
                       #self.posicao = self.posicaoNextString(p)
                    #  pontosPossiveis.append(self.posicaoNextString(p))
                    #  velocidades.append(self.velocidadeNextString(listaVs[idx]))
                # elif nestedCircuito[p[0]][p[1]] == "C":
                    #  pontosPossiveis.append(self.posicaoNextString(p))
                    #  velocidades.append(self.velocidadeNextString(listaVs[idx]))
                     #self.velocidade = self.velocidadeNextString(listaVs[idx])
        #print(f"posicaoAtual:      {self.posicao}")
        #print(f"pontosPossiveis    {pontosPossiveis}")
        return pontosPossiveis

    # Criar um grafo partindo do estado inicial com todas as transições possiveis
    def cria_grafo(self):#
        
        estados = []
        visitados = []
        estados.append(start)
        visitados.append(start)
        
        while estados != [] :
            estado = estados.pop()
            self.posicao = estado
            expansao = self.listaMov()  # Mudar expande
            #print(f"estado:   {estado} \nexpansao: {expansao}")
            for e in expansao:
                if e != None:
                    x = self.PStringtoArr(e)
                    x = nestedCircuito[x[0]][x[1]]
                    cost = 1
                    if x == 'X': cost = 25
                    self.g.add_edge(estado, e, cost)
                    if e not in visitados:
                        visitados.append(e)
                        estados.append(e)
                        estados.sort()
            #print(f"\nestados:   {estados} \nvisitados: {visitados}")