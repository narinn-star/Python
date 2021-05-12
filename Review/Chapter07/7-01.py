def f(y):
    x = 2
    print("In f() : x = {}, y = {}".format(x,y))
    g(3)
    print("In f() : x = {}, y = {}".format(x,y))

def g(y):
    x = 4
    print("In g() : x = {}, y = {}".format(x,y))

f(1)