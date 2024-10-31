import tkinter
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import time

def foo():
    pass

class TicTacToe:
    def __init__(self):
        self.root = Tk()
        self.root.title("SuperTickTackToe *** Ходит \'X\'")
        self.frame = Frame(self.root)
        self.frame.pack()

        self.reset_button = Button(self.frame, text="Сброс", command=self.reset)
        self.reset_button.grid(row = 10, column = 3, columnspan = 3, sticky=EW)

        self.big_field = [[], [],[]]
        for i in range (3):
            for j in range (3):
                button = Button(self.frame, text="", width=15, height=6, bg = 'beige', command = foo)
                button.grid(row = 3*i, column = 3*j, columnspan = 3, rowspan = 3)
                button.grid_forget()
                self.big_field[i].append(button)
                
    
        self.buttons = [[[[],[],[]], [[],[],[]], [[],[],[]]],[[[],[],[]], [[],[],[]], [[],[],[]]],[[[],[],[]], [[],[],[]], [[],[],[]]]]
        for a in range(3):
            for b in range(3):
                for i in range (3):
                    for j in range (3):
                        if (a + b)%2 == 0:
                            color = 'salmon'
                        else:
                            color = 'lightblue'
                        button = Button(self.frame, text="", width=5, height=2, bg = color, command=lambda a=a, b=b, i=i, j=j: self.make_step(a, b, i, j))
                        button.grid(row = a*3 + i, column = b*3 + j)
                        self.buttons[a][b][i].append(button)

        self.current_player = 'X'
        self.default_opened_fields = [(a,b) for a in range (3) for b in range (3)]
        self.opened_fields = self.default_opened_fields

    def reset(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        self.root.title("SuperTickTackToe *** Ходит \'" + self.current_player + "\'")
        self.default_opened_fields = [(a,b) for a in range (3) for b in range (3)]
        self.opened_fields = self.default_opened_fields
        self.color_opened_fields()
        
        for i in range (3):
            for j in range (3):
                self.big_field[i][j].grid_forget()
                self.big_field[i][j].config(text = '')
    
        for a in range(3):
            for b in range(3):
                for i in range (3):
                    for j in range (3):
                        self.buttons[a][b][i][j].grid(row = a*3 + i, column = b*3 + j)
                        self.buttons[a][b][i][j].config(text = '')
                        
        
        

    #вспомогательная функция, проверяет, является ли строка из кнопок выигрышной
    def check_button_line(self, line):
        if not (line[0]['text'] == 'X' or line[0]['text'] == 'O'):
            return False
        for i in line:
            if i['text'] != line[0]['text']:
                return False
        return line[0]['text']

    #вспомогательная функция, проверяет, является ли поле из кнопок выигрышным
    def check_button_field(self, field):
        lines = [[field[0][0], field[1][1], field[2][2]], [field[0][2], field[1][1], field[2][0]]] + [field[i] for i in range(3)] + [list(list(zip(*field))[i]) for i in range(3)]
        for k in range(8):
            if self.check_button_line(lines[k])!=False:
                return self.check_button_line(lines[k])
        return False

    def color_opened_fields(self):
        for a in range(3):
            for b in range(3):
                for i in range (3):
                    for j in range (3):
                        if (a,b) in self.opened_fields:
                            if (a + b)%2 == 0:
                                color = 'salmon'
                            else:
                                color = 'lightblue'
                        else:
                            if (a + b)%2 == 0:
                                color = 'white'
                            else:
                                color = 'lightgrey'
                        self.buttons[a][b][i][j].config(bg = color)

        

    def open_all_fields(self):
        self.opened_fields = self.default_opened_fields
        
    def change_player(self, a, b):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
        self.root.title("SuperTickTackToe *** Ходит \'" + self.current_player + "\'")
        if self.big_field[a][b]['text'] == '':
            self.opened_fields = [(a,b)]
        else:
            self.opened_fields = self.default_opened_fields
        self.color_opened_fields()

    def transform_field(self, a, b, sign):
        for i in range (3):
            for j in range (3):
                self.buttons[a][b][i][j].grid_forget()
        
        
        self.big_field[a][b].config(text = sign)
        self.big_field[a][b].grid(row = 3*a, column = 3*b, columnspan = 3, rowspan = 3, padx = 10, pady = 10)
        
    

    def make_step(self,a,b,i,j):
        if self.buttons[a][b][i][j]['text'] == '' and (a, b) in self.opened_fields:
            self.buttons[a][b][i][j].config(text = self.current_player)

            #проверяем, не выиграл ли игрок на этом поле
            x = self.check_button_field(self.buttons[a][b])
            if x != False:   
                self.transform_field(a, b, x)

            #проверяем, не выиграл ли игрок на всём поле
            y = self.check_button_field(self.big_field)
            if y != False:  
                tkinter.messagebox.showinfo(title='SuperTickTackToe', message='Игрок ' + self.current_player + ' победил!')
                self.opened_fields = []
                self.color_opened_fields()
            else:
                self.change_player(i, j)
                        
                
    def run(self):
        self.root.mainloop()

TicTacToe().run()
                   


            
