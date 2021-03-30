lst = [3,4,5]

#2-28(a)
center = int(len(lst)/2)
print(lst.index(lst[center]))

#2-28(b)
print(lst[center])

#2-28(c)
lst.sort()
lst.reverse()
print(lst)

#2-28(d)
a = lst[0]
lst.remove(a)
lst.append(a)
print(lst)