# print(f(3))

# def f():
#     return 2 * x + 1
# => 문제점 : f를 호출하기 전에 함수 f()가 선언되어 있어야함.
# 
def g(x):
    print(f(x))

def f(x):
    return 2*x+1

g(3) 

#위와 같이 함수는 순서 상관 없음.