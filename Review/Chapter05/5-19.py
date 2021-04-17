def inBoth(lst1, lst2):
    a = False
    for i in lst1:
        for j in lst2:
            if i == j:
                a = True
    print(a)

inBoth([3,2,5,4,7],[9,0,1,3])