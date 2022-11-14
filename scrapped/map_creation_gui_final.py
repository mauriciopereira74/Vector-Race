import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
from tkinter import filedialog as fd


class app:
    global buttons
    buttons = []
    global buttons_aux
    buttons_aux = []

    def __init__(self, master):
        self.master = master
        self.master.title("Map Creation Tool")
        self.master.geometry("200x200")
        self.MapSize()
            
    def MapSize(self):
        for i in self.master.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.master, width=500, height=500)
        self.frame1.pack()

        def temp_text1(e):
            lin.delete(0,"end")
        def temp_text2(e):
            col.delete(0,"end")

        self.reg_txt1= ttk.Label(self.frame1, text='Nº de Linhas do Circuito')
        self.reg_txt1.pack(side=tk.TOP)
        lin = ttk.Entry(self.frame1, width=20, justify="center", text = "#Linhas",)
        lin.insert(5, "#Linhas")
        lin.pack(pady=5, side=tk.TOP)


        self.reg_txt2 = ttk.Label(self.frame1, text='Nº de Colunas do Circuito')
        self.reg_txt2.pack(side=tk.TOP)
        col = ttk.Entry(self.frame1, width=20, justify="center", text = "#Colunas")
        col.insert(5, "#Colunas")
        col.pack(pady=5, side=tk.TOP)

        lin.bind("<FocusIn>", temp_text1)
        col.bind("<FocusIn>", temp_text2)

        def getEntryValues():
            global cols
            cols = col.get()
            global lines
            lines = lin.get()
            app.gridPage(self)

        self.gridPage_btn = tk.Button(self.frame1, bg="grey", text="Mostrar Circuito", command = getEntryValues)
        self.gridPage_btn.pack(pady=10)

        def getMapDatafromFile():
            global cols
            global lines
            global buttons_aux
            global opened_file_path
            filename = fd.askopenfilename()
            #opened_file_path = filename.name
            f = open(filename)
            file_data = f.read()
            txt_lines = file_data.split('\n')
            txt_lines.pop()
            txt_lines_nested = []
            for i in txt_lines:
                txt_lines_nested.append(i.split(' '))
            cols = len(txt_lines)
            lines = len(txt_lines_nested)
            buttons_aux = txt_lines_nested
            app.gridPage(self)

        save_btn = tk.Button(self.frame1, bg="grey", text="Abrir circuito.txt", command=getMapDatafromFile)
        save_btn.pack(pady = 5)


    def gridPage(self):
        if int(cols) < 7 and int(lines) < 7:
            resizeWindowString = "270x270"
        else:
            resizeWindowString = str(int(cols)*40)+"x"+str(int(lines)*40)
        self.master.geometry(resizeWindowString)
        for i in self.master.winfo_children():
            i.destroy()

        self.frame2 = Frame(self.master,  padx=15, pady=15)
        self.frame2.place(relx=.5, rely=.5, anchor=CENTER)

        global j

        def getButtonsTextData():
            buttons_data = []
            for x in range(len(buttons)):
                buttons_data_row = []
                for y in range(len(buttons[x])):
                    temp = buttons[x][y].cget('text')
                    if temp == "  ": temp = "-"
                    buttons_data_row.append(temp)
                buttons_data.append(buttons_data_row)
            j = 0
            while os.path.exists("Circuitos/circuito%s.txt" % j):
                j += 1
            with open("Circuitos/circuito%s.txt" % j, "w") as txt_file:
                for line in buttons_data:
                    txt_file.write(" ".join(line) + "\n")
            if save_btn.cget('text') == "Guardar .txt":
                save_btn.config(text=f"Guardado como circuito{j}.txt", fg='green', bg='white')
            else: save_btn.config(text=f"Guardado como circuito{j}.txt")


        def click(row, col):
            temp = buttons[row][col].cget('text')
            if temp == "X":
                buttons[row][col].config(text='  ', bg='white')
            elif temp == "  ":
                buttons[row][col].config(text='P', bg='green')
            elif temp == "P":
                buttons[row][col].config(text='F', bg='red')
            elif temp == "F":
                buttons[row][col].config(text='X', bg='black')

        if buttons == []:
            for linha in range(int(lines)):
                button_row = []
                for coluna in range(int(lines)):
                    btn = tk.Button(self.frame2, text="X", bg='black', command=lambda row=linha, column=coluna: click(row, column))
                    btn.grid(row=linha, column=coluna, sticky=E+W+N+S)
                    button_row.append(btn)
                buttons.append(button_row)
        else:
            for linha in range(int(lines)):
                button_row = []
                for coluna in range(int(lines)):
                    text_in_button = buttons_aux[linha][coluna]
                    
                    if text_in_button == 'X': color = 'black'
                    elif text_in_button == 'P': color = 'green'
                    elif text_in_button == 'F': color = 'red'
                    elif text_in_button == '  ': color = 'white'
                    btn = tk.Button(self.frame2, text=f"{text_in_button}", bg=f'{color}', command=lambda row=linha, column=coluna: click(row, column))
                    btn.grid(row=linha, column=coluna, sticky=E+W+N+S)
                    button_row.append(btn)
                buttons.append(button_row)

        
        self.frame3 = Frame(self.master)
        self.frame3.pack(side=tk.BOTTOM, pady=5)

        save_btn = tk.Button(self.frame3, bg="grey", text="Guardar .txt", command=getButtonsTextData)
        save_btn.pack()

root = Tk()
app(root)
root.mainloop()
