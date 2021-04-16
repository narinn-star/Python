def powers(n):
    n = int(input("n 입력 >> "))
    for i in range(1,n+1):
        print(2**i,'', end='')

powers(6)