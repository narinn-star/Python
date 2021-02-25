#input _ 과일

fruit = ["사과", "포도", "홍시"]

user = input("좋아하는 과일은? ")
if user in fruit:
    print("정답")
else:
    print("오답")