#arguments = 인자
def say_hello(who): #무한대의 인자 가질 수 있음
    print("hello", who)

say_hello("Narin")

def plus(a, b):
    print(a + b)

def minus(a, b = 0): #디폴트 매개변수 둘 수 있음
    print(a - b)

plus(2, 5)
minus(2)