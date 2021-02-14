#오류와 예외 처리

result = 0

try:
    [1,2,3][3] # IndexError => TypeError와 ZeroDivisionError는 걸리지 않게 됨
    "a"+1
    4/0
except TypeError:
    result += 1
except ZeroDivisionError:
    result += 2
except IndexError: #실행
    result += 3
finally:            #실행
    result += 4

print(result) #result 값은 => 3 + 4 = 7