text = 'all animals are equal but some animals are more equal than others'

def wordcount(text):
    res = text.split()
    counters = {}

    for word in res:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1

    for word in counters:
        if counters[word] == 1:
            print("{:8}appears {} time".format(word, counters[word]))
        else:
            print("{:8}appears {} time".format(word, counters[word]))

wordcount(text)