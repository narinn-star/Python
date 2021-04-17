def arithmetic(lst):
    lst = list(map(int,input("lists >> ").split()))
    if len(lst) < 2:
        return True

    d = lst[1]-lst[0]
    
    for i in range(1,len(lst)-1):
        if lst[i+1] - lst[i] != d:
            return False
    return True

print(arithmetic([]))