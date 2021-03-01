#for문 _ 문자열 자르기3

lists = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in lists:
    if i.split(".")[-1] == 'h' or i.split(".")[-1] == 'c':
        print(i)