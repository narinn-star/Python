#functions _ 실행 결과 예측

def f1(num) :
    return num + 4

def f2(num) :
    num = num + 2
    return f1(num)

c = f2(10) #16
print(c) #16