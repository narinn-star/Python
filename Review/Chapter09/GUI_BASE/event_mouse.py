from tkinter import *

top = Tk()
top.title("이벤트 처리")

def mleft(event):
    print(event.x, event.y, '에서 마우스 클릭')

def mright(event):
    print('Right Button, 끝내기')
    import sys; sys.exit()

fr=Frame(top, width=240, height=100)
fr.bind("<Button-1>", mleft)
fr.bind("<Button-3>", mright)
# <Button> : 마우스 버튼이 위젯에서 클릭될 때, 1은 left 2는 middle, 3은 right
fr.pack()

top.mainloop()