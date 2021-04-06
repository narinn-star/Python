import math

x = float(input("Enter x : "))
y = float(input("Enter y : "))

a = math.sqrt(x**2 + y**2)

if a <= 8:
    print("It is in !")
else:
    print("ERR")