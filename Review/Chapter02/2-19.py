answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']

#2-19(a)
numYes = answers.count('Y')
print(numYes)

#2-19(b)
numNo = answers.count('N')
print(numNo)

#2-19(c)
percentYes = (numYes/len(answers)) * 100
print(percentYes)

#2-19(d)
answers.sort()
print(answers)

#2-19(e)
f = answers[6]
print(f)