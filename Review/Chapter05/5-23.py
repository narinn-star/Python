def pay(p, h):
    res = 0
    if h <= 40:
        res = p*h
    elif h <= 60:
        res = (p * 40) + (p * (h-40) * 1.5)
    elif h > 60:
        res = (p * 40) + (p * (h-40) * 2)
    print(res)

pay(10,35)
pay(10,45)
pay(10,61)