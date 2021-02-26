#if문 _ 큰 수 찾기

number1 = input("number1 : ")
number2 = input("number2 : ")
number3 = input("number3 : ")

number1 = int(number1)
number2 = int(number2)
number3 = int(number3)

if number1 > number2 and number1 > number3:
    print(number1)
elif number2 > number1 and number2 > number3:
    print(number2)
else:
    print(number3)