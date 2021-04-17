def intersect(lst1, lst2):
    res = []
    for i in lst1:
        for j in lst2:
            if i == j:
                res.append(i)
    print(res)

intersect([3,5,1,7,9], [4,2,6,3,9])