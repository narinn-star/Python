#if문 _ 주민등록번호3

user = input("주민등록번호 : ")
one = int(user[0]) * 2 + int(user[1]) * 3 + int(user[2]) * 4 + int(user[3]) * 5 + int(user[4]) * 6 + \
        int(user[5]) * 7 + int(user[7]) * 8 + int(user[8]) * 9 + int(user[9]) * 2 + int(user[10])* 3 + \
        int(user[11])* 4 + int(user[12]) * 5 
two = 11 - (one % 11)
three = str(two)

if user[-1] == three[-1]:
    print("유효함")
else:
    print("유요하지 않음")