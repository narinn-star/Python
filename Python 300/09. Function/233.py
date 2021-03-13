#functions _ 함수 정의

def make_list(string):
    my_list = []
    for i in string:
        my_list.append(i)
    print(my_list)

make_list("abcd")