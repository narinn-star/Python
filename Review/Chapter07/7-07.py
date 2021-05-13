def h(n):
    print('Strat h')
    print(1/n)
    print(n)

def g(n):
    print('Start g')
    h(n-1)
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)

#Q. f(1) 실행 설명, 스택 상태 그리기
f(1)