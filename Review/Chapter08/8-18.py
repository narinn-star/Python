class myList(list):
    def sort(self):
        print('You wish ...')

x = myList([1, 2, 3])
print(x)
x.reverse()
print(x)
print(x[2])
x.sort()