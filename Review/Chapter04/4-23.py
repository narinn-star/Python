def average():
    s = input("Enter a sentence : ")
    res = s.split()
    sum = 0
    for i in range(len(res)):
        sum += len(res[i])
    
    print(sum / len(res))

average()