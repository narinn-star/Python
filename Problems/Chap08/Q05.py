#피보나치 함수 *
number = input("숫자 입력 : ")
n = int(number)
print(n)

def fib(n):
    if n == 0 : return 0          # n이 0일 때는 0을 반환
    if n == 1 : return 1          # n이 1일 때는 1을 반환
    return fib(n-2) + fib(n-1)    # n이 2 이상일 때는 그 이전의 두 값을 더하여 반환

for i in range(0,n):
    print(fib(i))

#input 함수는 리턴값이 문자열