from tkinter import*

class Key(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.pack()

        # self.text = Text(self, width=20, height=5)
        # self.text.bind("<KeyPress>", self.record)
        # self.text.pack(expand=True, fill=BOTH)
        # Text 위젯은 이벤트 핸들러에서 사용되지 않으므로
        # 인스턴스 변수에 저장하지 않아도 된다.

        text = Text(self, width=20, height=5)
        text.bind("<KeyPress>", self.record)
        text.pack(expand=True, fill=BOTH)

    def record(self, event):
        print('char = {}'.format(event.keysym))

top = Tk()
key = Key(top)
key.pack()

top.mainloop()