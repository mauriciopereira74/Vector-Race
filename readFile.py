from color import style

class readFile:

    # # Lista de listas de strings
    # # Função para ler o ficheiro e colocar a informação numa lista de listas
    # def matrix(file):
    #     contents = open(file).read()
    #     return [item.split() for item in contents.split('\n')[:-1]]
    #
    # # Abrir ficheiro em modo leitura e ler linha a linha e fechar o ficheiro
    # fileOpen = open("circuito", "rt")
    # file = fileOpen.readlines()
    # fileOpen.close()
    #
    # # Armazenar o circuito numa Lista de Strings
    # circuito = matrix("circuito")
    # print(circuito)
    #
    # x = 'X'
    # z = '-'
    # p = 'P'
    # f = 'F'
    #
    # for i in range(len(circuito)):
    #     for j in range(len(circuito[i])):
    #         if (circuito[i][j] == x):
    #             print(style.BLACK + "X")
    #             print("\n")
    #         if (circuito[i][j] == z):
    #             print(style.RED + "X")
    #             print("\n")
    #         if (circuito[i][j] == p):
    #             print(style.CYAN + "X")
    #             print("\n")
    #         if (circuito[i][j] == f):
    #             print(style.WHITE + "X")
    #             print("\n")


    # Lista de Strings
    # Abrir ficheiro em modo leitura e ler linha a linha e fechar o ficheiro
    fileOpen = open("circuito", "rt")
    file = fileOpen.readlines()
    fileOpen.close()

    # Armazenar o circuito numa Lista de Strings
    circuito = []
    for sub in file:
       circuito.append(sub.replace("\n", ""))
    print(circuito)

    x = 'X'
    z = '-'
    p = 'P'
    f = 'F'

    string = ""
    for i in range(len(circuito)):
        string = string + ("\n")
        for j in range(len(circuito[i])):
            if (circuito[i][j] == x):
                string = string + (style.RED + "X")
            if (circuito[i][j] == z):
                string = string + (style.BLACK + "-")
            if (circuito[i][j] == p):
                string = string + (style.CYAN + "P")
            if (circuito[i][j] == f):
                string = string + (style.WHITE + "F")
    print(string.strip())


