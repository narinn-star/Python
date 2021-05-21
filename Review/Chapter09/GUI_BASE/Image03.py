from tkinter import*
top = Tk()

logo = PhotoImage(file = "mini-logo.png")

txt = '''A GUI is a type of user 
interface that allows users
to interact with devices
in a graphical way.'''

lb = Label(top, padx=30,
            compound=CENTER,
            text = txt,
            image=logo).pack(side='right')

top.mainloop()