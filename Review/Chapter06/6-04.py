text = 'all animals are equal but some animals are more equal than others'

def wordCount(text):
    text = text.split()
    count = {}
    for word in text:
        if word in count:
            count[word] += 1
            print("{:8}appears {} times.".format(word, count[word]))
        else:
            count[word] = 1
            print("{:8}appears {} time.".format(word, count[word]))

wordCount(text)