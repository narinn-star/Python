from tkinter import *

top = Tk()
top.title("BMI 계산")

def calc():
    height = float(en1.get())
    weight = float(en2.get())
    bmi = weight / height ** 2
    en1.delete(0, END) #delete(from ,to) => 엔트리로부터 위치 from에서 to까지의 문자열 삭제
    en2.delete(0, END) 
    en3.insert(0, bmi) #insert(index, text) => 엔트리의 주어진 위치로 텍스트 입력

lb1 = Label(top, text = "키(m)")
lb1.grid(row = 0, column=0)
lb2 = Label(top, text="BMI")
lb2.grid(row=0, column=2)
lb3 = Label(top, text="몸무게(Kg)")
lb3.grid(row=1, column=0)

en1 = Entry(top)
en1.grid(row=0,column=1)
en2 = Entry(top)
en2.grid(row=1, column=1)
en3 = Entry(top)
en3.grid(row=1, column=2)

bt1 = Button(top, width=10, text="계산", command=calc)
bt1.grid(row=2, column=2)

top.mainloop()