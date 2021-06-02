from tkinter import*

class Plotter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.x, self.y = 50, 75

        self.canvas = Canvas(self, height = 100, width=150, relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        bt1 = Button(self, text='up', command=lambda: self.move(0, -10))
        bt1.pack(side=TOP)

        bt2 = Button(self, text='left', command=lambda: self.move(-10, 0))
        bt2.pack(side=BOTTOM)

        bt3 = Button(self, text='right', command=lambda: self.move(10, 0))
        bt3.pack(side=BOTTOM)

        bt4 = Button(self, text='down', command=lambda: self.move(0, 10))
        bt4.pack(side=LEFT)

    def move(self, dx, dy):
        self.canvas.create_line(self.x, self.y, self.x+dx, self.y+dy)
        self.x += dx
        self.y += dy

top = Tk()
plot = Plotter(top)
plot.pack()

top.mainloop()