# from color import style

class readFile:

    # global file
    # fileOpen = open("circuito.txt", "rt")
    # file = fileOpen.readlines()
    # fileOpen.close()
# 
    # global circuito
    # circuito = []
    # for sub in file:
        # circuito.append(sub.replace("\n", ""))

    def __init__(self, x):
        self.circuito_path = x
        global file
        global circuito
        
        circuito = []
        if self.circuito_path == "":
            fileOpen = open(f"Circuitos/circuito0.txt", "rt")
        else:
            fileOpen = open(f"Circuitos/{self.circuito_path}", "rt")
        file = fileOpen.readlines()
        fileOpen.close()
        for sub in file:
            circuito.append(sub.replace("\n", ""))

    # Função que lê um ficheiro coloca toda a sua informação numa Lista de Strings
    def ler(self):
        return circuito

    # Determina a CoordenadaX e Y da Posição Inicial
    def PInicialXY(self):
        for i in range(len(circuito)):
          for j in range(len(circuito[i])):
              if circuito[i][j] == "P":
                  return f"({i},{j})"

    # Determina a CoordenadaX e Y da Posição Final
    def PFinalXY(self):
        for i in range(len(circuito)):
          for j in range(len(circuito[i])):
              if circuito[i][j] == "F":
                  return f"({i},{j})"

    def PCheckXY(self):
        for i in range(len(circuito)):
          for j in range(len(circuito[i])):
              if circuito[i][j] == "C":
                  return f"({i},{j})"
        return None
                
    def demonstra(self):
        res = "\n    "
        i=0
        nestedCircuito = []
        for lin in circuito:
            nestedCircuito.append([c for c in lin])

        while i < len(nestedCircuito[0]):
            if len(str(i)) == 2: res += "" + f"{i}" + " "
            else: res += " " + f"{i}" + " "  
            i+=1
        res += "\n" + "-"*len(res) + "\n"
        i=0
        for x in nestedCircuito:
            if len(str(i)) == 2: res += f"{i}" + "| "
            else: res += f"{i}" + " | "
            for y in x:
                if len(str(y)) == 2: res += "" + f"{y}" + " "  
                else: res += " " + f"{y}" + " "  
            res = res + "\n"
            i+=1
        res = res + "\n"
        return res



        # x = 'X'
        # z = '-'
        # p = 'P'
        # f = 'F'
 
        # string = ""
        # for i in range(len(circuito)):
            # string = string + ("\n")
            # for j in range(len(circuito[i])):
                # if (circuito[i][j] == x):
                    # string = string + "X"
                # if (circuito[i][j] == z):
                    # string = string + "-"
                # if (circuito[i][j] == p):
                    # string = string + "P"
                # if (circuito[i][j] == f):
                    # string = string + "F"

        # return string
