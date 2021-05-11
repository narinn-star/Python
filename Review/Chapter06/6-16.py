mult3 = set()
mult5 = set()
mult7 = set()

for i in range(1, 101):
    if i % 3 == 0:
        mult3.add(i)
    if i % 5 == 0:
        mult5.add(i)
    if i % 7 == 0:
        mult7.add(i)

mult = mult3 | mult5 | mult7

#6-16(a)
print(mult5&mult7)

#6-16(b)
print(mult3&mult5&mult7)

#6-16(c)
print(mult3|mult7)

#6-16(d)
print(mult-(mult3&mult7))

#6-16(e)
print(mult7-mult3)
