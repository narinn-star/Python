#for문 _ 문자열 자르기2

lists = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in lists:
    result = i.split(".")
    print(result[-1])