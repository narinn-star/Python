def arithmetic(lst):
    lst = list(input("lists >> "))
    for i in range(len(lst)):
        if lst[i] % lst[0] == 0:
            print(True)
        else:
            print(False)

arithmetic([])