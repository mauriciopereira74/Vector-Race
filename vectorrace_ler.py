from tkinter import *
from track import *
from tk import TrackView
import sys
import re

class Application(Frame):

    def __init__(self, default, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=NSEW)
        self.default = default

        self.readTrack(default)
        self.createWidgets()

    def readTrack(self, default):

        self.default = default

        default = "./Circuitos/" + default
        start = []
        finish = []

        file = open(default, "r")
        lines = file.readlines()

        # check if there is only 1 start and 1 finish
        tmp = ""
        for x in range(len(lines)):
            tmp += lines[x][:-1]
        if (tmp.count('P') != 1) or (tmp.count('F') != 1):
            print("Circuito invalido.")
            sys.exit()

        # check if the border only contains X or 1 S/1 F
        border = lines[0][:-1] + lines[-1][:-1]
        for x in range(len(lines) - 2):
            border += lines[x][0]
            border += lines[x][-2]
        num_x = border.count('X')
        if (num_x != len(border)) and (num_x != len(border) - 1) and (num_x != len(border) - 2):
            print(len(border))
            print("Circuito invalido.")
            sys.exit()

        # check if all lines have the same size
        for i, x in enumerate(lines):
            if not x.endswith('\n'):
                lines[i] = f"{x}\n"


        it = iter(lines)
        the_len = len(next(it))

        if not all(len(l) == the_len for l in it):
            print("Circuito invalido.")
            sys.exit()


        largura = len(lines[0])
        altura = len(lines)

        # get start and finish coordinates
        y = -1
        for line in reversed(lines):
            y += 1
            for x in range(largura):
                if line[x] == 'P':
                    start = Point(x, y)
                elif line[x] == 'F':
                    finish = Point(x, y)

        # get barriers
        barriers = []
        f_lines = []
        tmp_lines = lines[1:-1]

        def help_barriers(line, ind):
            try:
                if line[1] == (line[2] - 1):
                    return help_barriers(line[1:], ind+1)
                else:
                    return ind
            except IndexError:
                    return ind

        c = -1
        for line in tmp_lines:
            c += 1
            indexes = []
            for x in re.finditer('X', line):
                indexes.append(x.start())
            f_lines.append(indexes)

        c = 0
        for line in reversed(f_lines):
            c2 = 0
            c += 1
            while c2 < len(line):
                try:
                    if line[c2] == (line[c2+1] - 1):
                        end_barrier = help_barriers(line[c2:], c2+1)
                        barriers.append(LineSegment(Point(line[c2], c), Point(line[end_barrier], c)))
                        c2 == line[end_barrier]
                    else:
                        barriers.append(LineSegment(Point(line[c2], c), Point(line[c2], c)))
                except IndexError:
                    break
                c2 += 1

        self.track = Track(largura - 3, altura - 2, start, finish, barriers)

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
