def interest(p):
    put = 100
    cnt = 0
    while put < 200:
        put += put * p
        cnt = cnt + 1
    print(cnt)

interest(0.07)