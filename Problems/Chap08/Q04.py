#리스트 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0

while A:
    idx = A.pop() # A 리스트의 가장 마지막 항목 뽑아내기
    if(idx >= 50):
        sum+= idx

print(sum)