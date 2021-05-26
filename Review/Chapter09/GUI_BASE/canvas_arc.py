from tkinter import*

top = Tk()

cnvs=Canvas(top, width=300, height=200)
cnvs.pack()
cnvs.create_arc(10, 10, 200, 150, extent = 90, style=CHORD)
#create_arc : ARC, CHORD, PIESLICE 객체 생성 가능 
#             extent=359, 
#create_oval : 타원 생성

top.mainloop()