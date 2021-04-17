lst = [3,0,1,2,3,6,2,4,5,6,5]

def doubles(lst):
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1]*2:
            print(lst[i])

doubles(lst)