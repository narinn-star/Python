#functions _ 실행 결과 예측

def f0(num) :
    return num * 2

def f1(num) :
    return f0(num + 2)

def f2(num) :
    num = num + 10
    return f1(num)

c = f2(2) #28
print(c) #28