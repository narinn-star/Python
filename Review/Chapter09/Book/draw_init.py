from tkinter import *

class Draw(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack()

        #마우스 좌표는 인스턴스 변수임
        self.oldx, self.oldy = 0, 0

        self.canvas = Canvas(self, height=100, width=150)
        self.canvas.bind("<Button-1>", self.begin)
        self.canvas.bind("<Button1-Motion>", self.draw)
        self.canvas.pack(expand=True, fill=BOTH)

    def begin(self, event):
        self.oldx, self.oldy = event.x, event.y

    def draw(self, event):
        newx, newy = event.x, event.y
        self.canvas.create_line(self.oldx, self.oldy, newx, newy)
        self.oldx, self.oldy = newx, newy

top = Tk()

draw = Draw(top)
draw.pack()

top.mainloop()

