from tkinter import *
from time import strftime, localtime

def clicked():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    print(time)

top = Tk()

button = Button(top, text ='Click it', command=clicked)
button.pack()

top.mainloop()