from tkinter import*
from time import strftime, strptime
from tkinter.messagebox import showinfo

top = Tk()


def compute():
    global dateEnt

    date = dateEnt.get()

    weekday = strftime('%A', strptime(date, '%b %d, %Y'))

    showinfo(message='{} was a {}'.format(date, weekday))

    dateEnt.delete(0, END)


label = Label(top, text='Enter date')
label.grid(row=0, column=0)

dateEnt = Entry(top)
dateEnt.grid(row=0, column=1)

button = Button(top, text='Enter date', command=compute)
button.grid(row=1, column=0, columnspan=2)

top.mainloop()
