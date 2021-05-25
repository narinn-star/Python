from tkinter import *

w = Tk()
w.title("라디오 버튼")

def show():
    choice = str(v.get()) + ' 언어 선택함'
    lb2.config(text=choice)

v = StringVar()

lb1 = Label(w, text = "가장 선호하는 프로그래밍 언어 선택")
lb2 = Label(w)
lb1.pack(padx=10)

rb1 = Radiobutton(w, text ="Python", variable=v, value='Python',command=show)
rb1.pack(padx=20, anchor=W)
rb2 = Radiobutton(w, text="Java", variable=v, value='Java', command=show)
rb2.pack(padx=20, anchor=W)
rb3 = Radiobutton(w, text="C++", variable=v, value='C++', command=show)
rb3.pack(padx=20, anchor=W)

lb2.pack()

w.mainloop()