import random

def coins():
    res = random.randint(1,2)
    if res == 1:
        print("Heads")
        print(res)
    else:
        print("Tails")
        print(res)

coins()