from tkinter import*

top = Tk()

cnvs=Canvas(top, width=300, height=200)
cnvs.pack()

cnvs.create_polygon(10, 10, 10, 200, 250, 10, fill='blue') 
                    #세 점의 좌표 (x1, y1, x2, y2, x3, y3)

top.mainloop()