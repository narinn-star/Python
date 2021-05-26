from tkinter import *

top = Tk()
top.title="라디오 버튼"
ch = IntVar()

dog = PhotoImage(file="dog.png")
cat = PhotoImage(file="cat.png")
rabbit = PhotoImage(file="rabbit.png")
bird = PhotoImage(file="bird.png")

def choice():
    pic = ch.get()
    if pic == 1:
        img = dog
    elif pic == 2:
        img = cat
    elif pic == 3:
        img = rabbit
    elif pic == 4:
        img = bird
    lb2 = Label(fr, image = img)
    lb2.grid(row = 0, column=1,rowspan=10)

lb1 = Label(top, text="가장 선호하는 동물을 고르시오 : ")
lb1.pack()

fr = Frame(top)
fr.pack(side=LEFT)


rb1 = Radiobutton(fr, text="개", variable=ch, value = 1, command=choice)
rb1.grid(row = 0, column=0, sticky=W)
rb2 = Radiobutton(fr, text="고양이", variable=ch, value = 2, command=choice)
rb2.grid(row=1, column=0, sticky=W)
rb3 = Radiobutton(fr, text="토끼", variable=ch, value = 3, command=choice)
rb3.grid(row=2, column=0, sticky=W)
rb4 = Radiobutton(fr, text="새", variable=ch, value = 4, command=choice)
rb4.grid(row=3, column=0, sticky=W)

top.mainloop()