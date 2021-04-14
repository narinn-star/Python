def avg(num):
    for i in range(len(num)):
        sum = 0
        for j in range(len(num[i])):
            sum += num[i][j]
        print(sum / len(num[i]))

avg([[95,92,86,87],[66,54],[89,72,100],[33, 0, 0]])