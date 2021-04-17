def xmult(lst1, lst2):
    res = []
    for i in range(len(lst1)):
        for j in range(len(lst2)):
            res.append(lst1[i]*lst2[j])
    print(res)

xmult([2],[1,5])
xmult([2,3],[1,5])
xmult([3,4,1],[2,0])