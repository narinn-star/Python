def myGrep(filename, word):
    infile=open(filename, 'r')
    for line in infile:
        if word in line:
            print(line, end='')

myGrep('example.txt', 'lines')