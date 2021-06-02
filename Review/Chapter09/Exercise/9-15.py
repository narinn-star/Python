from tkinter import*

class Plotter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.x, self.y = 50, 75

        self.canvas = Canvas(self, height = 100, width=150, relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        bt1 = Button(self, text='up', command=lambda: self.move(0, -10))
        bt1.pack(side=LEFT)

        bt2 = Button(self, text='left', command=lambda: self.move(-10, 0))
        bt2.pack(side=LEFT)

        bt3 = Button(self, text='right', command=lambda: self.move(10, 0))
        bt3.pack(side=LEFT)

        bt4 = Button(self, text='down', command=lambda: self.move(0, 10))
        bt4.pack(side=LEFT)

        bt5 = Button(self, text='clear', command=self.clear)
        bt5.pack(side=LEFT)

        bt6 = Button(self, text='delete', command=self.delete)
        bt6.pack(side=LEFT)

    def move(self, dx, dy):
        self.canvas.create_line(self.x, self.y, self.x+dx, self.y+dy)
        self.x += dx
        self.y += dy

    def clear(self):
        self.canvas.delete(ALL)

    def delete(self):
        self.x = 50
        self.y = 75

top = Tk()
plot = Plotter(top)
plot.pack()

top.mainloop()