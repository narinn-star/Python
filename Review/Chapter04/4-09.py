def words(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    table = str.maketrans('!,.:;?', 6*' ')
    content=content.translate(table)
    content=content.lower()

    print(content.split())

words('example.txt')