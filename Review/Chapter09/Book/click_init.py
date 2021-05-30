from tkinter import*
from tkinter.messagebox import showinfo
from time import strftime, localtime

class ClickIt(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        button = Button(self, text='Click it', command=self.clicked)
        button.pack()

    def clicked(self):
        time = strftime('Day : %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
        showinfo(message=time)

top = Tk()
app = ClickIt(top)
app.pack()
top.mainloop()