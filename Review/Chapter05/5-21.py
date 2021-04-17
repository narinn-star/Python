def pair(lst1, lst2, n):
    for i in lst1:
        for j in lst2:
            if i+j == n:
                print(i,j)

pair([2,3,4],[5,7,9,12],9)