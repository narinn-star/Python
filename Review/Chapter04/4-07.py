import time
t = time.localtime(1500000000)

#4-07(a)
a = time.strftime('%A, %B %d %Y', time.localtime())
print(a)

#4-07(b)
b = time.strftime('%H:%M %p Cntral Daylight Time on %m/%d/%Y',time.localtime())
print(b)

#4-07(c)
c = time.strftime('I will meet you on %b %B %d at %m:%M %p.', time.localtime())
print(c)