lst = [2,3,4]
lst.extend([5,6])
print(lst)

lst2 = lst.copy()
print(lst2)

lst.clear()
print(lst)
print(lst2)