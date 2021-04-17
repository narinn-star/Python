def pairSum(lst, n):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == n:
                print(i, j)

pairSum([7,8,5,3,4,6], 11)