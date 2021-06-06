class myInt(int):

    def __init__(self, x):
        int(x)

    def __add__(self, other):
        print("'Whatever ...'")


x = myInt(5)
print(x * 4)
print(x * (4 + 6))
x+6