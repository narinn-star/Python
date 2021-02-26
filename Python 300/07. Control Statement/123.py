#if문 _ 환율 계산

n = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171 }
user = input("입력 : ")
num, name = user.split()

print(float(num) * n[name], "원")