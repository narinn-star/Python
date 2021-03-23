import turtle
t = turtle.Pen()

#n = int(input("정수 n 입력 >> "))
n = len(input("정수 입력 >> "))

t.circle(n/2)
t.penup()
t.forward(n/2)
t.left(90)
t.pendown()

t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)
t.left(90)
t.forward(n)

# 정수의 길이를 n으로 받는 것인지, 정수 n을 받는 것인지
# 확실치 않아 두 가지 모두 작성하였습니다.

