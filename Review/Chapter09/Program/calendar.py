from tkinter import *

w = Tk()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

for d in range(7):
    lbd = Label(w, padx=15, text=days[d])
    lbd.grid(row = 0, column=d)

week = 1
num = 2

for i in range(1, 31):
    lb1 = Label(w, padx=15, text=str(i))
    lb1.grid(row=week, column=num)

    num += 1
    if num > 6:
       week += 1
       num = 0 

w.mainloop()