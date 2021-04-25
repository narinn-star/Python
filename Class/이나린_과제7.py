import random

user = input("(가위,바위,보)중 하나 선택 >> ")

com = random.choice(['가위', '바위', '보'])
print("컴퓨터 선택 >> ", com)

if user == '가위':
    if com == '보':
        print("유저 승, 컴퓨터 패")
    elif com == '바위':
        print("유저 패, 컴퓨터 승")
    else:
        print("비겼습니다.")
elif user == '바위':
    if com == '가위':
        print("유저 승, 컴퓨터 패")
    elif com == '보':
        print("유저 패, 컴퓨터 승")
    else:
        print("비겼습니다.")
elif user == '보':
    if com == '바위':
        print("유저 승, 컴퓨터 패")
    elif com == '가위':
        print("유저 패, 컴퓨터 승")
    else:
        print("비겼습니다.")