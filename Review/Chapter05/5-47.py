#n을 x진법으로 바꾸기 => 문자열로 반환
def d2x(n, x):
    n = int(input("n 입력 >> "))
    x = int(input("x 입력 >> "))

    answer  = ""
    while n // x >= 1:
        remain = n % x
        n = n // x
        answer = str(remain) + answer
        if n < x:
            answer = str(n) +answer
    
    print(answer)

d2x(10, 2)