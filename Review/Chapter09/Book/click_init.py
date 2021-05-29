from tkinter import*
from tkinter.messagebox import showinfo
from time import strftime, localtime

class ClickIt(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()
        