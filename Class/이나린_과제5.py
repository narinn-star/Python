for i in range(1,6):
    for j in range(5-i):
        print(" ", end = '')
    for k in range(2*i-1):
        print("*", end = '')
    print()

import turtle
t = turtle.Pen()
#t.hideturtle()

for i in range(0,5):
    for j in range(0,5):
        t.forward(80)
        t.left(72)
    t.left(72)
