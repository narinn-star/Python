from tkinter import*

top = Tk()

oldx, oldy = 0, 0

def begin(event):
    global oldx, oldy
    oldx, oldy = event.x, event.y

def draw(event):
    global oldx, oldy, cnvs
    newx, newy = event.x, event.y
    cnvs.create_line(oldx, oldy, newx, newy)
    #create_line() : 여러 좌표들 사이를 직선으로 연결
    oldx, oldy = newx, newy

cnvs = Canvas(top, height=100, width=150)
cnvs.pack()

cnvs.bind('<Button-1>', begin)
cnvs.bind('<B1-Motion>', draw)

top.mainloop()