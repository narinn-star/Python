import math

def collision(r1, x1, y1, r2, x2, y2):
    if math.sqrt((x1-x2)**2 + (y1-y2)**2) < r1+ r2:
        print(True)
    else:
        print(False)

collision(3, 0, 0, 3, 0, 5)

collision(1.4, 0, 0, 1.4, 2, 2)