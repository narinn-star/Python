def indexes(s, word):
    res = []
    for i in range(len(s)):
        if s[i] == word:
            res.append(i)
    print(res)

indexes('mississippi', 's')
indexes('mississippi', 'i')
indexes('mississippi', 'a')