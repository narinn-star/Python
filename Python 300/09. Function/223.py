#functions _ 함수 정의

def print_even(lists):
    for i in lists:
        if i % 2 == 0:
            print(i)

print_even([1,3,2,10,12,11,15])