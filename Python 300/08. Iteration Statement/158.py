#for문 _ 문자열 자르기

lists = ['hello.py', 'ex01.py', 'intro.hwp']

for i in lists:
    result = i.split(".")
    print(result[0])