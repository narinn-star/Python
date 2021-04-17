def four_letter(lst):
    res = []
    for i in lst:
        if len(i) == 4:
            res.append(i)
    print(res)

lst = ['dog', 'letter', 'stop', 'door', 'bus', 'dust']
four_letter(lst)