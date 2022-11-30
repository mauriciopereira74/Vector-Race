import os
from tkinter import *
from track import *
from tk import TrackView

class Application2(Frame):

    def __init__(self, master=None):
        self.createTrack()
        
        Frame.__init__(self, master)
        self.grid(sticky=NSEW)

        self.createWidgets()

    def createTrack(self):

        def dimensao(altura, largura):
            circuito = []
            circuito.append('X' * largura)
            for x in range(altura - 2):
                circuito.append('X' + ('-' * (largura - 2)) + 'X')
            circuito.append('X' * largura)
            return circuito

        def pontos(circuito, start, finish):
            ind = len(circuito) - start[1] - 1
            tmp = list(circuito[ind])
            tmp[start[0]] = 'P'
            tmp2 = ""
            for x in tmp:
                tmp2 += x
            circuito[ind] = tmp2

            ind = len(circuito) - finish[1] - 1
            tmp = list(circuito[ind])
            tmp[finish[0]] = 'F'
            tmp2 = ""
            for x in tmp:
                tmp2 += x
            circuito[ind] = tmp2

            return circuito

        def checkpoints(circuito, check):
            ind = len(circuito) - check[1] - 1
            tmp = list(circuito[ind])
            tmp[check[0]] = 'C'
            tmp2 = ""
            for x in tmp:
                tmp2 += x
            circuito[ind] = tmp2

            return circuito

        def barreiras(circuito, p1, p2):
            ind = len(circuito) - p1[1] - 1
            tmp = list(circuito[ind])
            r = p2[0] - p1[0]
            i = p1[0]
            while r >= 0:
                tmp[i] = 'X'
                r -= 1
                i += 1
            tmp2 = ""
            for x in tmp:
                tmp2 += x
            circuito[ind] = tmp2

            return circuito         

        def get_next_file_num():
            dir_list = os.listdir("./Circuitos")
            return int(sorted(dir_list)[-1].split(".")[0][-1])

        print("Para criar um circuito e necessario ter as dimensoes, as coordendas dos pontos de partida e de chegada e as coordenadas das barreiras.")
        altura = int(input("Altura do circuito: ")) # 5
        largura = int(input("Largura do circuito: ")) # 8

        txt_circuito = dimensao(altura, largura)

        print("As coordenadas dos pontos precisam de ser dadas em forma de tuplo. Ex: (0,0)")
        start_i = eval(input("Coordenadas do ponto de partida: ")) # (1,3)
        start = Point(start_i[0], start_i[1])
        finish_i = eval(input("Coordenadas do ponto de chegada: ")) # (9,3)
        finish = Point(finish_i[0], finish_i[1])

        txt_circuito = pontos(txt_circuito, start_i, finish_i)

        barriers = []
        num_barriers = int(input("Quantas barreiras vao ser adicionadas? "))
        if num_barriers > 0:
            print("Cada barreira e uma linha reta entre 2 pontos. Portanto, para cada barreira e necessario ter as coordenadas de 2 pontos.")
        for x in range(num_barriers):
            p1_i = eval(input("Coordenadas do ponto 1 da barreira {}: ".format(x+1)))
            p1 = Point(p1_i[0], p1_i[1]) 
            p2_i = eval(input("Coordenadas do ponto 2 da barreira {}: ".format(x+1)))
            p2 = Point(p2_i[0], p2_i[1])
            barriers.append(LineSegment(p1, p2))
            txt_circuito = barreiras(txt_circuito, p1_i, p2_i)

        checks = []
        num_checks = int(input("Quantos checkpoints vao ser adicionados? "))
        if num_checks > 0:
            print("Cada checkpoint corresponde a um ponto. As coordenadas precisam de ser dadas em forma de tuplo. Ex: (0,0)")
        for x in range(num_checks):
            c = eval(input("Coordenadas do checkpoint {}: ".format(x+1)))
            checks.append(Point(c[0], c[1]))
            txt_circuito = checkpoints(txt_circuito, c)

        path = "./Circuitos/circuito" + str(get_next_file_num() + 1) + ".txt"
        circuito_export = open(path, "w")
        for line in txt_circuito:
            circuito_export.write(line)
            circuito_export.write('\n')
        circuito_export.close()

        self.track = Track(largura - 2, altura - 2, start, finish, barriers, checks)

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.title('Race Track')
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.menuBar = Menu(top)
        top['menu'] = self.menuBar
        self.fileMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)
        self.fileMenu.add_command(label='Quit', command=self.quit, 
                                  accelerator="Ctrl-q")
        self.viewMenu = Menu(self.menuBar)
        self.menuBar.add_cascade(label='View', menu=self.viewMenu)

        self.trackview = TrackView(self, self.track, 
                                   borderwidth=2, relief=GROOVE)
        self.trackview.grid(row=0, column=0, sticky=NSEW)

        self.xscroll = Scrollbar(self, orient=HORIZONTAL, 
                                 command=self.trackview.xview)
        self.yscroll = Scrollbar(self, orient=VERTICAL, 
                                 command=self.trackview.yview)
        self.xscroll.grid(row=1, column=0, sticky=EW)
        self.yscroll.grid(row=0, column=1, sticky=NS)

        self.trackview['xscrollcommand'] = self.xscroll.set
        self.trackview['yscrollcommand'] = self.yscroll.set

        self.viewMenu.add_command(label='Zoom in', 
                                  command=self.trackview.zoomIn, 
                                  accelerator="Ctrl-+")
        self.viewMenu.add_command(label='Zoom out', 
                                  command=self.trackview.zoomOut, 
                                  accelerator="Ctrl--")

        buttonframe = Frame(self)
        buttonframe.grid(row=2, column=0, columnspan=2)
        self.prefixlen = StringVar()
        isIntCommand = self.register(self.isInt)
        self.prefixentry = Entry(buttonframe, textvariable=self.prefixlen,
                                 width=6, validate='all',
                                 validatecommand=(isIntCommand, '%P'))
        self.prefixentry.grid(row=0, column=0, padx=10, pady=2)

    def isInt(self, value):
        if value == "":
            return True
        try:
            int(value)
            return True
        except ValueError:
            return False
