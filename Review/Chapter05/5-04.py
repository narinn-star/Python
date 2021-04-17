def factorial(n):
    res = 1
    if n < 0:
        return False
    else:
        if n == 0:
            res = 1
        else:
            for i in range(1, n+1):
                res *= i 
    print(res)


factorial(0)
factorial(3)
factorial(5)