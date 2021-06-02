from tkinter import*
from time import*
from tkinter.messagebox import showinfo

top = Tk()

def click1():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', localtime())
    showinfo(message=time, title='Local time')

def click2():
    time = strftime('Day: %d %b %Y\nTime: %H:%M:%S %p\n', gmtime())
    showinfo(message=time, title='Greenwich time')

ltbutton = Button(top, text='Local time', command=click1)
gtbutton = Button(top, text='Greenwich time', command=click2)

ltbutton.pack(side=LEFT)
gtbutton.pack(side=LEFT)

top.mainloop()