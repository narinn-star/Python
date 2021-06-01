from tkinter import *
from time import strptime, strftime, localtime
from tkinter.messagebox import showinfo

class Day(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        label = Label(self, text='Enter date')
        label.grid(row=0, column=0)

        self.dateEnt = Entry(self) #인스턴스 변수
        self.dateEnt.grid(row=0, column=1)

        button = Button(self, text='Enter',
                        command=self.compute)
        button.grid(row=1, column=0, columnspan=2)

    def compute(self):
        date = self.dateEnt.get()
        weekday = strftime('%A', strptime(date, '%b %d, %Y'))
        showinfo(message='{} was a {}'.format(date, weekday))
        self.dateEnt.delete(0, END)

top = Tk()

day = Day(top)
day.pack()

top.mainloop()