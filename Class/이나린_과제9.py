from tkinter import *
from random import *

top = Tk()
top.title("가위 바위 보 게임")

scissors = PhotoImage(file="가위.png")
rock = PhotoImage(file="바위.png")
paper = PhotoImage(file="보.png")

def d1():
    com = randint(1, 3)
    Label(top, image=scissors).grid(row = 0, column = 0)
    if com == 1:
        lb1["text"] = "비겼습니다."
        Label(top, image=scissors).grid(row = 0, column = 2)
    
    elif com == 2:
        lb1["text"] = "컴퓨터 승!"
        Label(top, image=rock).grid(row = 0, column = 2)
    
    elif com == 3:
        lb1["text"] = "사용자 승!"
        Label(top, image=paper).grid(row = 0, column = 2)

def d2():
    com = randint(1, 3)
    Label(top, image=rock).grid(row = 0, column = 0)
    if com == 1:
        lb1["text"] = "사용자 승!"
        Label(top, image=scissors).grid(row = 0, column = 2)

    elif com == 2:
        lb1["text"] = "비겼습니다."
        Label(top, image=rock).grid(row = 0, column = 2)
    
    elif com == 3:
        lb1["text"] = "컴퓨터 승!"
        Label(top, image=paper).grid(row = 0, column = 2)

def d3():
    com = randint(1, 3)
    Label(top, image=paper).grid(row = 0, column = 0)
    if com == 1:
        lb1["text"] = "컴퓨터 승!"
        Label(top, image=scissors).grid(row = 0, column = 2)

    elif com == 2:
        lb1["text"] = "사용자 승!"
        Label(top, image=rock).grid(row = 0, column = 2)
    
    elif com == 3:
        lb1["text"] = "비겼습니다."
        Label(top, image=paper).grid(row = 0, column = 2)

Label(top, text = "USER", font = "bold").grid(row = 1, column = 0)

lb1 = Label(top, text = "가위 바위 보 !", font = "bold")
lb1.grid(row = 0, column = 1)

Label(top, text = "COM", font = "bold").grid(row = 1, column = 2)

Button(top, text = "가위", width = 20, command = d1, bg = "yellow").grid(row = 2, column = 0)
Button(top, text = "바위", width = 20, command = d2, bg = "yellow").grid(row = 2, column = 1)
Button(top, text = "보", width = 20, command = d3, bg = "yellow").grid(row = 2, column = 2)

top.mainloop()