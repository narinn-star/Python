def fcopy(filename, copyname):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    newfile = open(copyname, 'w')
    newfile.write(content)
    newfile.close()

fcopy('example.txt', 'output.txt')
print(open('output.txt').read())