from tkinter import*

top = Tk()
top.title('라디오버튼과 체크버튼')

x1, y1, x2, y2 = 10, 10, 280, 90

def draw():
    cnvs.delete(ALL)
    if cv1.get() == 1:
        cnvs.create_rectangle(x1, y1, x2, y2)
        if cv4.get() == 1:
            cnvs.create_rectangle(x1, y1, x2, y2, fill='pink')
    if cv1.get() == 2:
        cnvs.create_oval(x1, y1, x2, y2)
        if cv4.get() == 1:
            cnvs.create_oval(x1, y1, x2, y2, fill='pink')
    if cv1.get() == 3:
        cnvs.create_line(x1, y1, x2, y2)
    
    

cnvs = Canvas(top, width=300, height=100, bg='white')
cnvs.pack()

frm = Frame(top)
frm.pack()

cv1, cv4 = IntVar(), IntVar()
rbt1 = Radiobutton(frm, text='직사각형', variable=cv1, value = 1, command=draw)
rbt2 = Radiobutton(frm, text='타 원', variable=cv1, value = 2,command=draw)
rbt3 = Radiobutton(frm, text='직 선', variable=cv1, value = 3,command=draw)
cbt4 = Checkbutton(frm, text='색채우기', variable=cv4, command=draw)

rbt1.pack(side=LEFT)
rbt2.pack(side=LEFT)
rbt3.pack(side=LEFT)
cbt4.pack(side=LEFT)

top.mainloop()