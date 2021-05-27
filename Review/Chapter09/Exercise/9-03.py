from tkinter import*
from time import *

top = Tk()

def click1():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',
                    localtime())
    print('Local time\n', time)

def click2():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n',
                    gmtime())
    print('Local time\n', time)


ltbutton = Button(top, text='Local time', command=click1)
gtbutton = Button(top, text='Greenwich', command=click2)

ltbutton.pack(side=LEFT)
gtbutton.pack(side=LEFT)

top.mainloop()