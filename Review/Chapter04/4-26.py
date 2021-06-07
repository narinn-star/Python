def crypto(filename):
    infile = open(filename, 'r')
    content = infile.read()

    res = content.replace('secret', 'xxxxxx')

    print(res)

crypto('crypto.txt')