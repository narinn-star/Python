from tkinter import*

top = Tk()
top.title("Temperature")

def fToC():
    h = float(en1.get())
    c = (h - 32) / 1.8
    en2.insert(0, c)

def cToH():
    c = float(en2.get())
    h = (c * 1.8) + 32
    en1.insert(0,h)

lb1 = Label(top, text="화씨")
lb1.grid(row=0, column=0)
lb2 = Label(top, text="섭씨")
lb2.grid(row=1, column=0)

en1 =Entry(top)
en1.grid(row=0, column=1)
en2 = Entry(top)
en2.grid(row=1, column=1)

bt1 = Button(top, width = 10, text="화씨->섭씨", command=fToC)
bt1.grid(row=2, column=0)
bt2 = Button(top, width = 10, text="섭씨->화씨", command=cToH)
bt2.grid(row=2, column=1)

top.mainloop()