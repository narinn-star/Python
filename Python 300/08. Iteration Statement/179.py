#for문 _ 

my_list = [100, 200, 400, 800, 1000, 1300]

l = len(my_list)

for i in range(l-1):
    print((my_list[i-1]+my_list[i]+my_list[i+1])/3)