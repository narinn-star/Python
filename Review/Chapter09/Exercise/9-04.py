from tkinter import*
from time import strftime, strptime


top = Tk()


def compute():
    global dateEnt

    date = dateEnt.get()

    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    dateEnt.insert(0, weekday + ' ')


def clear():
    global dateEnt
    dateEnt.delete(0, END)


label = Label(top, text='Enter date')
label.grid(row=0, column=0)

dateEnt = Entry(top)
dateEnt.grid(row=0, column=1)

button = Button(top, text='Enter', command=compute)
button.grid(row=1, column=0)

clearb = Button(top, text='Clear', command=clear)
clearb.grid(row=1, column=1)


top.mainloop()
