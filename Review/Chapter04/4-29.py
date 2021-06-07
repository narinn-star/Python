def stats(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    lcnt = 0
    for w in content:
        if '\n' == w:
            lcnt+= 1
    print("line count : ", lcnt)

    wordList = content.split()
    print("word count : ", len(wordList))
    
    ccnt = 0
    for w in content:
        ccnt += 1
    print("character count : ", ccnt)

stats('example.txt')