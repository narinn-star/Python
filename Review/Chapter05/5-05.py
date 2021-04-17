def acronym(s):
    ns = s.split()
    res = ''
    for i in range(len(ns)):
        res += ns[i][0]
    res = res.upper()
    print(res)

acronym('Random access memory')
acronym('central processing unit')