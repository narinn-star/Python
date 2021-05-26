from tkinter import*

top = Tk()
top.title("tk #3")


cat = PhotoImage(file="cat.png")

lb1 = Label(top, text="Peace & Love", bg="black", fg="white",
                width=20, height=5, font=('Helvetica', 18, 'italic')).pack(side=LEFT)
lb2 = Label(top, image=cat).pack(side=RIGHT, expand=True, fill=BOTH)
#expand : 내부의 빈 공간을 채우기 위해 위젯을 확장시킬 것인가를 명시, 디폴트 : False
#fill : 내부에서 위젯이 확장될 가로 또는 세로 방향을 명시, 디폴트 : default

top.mainloop()