def divisor(n):
    n = int(input("n 입력 >> "))
    lst = []
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    print(lst)

divisor(1)
divisor(6)
divisor(11)