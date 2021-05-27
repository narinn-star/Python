from tkinter.messagebox import showinfo
from tkinter import *
from time import strftime, localtime

top = Tk()

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    showinfo(message=time)

button = Button(top, text ='Click it', command=clicked)
button.pack()

top.mainloop()