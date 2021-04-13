def avg(num):
    sum = 0
    for i in range(len(num)):
        for j in range(len(num[i])):
            sum += num[i][j]
        print(sum / len(num[i]))

avg([[95,92,86,87],[66,54],[89,72,100]])