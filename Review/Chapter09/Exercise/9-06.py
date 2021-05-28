from tkinter import*

top = Tk()

def begin(event):
    global oldx, oldy, curve
    oldx, oldy = event.x, event.y
    curve = []

def draw(event):
    global oldx, oldy, canvas, curve
    newx, newy = event.x, event.y
    
    curve.append(canvas.create_line(oldx, oldy, newx, newy))

    oldx, oldy = newx, newy

def delete(event):
    global curve
    for segment in curve:
        canvas.delete(segment)



canvas = Canvas(top, height=100, width=150)

canvas.bind("<Button-1>", begin)
canvas.bind("<Button1-Motion>", draw)
canvas.bind("<Control-Button-1>", delete)

canvas.pack()
canvas.mainloop()