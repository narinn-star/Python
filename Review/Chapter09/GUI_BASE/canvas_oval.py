from tkinter import*

top = Tk()

cnvs=Canvas(top, width=300, height=200)
cnvs.pack()
cnvs.create_oval(10, 10, 200, 150)

top.mainloop()