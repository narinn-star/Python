def bubblesort(lst):
    for i in range(len(lst)):
        for j in range(1,len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]

lst = [3,1,7,9,2,5]
bubblesort(lst)
print(lst)