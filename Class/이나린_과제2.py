number = 990516
year = 1900 + (number // 10000)
month = (number % 10000) // 100
day = ((number % 10000) % 100) // 1
print("주민번호 = " , number)
print("생년월일 = " , year , " 년 " , month , " 월 " , day , " 일")
