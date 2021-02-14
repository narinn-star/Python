#Duplicate Numbers
# 0~9의 문자로 된 숫자를 입력받았을 때, 
# 이 입력값이 0~9의 모든 숫자를 각각 한 번씩만 사용한 것인지 확인

def Duplicate(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(Duplicate("0123456789"))      # True 리턴
print(Duplicate("01234"))           # False 리턴
print(Duplicate("01234567890"))     # False 리턴
print(Duplicate("6789012345"))      # True 리턴
print(Duplicate("012322456789"))    # False 리턴