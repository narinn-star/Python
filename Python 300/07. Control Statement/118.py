#input _ invest

warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

user = input("종목명 : ")
if user in warn_investment_list:
    print("투자 경고 종목이 맞음")
else:
    print("투자 경고 종목이 아님")
