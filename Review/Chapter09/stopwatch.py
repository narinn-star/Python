from tkinter import*

top = Tk()
top.title("스톱 워치")

cnt = 0


def StopWatch():
    if running:
        global cnt
        cnt += 1
        lbl.config(text=str(cnt))
    top.after(1000, StopWatch)
    #1000밀리초(1초) 후에 함수 StopWatch를 재호출하여 카운터를 1초마다 증가


def start():
    global running  # 전역변수로 True 설정, 카운터 구동 시작
    running = True


def stop():
    global running  # 전역변수로 False 설정, 카운터 구동 멈춤
    running = False


def reset():
    global cnt  # 전역변수 cnt 0으로 초기화
    cnt = 0
    lbl.config(text=str(cnt))


lbl = Label(top, font=("Helvetica", 20), fg="red")
lbl.pack()

running = False
StopWatch()

bt1 = Button(top, text="Start", width=25, command=start).pack()
bt2 = Button(top, text="Stop", width=25, command=stop).pack()
bt3 = Button(top, text="Reset", width=25, command=reset).pack()

top.mainloop()