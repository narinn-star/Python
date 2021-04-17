def mult3(lst):
    for i in lst:
        if i % 3 == 0:
            print(i)

lst = list(map(int,input("mult3 >> ").split()))

mult3(lst)