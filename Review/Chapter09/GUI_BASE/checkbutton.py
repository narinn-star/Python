from tkinter import*

w = Tk()
w.title("체크 버튼")

def varState():
    print("var1: ", v1.get())
    print("var2: ", v2.get())
    print("var3: ", v3.get())

lb = Label(w, text = "선호하는 프로그래밍 언어 모두 선택 : ").pack(padx=10)

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()

cb1 = Checkbutton(w, text = "Python", variable=v1)
cb2 = Checkbutton(w, text = "Java", variable=v2)
cb3 = Checkbutton(w, text = "C++", variable=v3)
cb1.pack(padx=10, anchor=W) #왼쪽 정렬
cb2.pack(padx=10, anchor=W)
cb3.pack(padx=10, anchor=W)

bt = Button(w, text = "Show", command=varState)
bt.pack()

w.mainloop()
