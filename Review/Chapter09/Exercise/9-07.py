from tkinter import*

def up():
    global y, canvas
    canvas.create_line(x, y, x, y-10)
    y -= 10

def left():
    global x, canvas
    canvas. create_line(x, y, x-10, y)
    x -= 10

def right():
    global x, canvas
    canvas.create_line(x, y, x+10,y)
    x += 10

def down():
    global y, canvas
    canvas.create_line(x, y, x, y+10)
    y += 10

top = Tk()

canvas = Canvas(top, height=100, width=150, relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)

box = Frame(top)
box.pack(side=RIGHT)

bt1 = Button(box, text='up', command=up)
bt1.grid(row=0, column=0, columnspan=2)

bt2 = Button(box, text='left', command=left)
bt2.grid(row=1, column=0)

bt3 = Button(box, text='right', command=right)
bt3.grid(row=1, column=1)

bt4 = Button(box, text='down', command=down)
bt4.grid(row=2, column=0, columnspan=2)

x, y = 50, 75 #펜 위치, 중앙으로 초기화

top.mainloop()