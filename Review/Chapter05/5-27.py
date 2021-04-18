def letter2number(score):
    res = 0
    if score[0] == 'A':
        res = 4
    elif score[0] == 'B':
        res = 3
    elif score[0] == 'C':
        res = 2
    elif score[0] == 'D':
        res = 1
    elif score[0] == 'F':
        res = 0
    if '+' in score:
        res += 0.3
    elif '-' in score:
        res -= 0.3
    else:
        res = res
    print(res)

letter2number('A-')
letter2number('B+')
letter2number('D')