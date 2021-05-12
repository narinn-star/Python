def h(n):
    print('Start h')
    print(1/n)
    print(n)

def g(n):
    print('Start g')
    try:
        h(n-1)
    except:
        print("Caught!")
    print(n)

def f(n):
    print('Start f')
    g(n-1)
    print(n)

f(2)

#7-04(a)
# 실행되지 않는 문장이 없음

#7-04(b)
# h() 마지막 문장 실행 X    g() 마지막 문장 실행 X

#7-04(c)
# h() 마지막 문장 실행 X