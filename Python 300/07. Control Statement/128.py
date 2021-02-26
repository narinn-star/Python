#if문 _ 주민등록번호2

user = input("주민등록번호 : ")
front, back = user.split('-')

area = back[1:3]
if 0 <= int(area) <= 8:
    print("서울입니다.")
else:
    print("서울이 아님")