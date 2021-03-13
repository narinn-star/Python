#functions _ 함수 정의

def pickup_even(lists):
    even_list = []
    for i in lists:
        if i % 2 == 0:
            even_list.append(i)
    print(even_list)

pickup_even([3,4,5,6,7,8])
    