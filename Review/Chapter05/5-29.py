def lastfirst(lst):
    first = []
    last = []
    for i in range(len(lst)):
        first.append(lst[i].split(', ')[1])
        last.append(lst[i].split(', ')[0])

    print(first, last)
lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob'])
        