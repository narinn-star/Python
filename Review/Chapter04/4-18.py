s = '''It was the best of times, it was the worst of times;
        it was the age of wisdom, it was the age of foolishness;
        it was the epoch of belief, it was the epoch of incredulity;
        it was ...'''

#4-18(a)
newS = s.replace(',', '')
newS = newS.replace('.', '')
newS = newS.replace(';', '')
newS = newS.replace('\n', '')
print(newS)

#4-18(b)
newS.strip()
print(newS)

#4-18(c)
newS = newS.lower()
print(newS)

#4-18(d)
count = newS.count('it was')
print(count)

#4-18(e)
newS = newS.replace('was', 'is')
print(newS)

#4-18(f)
listS = newS.split()
print(listS)