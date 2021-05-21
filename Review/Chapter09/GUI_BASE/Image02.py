from tkinter import*
top = Tk()

logo = PhotoImage(file = "mini-logo.png")
lb1 = Label(top, image = logo).pack(side = 'left')

txt = '''A GUI is a type of user 
interface that allows users
to interact with devices
in a graphical way.'''

#lb2 = Label(top, padx = 10, text = txt).pack(side='right')
lb2 = Label(top, padx = 10, text = txt, justify = LEFT).pack(side='right')

top.mainloop()