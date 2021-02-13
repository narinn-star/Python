#한 줄 구구단

number = input("구구단을 출력할 숫자를 입력하세요(2~9) : ")
numbers = int(number)

for n in range(1,9):
    print(numbers* n, end=' ')
