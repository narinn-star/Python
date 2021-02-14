#DashInsert 함수 *
# 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 
# 홀수가 연속되면 두 수 사이에 -를 추가하고, 
# 짝수가 연속되면 두 수 사이에 *를 추가하는 기능
number = list(map(int,input("수 입력 : ")))
result = []

for i, num in enumerate(number):
    result.append(str(num))
    if i < len(number) -1:
        is_odd = num % 2 == 1
        is_next_odd = number[i+1] % 2 == 1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")

print("".join(result))
        
