from tkinter import*

top = Tk()

buttons = [['1', '2', '3'],
           ['4', '5', '6'],
           ['7', '8', '9'],
           ['*', '0', '#']]

def button(num):
    print(num)

bt1 = Button(top, width = 5, text='1', command=lambda:button(1))
bt2 = Button(top, width = 5, text='2', command=lambda:button(2))
bt3 = Button(top, width = 5, text='3', command=lambda:button(3))
bt4 = Button(top, width = 5, text='4', command=lambda:button(4))
bt5 = Button(top, width = 5, text='5', command=lambda:button(5))
bt6 = Button(top, width = 5, text='6', command=lambda:button(6))
bt7 = Button(top, width = 5, text='7', command=lambda:button(7))
bt8 = Button(top, width = 5, text='8', command=lambda:button(8))
bt9 = Button(top, width = 5, text='9', command=lambda:button(9))
btstar = Button(top, width = 5, text='*', command=lambda:button('*'))
bt0 = Button(top, width = 5, text='0', command=lambda:button(0))
btsharp = Button(top, width = 5, text='#', command=lambda:button('#'))

bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)
bt3.grid(row=0, column=2)
bt4.grid(row=1, column=0)
bt5.grid(row=1, column=1)
bt6.grid(row=1, column=2)
bt7.grid(row=2, column=0)
bt8.grid(row=2, column=1)
bt9.grid(row=2, column=2)
btstar.grid(row=3, column=0)
bt0.grid(row=3, column=1)
btsharp.grid(row=3, column=2)





top.mainloop()