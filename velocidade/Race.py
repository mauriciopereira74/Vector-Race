from Graph import Grafo
from readFile import readFile
import copy
import itertools as it


class Race():

    # Exemplos
    # Posição -> "(10,20)"
    # Velocidade ->  "(1,2)"
    # AceleraçãoX -> 1 e AceleracaoY -> 0
    def __init__(self, circuito_path, startt, endd, checkpoint, velocidade):
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
        global nestedVelocity
        global visitados


        file = readFile(circuito_path)
        circuito = file.ler()
        lines = len(circuito)
        cols = len(circuito[1])
        start = startt
        end = endd

        nestedCircuito = []
        for lin in circuito:
            nestedCircuito.append([c for c in lin])

        nestedVelocity = []
        for idx, lin in enumerate(circuito):
            # nestedVelocity.append([velocidade for c in lin])
            nestedVelocity.append([dict() for x in lin])
        pontoAtualArr = self.PStringtoArr(startt)
        nestedVelocity[pontoAtualArr[0]][pontoAtualArr[1]] = dict({start:velocidade}) 

        self.cria_grafo()
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


    #funcao que retorna lista de velocidades da path resultante
    def getPathVelocitys(self, path):
        lstVelocidadesPontos = []
        for point in path:
            print(point)
            lstVelocidadesPontos.append(nestedVelocity[int(self.partePX_Custom([point]))][int(self.partePY_Custom([point]))])
        return lstVelocidadesPontos

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

    # Retorna o X de um ponto String
    def partePX_Custom(self, arr):
        res = arr[0][1:-1] # Tirar primeiro e último elemento
        res = res.split(',') # Partir a string na virgula
        return res[0] # Retorna o primeiro elemento em String

    # Retorna o Y de um ponto String
    def partePY_Custom(self, arr):
        res = arr[0][1:-1] # Tirar primeiro e último elemento
        res = res.split(',') # Partir a string na virgula
        return res[1] # Retorna o primeiro elemento em String

    # Transforma um ponto string num array
    def PStringtoArr(self, pontoString):
        res = pontoString[1:-1]
        res = res.split(',')
        resint = list(map(int, res))
        return resint

    # Transforma um ponto array numa string
    def ArrToPString(self, pontoArr):
        res = "(" + str(pontoArr[0]) + "," + str(pontoArr[1]) + ")"
        return res

    # Transforma uma velocidade string num array
    def VStringtoArr(self, velString):
        res = velString[1:-1]
        res = res.split(',')
        resint = list(map(int, res))
        return resint

    # Transforma uma velocidade array numa string
    def ArrToVString(self, velArr):
        res = "(" + str(velArr[0]) + "," + str(velArr[1]) + ")"
        return res

    #lista de todas as possibilidades de velocidades
    def getListVelocidadesPossíveis(self):
        listaaceleracoes = [-1, 0, 1]

        # self.velocidade = "(0,0)"
        pontoAtualArr = self.PStringtoArr(self.posicao)
        vEmPonto = nestedVelocity[pontoAtualArr[0]][pontoAtualArr[1]]
        if len(vEmPonto) == 1:
            onlyelem = list(vEmPonto.values())[0]
            self.velocidade = onlyelem
        else:
            print(vEmPonto)
            onlyelem = list(vEmPonto.values())[0]
            self.velocidade = onlyelem

        listaVs = []
        lstTeste = []

        xDaVelMax = int(self.parteVX())
        yDaVelMax = int(self.parteVY())

        if xDaVelMax < 0 and yDaVelMax < 0: 
            for x in range(xDaVelMax-1, 0):
                for y in range(yDaVelMax-1, 0):
                    lstTeste.append([x,y])
        elif xDaVelMax > 0 and yDaVelMax > 0:
            for x in range(0, xDaVelMax+2):
                for y in range(0, yDaVelMax+2):
                    lstTeste.append([x,y])
        elif xDaVelMax < 0 and yDaVelMax > 0:
            for x in range(xDaVelMax-1, 0):
                for y in range(0, yDaVelMax+2):
                    lstTeste.append([x,y])
        elif xDaVelMax > 0 and yDaVelMax < 0:
            for x in range(0, xDaVelMax+2):
                for y in range(yDaVelMax-1, 0):
                    lstTeste.append([x,y])
        elif xDaVelMax == 0 and yDaVelMax == 0:
            for x in range(-1, 2):
                for y in range(-1, 2):
                    lstTeste.append([x,y])
        elif xDaVelMax == 0 and yDaVelMax < 0:
            for x in range(-1, 2):
                for y in range(yDaVelMax-1, 0):
                    lstTeste.append([x,y])
        elif xDaVelMax == 0 and yDaVelMax > 0:
            for x in range(-1, 2):
                for y in range(0, yDaVelMax+2):
                    lstTeste.append([x,y])
        elif xDaVelMax < 0 and yDaVelMax == 0:
            for x in range(xDaVelMax-1, 0):
                for y in range(-1, 1):
                    lstTeste.append([x,y])
        elif xDaVelMax > 0 and yDaVelMax == 0:
            for x in range(0, xDaVelMax+2):
                for y in range(-1, 1):
                    lstTeste.append([x,y])


        for idx, x in enumerate(lstTeste):
            if x == [0,0]:
                lstTeste.pop(idx)
        # for x in range(abs(xDaVelMax)+1):
            # for y in range(abs(yDaVelMax)+1):
                # lstTeste.append([x,y])
        # print(f"print testttttttt: {lstTeste}")

        # for x in listaaceleracoes:
            # for y in listaaceleracoes:
                # listaVs.append([xDaVelMax+x,yDaVelMax+y])
# 
        # listaaT = []
        # for acel in listaaceleracoes:
            # for xP in range(xDaVelMax+1):
                # for yP in range(yDaVelMax+1):
                    # listaaT.append([xP+acel,yP])
        # for acel in listaaceleracoes:
            # for xP in range(xDaVelMax+1):
                # for yP in range(yDaVelMax+1):
                    # listaaT.append([xP,yP+acel])
# 
        # print(listaaT)
        # listT = []
        # for y in listaVs:
            # if y not in listT:
                # listT.append(y)

        # for x in listaaceleracoes:
            # for y in listaaceleracoes:
                # listaVs.append([xDaVelMax+x,yDaVelMax+y])
        return lstTeste


    #lista de todas as possibilidades de pontos, tendo em conta todas as velocidades
    def getListPontosPossíveis(self):
        listaVs = self.getListVelocidadesPossíveis()

        listaPs = []
        for v in listaVs:
            listaPs.append([int(self.partePX())+v[0],int(self.partePY())+v[1]])
        return listaPs

    def barreirasBetween(self, p1x, p1y, pontoAtualStr):
        pontoAtual = self.PStringtoArr(pontoAtualStr)
        if p1x != pontoAtual[0] or p1y != pontoAtual[1]:
            if p1x == pontoAtual[0]:
                minx = min(p1y, pontoAtual[1])
                maxx = max(p1y, pontoAtual[1])
                for x in range(minx, maxx+1):
                    if nestedCircuito[p1x][x] == 'X': return False
            elif p1y == pontoAtual[1]:
                minx = min(p1x, pontoAtual[0])
                maxx = max(p1x, pontoAtual[0])
                for x in range(minx, maxx+1):
                    if nestedCircuito[x][p1y] == 'X': return False
        return True

    def listaMov(self, lastEstado):
        listaVs = self.getListVelocidadesPossíveis()
        listaPs = self.getListPontosPossíveis()

        pontosPossiveis = []
        velocidades = []
        pontosX = []
        for idx, p in enumerate(listaPs):
            if 0 <= p[0] < lines and 0 <= p[1] < cols:
                if nestedCircuito[p[0]][p[1]] == "-":
                     #self.posicao = self.posicaoNextString(p)
                     velocidades.append(self.ArrToVString(listaVs[idx]))
                     pontosPossiveis.append(self.ArrToPString(p))
                     nestedVelocity[p[0]][p[1]].update({lastEstado:self.ArrToVString(listaVs[idx])})
                     #self.velocidade = self.ArrToVString(listaVs[idx])
                elif nestedCircuito[p[0]][p[1]] == "X":
                     pontosX.append(self.ArrToPString(p))
                     #self.velocidade = "(0,0)"
                elif nestedCircuito[p[0]][p[1]] == "F":
                     #self.posicao = self.ArrToPString(p)
                     pontosPossiveis.append(self.ArrToPString(p))
                     velocidades.append(self.ArrToVString(listaVs[idx]))
                     nestedVelocity[p[0]][p[1]].update({lastEstado:self.ArrToVString(listaVs[idx])})
                elif nestedCircuito[p[0]][p[1]] == "C":
                     pontosPossiveis.append(self.ArrToPString(p))
                     velocidades.append(self.ArrToVString(listaVs[idx]))
                     nestedVelocity[p[0]][p[1]].update({lastEstado:self.ArrToVString(listaVs[idx])})
                     #self.velocidade = self.ArrToVString(listaVs[idx])
        #print(f"posicaoAtual:      {self.posicao}")
        #print(f"pontosPossiveis    {pontosPossiveis}")
        # self.exchangeVelocity(velocidades)
        return pontosPossiveis

    # Criar um grafo partindo do estado inicial com todas as transições possiveis
    def cria_grafo(self):#
        
        estados = []
        visitados = []
        estados.append(start)
        visitados.append(start)
        lastVisited = start
        
        while estados != [] :
            estado = estados.pop()
            self.posicao = estado
            pontoEstado = self.PStringtoArr(estado)
            xxxxxxxxxxxxx = nestedVelocity[pontoEstado[0]][pontoEstado[1]]
            # self.velocidade = nestedVelocity[pontoEstado[0]][pontoEstado[1]][lastVisited]
            expansao = self.listaMov(estado)  # Mudar expande
            #print(f"estado:   {estado} \nexpansao: {expansao}")
            for idx, e in enumerate(expansao):
                if e != None:
                    x = self.PStringtoArr(e)
                    x = nestedCircuito[x[0]][x[1]]
                    cost = 1
                    if x == 'X': cost = 25
                    self.g.add_edge(estado, e, cost)
                    lastVisited = visitados[-1]
                    if e not in visitados:
                        visitados.append(e)
                        estados.append(e)
                        # estados.sort()
            #print(f"\nestados:   {estados} \nvisitados: {visitados}")