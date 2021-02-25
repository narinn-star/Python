#input _ 계산

num = input("입력값 : ")
result = int(num) - 20

if result < 0:
    print(0)
elif result > 255:
    print(255)
else:
    print(result)