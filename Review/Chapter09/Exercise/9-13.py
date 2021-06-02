from tkinter import*

top = Tk()

def up(event):
    global y, canvas
    canvas.create_line(x, y, x, y-10)
    y -= 10


x, y = 50, 75 #펜 위치, 중앙으로 초기화

canvas = Canvas(top, height=100, width=150, relief=SUNKEN, borderwidth=3)
canvas.pack(side=LEFT)
canvas.focus_set()

canvas.bind("<Up>", up)

top.mainloop()