from tkinter import*
from typing import Sized

top = Tk()

img = PhotoImage(file='dog.png')
label = Label(top, image=img)
label.pack(side=LEFT)

name = Label(top, text='\n이름 : 이나린')
name.pack(side=TOP)

gender = Label(top, text='성별 : 여')
gender.pack(side=TOP)

area = Label(top, text='출생지 : 울산광역시')
area.pack(side=TOP)

birth = Label(top, text='생년월일 : 00.05.16')
birth.pack(side=TOP)

top.mainloop()