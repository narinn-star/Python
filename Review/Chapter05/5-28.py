def geometric(lst):
    if len(lst) < 2:
        return True
    r = lst[1] - lst[0]
    for i in range(0,len(lst)-1):
        if lst[i+1] / lst[i] != r:
            return False
    return True

print(geometric([2,4,8,16,32,64,128,256]))
print(geometric([2,4,6,8]))