from tkinter import*

top = Tk()
top.title("Oval을 이용한 그림판")

penC = "blue"

def paint(event):
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    cnvs.create_oval(x1, y1, x2, y2, outline=penC, fill = penC)

def redColor():
    global penC
    penC = "red"

def greenColor(): 
    global penC
    penC ="green"

def blueColor():
    global penC
    penC = "blue"

cnvs=Canvas(top, width=500, height=150)
cnvs.pack()
cnvs.bind("<B1-Motion>", paint)

bt1 = Button(top, text="빨간색", command=redColor)
bt1.pack(side=LEFT, ipadx=50)
bt2 = Button(top, text="초록색", command=greenColor)
bt2.pack(side=LEFT, ipadx=50)
bt3 = Button(top, text="파란색", command=blueColor)
bt3.pack(side=LEFT, ipadx=50)

top.mainloop()