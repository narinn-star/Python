def char(low, high):
    for i in range(low, high+1):
        print(i, " : ", chr(i))

low = int(input("low : "))
high = int(input("high : "))

char(low, high)