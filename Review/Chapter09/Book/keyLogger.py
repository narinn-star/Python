from tkinter import *

top = Tk()

def record(event):
    print('char = {}'.format(event.keysym))


text = Text(top, width=20, height=5)


text.bind('<KeyPress>', record)

text.pack(expand=True, fill=BOTH)

top.mainloop()