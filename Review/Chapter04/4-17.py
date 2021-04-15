#4-17(a)
message = 'The secret of this message is that it is secret.'
print(message)

#4-17(b)
length = len(message)
print(length)

#4-17(c)
count = message.count('secret')
print(count)

#4-17(d)
censored = message.replace('secret', 'xxxxxx')
print(censored)