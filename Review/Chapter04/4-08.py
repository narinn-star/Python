def stringCount(filename, word):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    print(content)
    print(content.count(word))
    # wordList = content.split()
    # count = 0

    # for w in wordList:
    #     if w == word:
    #         count += 1

    # print(count)

stringCount('example.txt', 'line')