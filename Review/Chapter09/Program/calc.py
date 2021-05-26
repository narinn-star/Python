from tkinter import*

top = Tk()

def calc(event):
    lb2.configure(text = "결과: " + str(eval(en1.get())))
    #en1.delete(0,END)
    

lb1 = Label(top, text="파이썬 수식 입력: ").pack()

en1 = Entry(top)
en1.bind("<Return>", calc)
en1.pack()
lb2 = Label(top, text="결과: ")
lb2.pack()


top.mainloop()
    