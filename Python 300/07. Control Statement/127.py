#if문 _ 주민등록번호1

user = input("주민등록번호 : ")
front, back = user.split('-')
back = list(back)
gender = back[0]

if gender in ["1", "3"]:
    print("남자")
elif gender in ["2", "4"]:
    print("여자")
else:
    print("잘못된 주민등록번호")