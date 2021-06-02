from tkinter import*

class Plotter(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        self.x, self.y = 50, 75

        self.canvas = Canvas(self, height = 100, width=150, relief=SUNKEN, borderwidth=3)
        self.canvas.pack(side=LEFT)

        bt1 = Button(self, text='up', command=self.up)
        bt1.pack(side=LEFT)

    def up(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y-10)
        self.y -= 10

top = Tk()
plot = Plotter(top)
plot.pack()

top.mainloop()