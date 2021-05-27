from random import*
from tkinter import*

top = Tk()
top.title("덧셈 & 뺄셈")


class Ed:
    res = 0
    cnt = 0
    def result():
        Ed.cnt = 0
        a, b = randint(0, 9), randint(0, 9)
        op = randint(0, 1)
       
        if op == 0:
            s = str(a) + ' + ' + str(b)
            Ed.res = a + b

        else:
            if a < b:
                s = str(b) + ' - ' + str(a)
                Ed.res = b - a
            else:
                s = str(a) + ' - ' + str(b)
                Ed.res = a - b
        en1.delete(0, END)
        en1.insert(0, s)
        en2.delete(0, END)
        
    def calc():
        user = str(en2.get())
        if user == str(Ed.res):
            Ed.cnt += 1
            print("You got it!", "count : ", Ed.cnt)  
            en2.delete(0,END)
            Ed.result()
        else:
            Ed.cnt += 1
            en2.delete(0,END)

        
 
            
en1 = Entry(top)
en1.pack() 
en2 = Entry(top)
en2.pack(pady=20)

res = Ed.result()
bt1 = Button(top, text="Enter", command=Ed.calc)
bt1.pack()

top.mainloop()