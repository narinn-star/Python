import random

def guess(n):
    rand = random.randrange(0,n)
    #print(rand)
    while(True):
        user = int(input("Enter your guess : "))
        if rand > user:
            print("Too low.")
        elif rand < user:
            print("Too high.")
        elif rand == user:
            print("You got it!")
            break

n = int(input("n : "))
guess(n)