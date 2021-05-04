import random

def approxPi(n):
    count = 0
    for i in range(n):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if (x**2)+(y**2) <= 1:
            count += 1
    return 4*count / n

print(approxPi(1000))
print(approxPi(100000))
print(approxPi(1000000))