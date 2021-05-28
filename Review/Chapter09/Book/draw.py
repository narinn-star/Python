from tkinter import*

top = Tk()

def begin(event):
    global oldx, oldy
    oldx, oldy = event.x, event.y

def draw(event):
    global oldx, oldy, canvas
    newx, newy = event.x, event.y

    canvas.create_line(oldx, oldy, newx, newy)

    oldx, oldy = newx, newy


canvas = Canvas(top, height=100, width=150)

canvas.bind("<Button-1>", begin)
canvas.bind("<Button1-Motion>", draw)

canvas.pack()
canvas.mainloop()