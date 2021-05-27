from tkinter import*

top = Tk()
top.title('체크버튼')

x1, y1, x2, y2 = 10, 10, 280, 90

def draw():
    cnvs.delete(ALL)
    if cv1.get() == 1:
        cnvs.create_rectangle(x1, y1, x2, y2)
    if cv2.get() == 1:
        cnvs.create_oval(x1, y1, x2, y2)
    if cv3.get() == 1:
        cnvs.create_line(x1, y1, x2, y2)
    

cnvs = Canvas(top, width=300, height=100, bg='white')
cnvs.pack()

frm = Frame(top)
frm.pack()

cv1, cv2, cv3 = IntVar(), IntVar(),IntVar()
cbt1 = Checkbutton(frm, text='직사각형', variable=cv1, command=draw)
cbt2 = Checkbutton(frm, text='타 원', variable=cv2, command=draw)
cbt3 = Checkbutton(frm, text='직 선', variable=cv3, command=draw)

cbt1.pack(side=LEFT)
cbt2.pack(side=LEFT)
cbt3.pack(side=LEFT)

top.mainloop()