#if문 _ 우편번호

user = input("우편번호 : ")
user = list(user)

if user[2] == '0' or user[2] == '1' or user [2] == '2':
    print("강북구")
elif user[2] == '3' or user[2] == '4' or user [2] == '5':
    print("도봉구")
else:
    print("노원구")  