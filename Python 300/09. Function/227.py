#functions _ 함수 정의

def print_mxn(line, n):
    num = int(len(line)/n)
    for i in range(num + 1):
        print(line[i * n : i * n + n])

print_mxn("가나다라마바사아자차", 3)