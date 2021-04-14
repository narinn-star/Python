import math

def hit(x1, y1, r1, x2, y2):
    if math.sqrt((x1+x2)**2 + (y1+y2)**2) <= r1:
        print(True)
    else:
        print(False)

hit(0,0,3,3,0)
hit(0,0,3,4,0)