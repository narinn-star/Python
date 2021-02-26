#if문 _ 통신사

user = input("휴대전화 번호 입력 : ")
front, center, back = user.split('-')

if front == '011':
    print("SKT 사용자")
elif front == '016':
    print("KT 사용자")
elif front == '019':
    print("LGU 사용자")
else:
    print("알수없음")