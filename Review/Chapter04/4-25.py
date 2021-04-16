def vowelCount(sentence):
    acount=0
    ecount=0
    icount=0
    ocount=0
    ucount=0
    for i in range(len(sentence)):
        if sentence[i] == 'a':
            acount = acount + 1
        elif sentence[i] == 'e':
            ecount = ecount + 1
        elif sentence[i] == 'i':
            icount = icount + 1
        elif sentence[i] == 'o':
            ocount = ocount + 1
        elif sentence[i] == 'u':
            ucount = ucount + 1
    print(f'a, e, i, o, and u appear, respectively, {acount}, {ecount}, {icount}, {ocount}, {ucount} times.')

vowelCount('Le Tour de France')
