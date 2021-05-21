from tkinter import*
top = Tk()

click = PhotoImage(file = 'click.png')
bt = Button(top, image = click, text = "클릭하세요!", compound=TOP)
bt.pack()

top.mainloop()