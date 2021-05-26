from tkinter import *

w = Tk()

Label(w, text="위쪽", width=10, relief=RAISED).pack()
Label(w, text="아래쪽",width=10, relief=RAISED).pack(side=BOTTOM)
Label(w, text="왼쪽",width=10, relief=RAISED).pack(side=LEFT)
Label(w,text="오른쪽", width=10, relief=RAISED).pack(side=LEFT)

w.mainloop()