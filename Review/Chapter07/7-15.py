

#7-15(a)
#a = 'error'.upper()
a = str.upper('error')
print(a)

#7-15(b)
#a = '2, 3, 4, 5'.split(',')
a = str.split('2, 3, 4, 5', ',')
print(a)

#7-15(c)
#a = 'mississippi'.count('i')
a = str.count('mississippi', 'i')
print(a)

#7-15(d)
#a = 'bell'.replace('e', 'a')
a = str.replace('bell', 'e', 'a')
print(a)

#7-15(e)
#a = ' '.format(1, 2, 3)
a = str.format(' ', 1, 2, 3)
print(a)