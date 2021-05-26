from tkinter import *
top = Tk()

def kcal():
    print("총 소모 칼로리 : ", int(en.get())*156)

lb1 = Label(top, text= "칼로리 계산")
lb1.grid(row=0, column=0)
lb2 = Label(top, text = "운동시간")
lb2.grid(row = 1, column=0)

en = Entry(top)
en.grid(row = 1, column= 1)

bt1 = Button(top, text="계산", command=kcal)
bt1.grid(row = 2, column=0)
bt2 = Button(top, text="종료", command=top.quit)
bt2.grid(row = 2, column=1)

top.mainloop()