from tkinter import*
top = Tk()

lb = Label(top, text = "User Name").pack(side = LEFT)
en = Entry(top, show = '*').pack(side=RIGHT)

top.mainloop()