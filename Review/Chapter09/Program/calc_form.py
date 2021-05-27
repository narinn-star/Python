from tkinter import*

top = Tk()
top.title("Calculator")

Entry(top, width= 30, bg='skyblue').grid(row=0, column=0, columnspan=5)

lst=[['7','8','8','/','C'],
     ['4','5','6','*','('],
     ['1','2','3','-',')'],
     ['0','.','=','+',' ']]

for r in range(1,5):
    for c in range(5):
        Button(top, text=lst[r-1][c], width=5).grid(row=r, column=c)

top.mainloop()

