#functions _ 함수 정의

def print_5xn(string):
    num = int(len(string) / 5)
    for i in range(num + 1):
        print(string[i * 5 : i * 5 + 5])

print_5xn("가나다라마바사아자차")