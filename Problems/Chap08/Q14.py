#문자열 압축하기
#문자열을 입력받아 같은 문자가 연속적으로 반복되는 경우,
#그 반복 횟수를 표시

ch = list(input("문자열 입력 : "))
result = []
count = 1
for i in range(0,len(ch)):
    
    if i == len(ch) -1:
        result.append(ch[i])
        result.append(str(count))
    else:
        if ch[i] == ch[i+1]:
            count += 1
        else:
            result.append(ch[i])
            result.append(str(count))
            count = 1

for s in result:   
    print(s, end = "")
