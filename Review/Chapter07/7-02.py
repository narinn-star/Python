def f(y):                                   #f는 전역, y는 f()에 지역
    x = 2                                   #x는 f()에 지역
    return g(x)                             #g는 전역, x는 f()에 지역

def g(y):                                   #g는 전역, y는 g()에 지역
    global x                                #x 전역
    x = 4                                   #x 전역
    return x*y                              #x는 전역, y는 g()에 지역

x = 0                                       #x 전역
res = f(x)                                  #res, x, f 모두 전역
print("x = {}, f(0) = {}".format(x, res))   #res, x, f 모두 전역