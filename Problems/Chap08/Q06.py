#숫자의 총합 구하기
n = input("숫자 입력(콤마로 구분하여 입력) : ")
num = n.split(",")
print(num)
sum = 0

for n in num:
    sum += int(n)

print(sum)