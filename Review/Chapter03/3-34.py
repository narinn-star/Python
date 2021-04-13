def pay(a, b):
    if(b > 40):
        c = b-40
        print(a*40 + c*1.5*10)
    else:
        print(a*b)

pay(10, 35)
pay(10, 45)