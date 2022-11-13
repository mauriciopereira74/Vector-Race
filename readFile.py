# from color import style

class readFile:

    # Função que lê um ficheiro coloca toda a sua informação numa Lista de Strings
    def ler(self):
        fileOpen = open("circuito", "rt")
        file = fileOpen.readlines()
        fileOpen.close()

        # Armazenar o circuito numa Lista de Strings
        circuito = []
        for sub in file:
            circuito.append(sub.replace("\n", ""))
        return circuito
        #print(circuito)

    # Determina a CoordenadaX da Posição Inicial
    def PInicialX(self):
        fileOpen = open("circuito", "rt")
        file = fileOpen.readlines()
        fileOpen.close()

        # Armazenar o circuito numa Lista de Strings
        circuito = []
        for sub in file:
            circuito.append(sub.replace("\n", ""))
        print(circuito)

        for i in range(len(circuito)):
          for j in range(len(circuito[i])):
              if circuito[i][j] == "P":
                  return i

    # Determina a CoordenadaY da Posição Inicial
    def PInicialY(self):
        fileOpen = open("circuito", "rt")
        file = fileOpen.readlines()
        fileOpen.close()

        # Armazenar o circuito numa Lista de Strings
        circuito = []
        for sub in file:
            circuito.append(sub.replace("\n", ""))
        print(circuito)

        for i in range(len(circuito)):
          for j in range(len(circuito[i])):
              if circuito[i][j] == "P":
                  return j









    # # Lista de Strings
    # # Abrir ficheiro em modo leitura e ler linha a linha e fechar o ficheiro
    # fileOpen = open("circuito", "rt")
    # file = fileOpen.readlines()
    # fileOpen.close()
    #
    # # Armazenar o circuito numa Lista de Strings
    # circuito = []
    # for sub in file:
    #    circuito.append(sub.replace("\n", ""))
    # print(circuito)

    # x = 'X'
    # z = '-'
    # p = 'P'
    # f = 'F'
    #
    # string = ""
    # for i in range(len(circuito)):
    #     string = string + ("\n")
    #     for j in range(len(circuito[i])):
    #         if (circuito[i][j] == x):
    #             string = string + (style.RED + "X")
    #         if (circuito[i][j] == z):
    #             string = string + (style.BLACK + "-")
    #         if (circuito[i][j] == p):
    #             string = string + (style.CYAN + "P")
    #         if (circuito[i][j] == f):
    #             string = string + (style.WHITE + "F")
    #print(string.strip())


