from tkinter import *

top = Tk()

def ft():
    lb["text"] ="클릭했습니다."

lb =Label(top)
lb.pack()

bt = Button(top, text="클릭하세요!", command=ft)
bt.pack()

top.mainloop()