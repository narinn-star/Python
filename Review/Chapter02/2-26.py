import math

x = 0
y = 0
r = 10

#2-26(a)
x1 = 0
y1 = 0
if (math.sqrt((x-x1)**2 + (y-y1)**2) < r):
    print(True)
else:
    print(False)

#2-26(b)
x1 = 10
y1 = 10
if (math.sqrt((x-x1)**2 + (y-y1)**2) < r):
    print(True)
else:
    print(False)

#2-26(c)
x1 = 6
y1 = -6
if (math.sqrt((x-x1)**2 + (y-y1)**2) < r):
    print(True)
else:
    print(False)

#2-26(d)
x1 = -7
y1 = 8
if (math.sqrt((x-x1)**2 + (y-y1)**2) < r):
    print(True)
else:
    print(False)   