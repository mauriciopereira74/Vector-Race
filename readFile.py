# from color import style

class readFile:

    global file
    fileOpen = open("circuito.txt", "rt")
    file = fileOpen.readlines()
    fileOpen.close()

    global circuito
    circuito = []
    for sub in file:
        circuito.append(sub.replace("\n", ""))

    # Função que lê um ficheiro coloca toda a sua informação numa Lista de Strings
    def ler(self):
        return circuito

    # Determina a CoordenadaX e Y da Posição Inicial
    def PInicialXY(self):
        print(circuito)
        for i in range(len(circuito)):
          for j in range(len(circuito[i])):
              if circuito[i][j] == "P":
                  print(f"({i},{j})")
                  return f"({i},{j})"
                
    def demonstra(self):
        x = 'X'
        z = '-'
        p = 'P'
        f = 'F'

        string = ""
        for i in range(len(circuito)):
            string = string + ("\n")
            for j in range(len(circuito[i])):
                if (circuito[i][j] == x):
                    string = string + "X"
                if (circuito[i][j] == z):
                    string = string + "-"
                if (circuito[i][j] == p):
                    string = string + "P"
                if (circuito[i][j] == f):
                    string = string + "F"

        return string
