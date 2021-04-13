#세자리 정수
def reverse_int(a):
    if a <= 0:
        return
    print(a%10, end = '')
    reverse_int(a//10)
    
reverse_int(123)
print()
reverse_int(908)
