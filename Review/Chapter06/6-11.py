def easyCrypto(text):
    tmp = []
    res = ""
    for i in text:
        tmp.append(ord(i))

    for i in tmp:
        if i % 2 == 0:
            res += chr(i-1)
        else:
            res += chr(i+1)
    print(res)


easyCrypto('abc')
easyCrypto('ZOO')