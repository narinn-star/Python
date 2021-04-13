def d2x(n,x):
    n = int(input("n 입력 >> "))
    x = int(input("x 입력 >> "))
    
    result = ""

    while n // x >= 1:
        remains = n % x
        n = n // x
        result = str(remains) + result
        if(n < x):
            result = str(n) + result

    print(result)

d2x(10, 2)
d2x(10, 3)
d2x(10, 8)
