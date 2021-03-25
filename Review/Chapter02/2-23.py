monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

#2-23(a)
monthsL.insert(3,'Apr')
#monthsT.insert(3,'Apr') #튜플 요소 변경 불가
print(monthsL, monthsT) 

#2-23(b)
monthsL.append('Jun')
#monthsT.append('Jun') #튜플 요소 변경 불가
print(monthsL, monthsT)

#2-23(c)
a = monthsL.pop()
print(a)
#b = monthsT.pop() # pop 기능 없음, 요소 변경 불가
print(monthsL, monthsT)

#2-23(d)
monthsL.remove('Feb')
#monthsT.remove('Feb') #튜플 요소 변경 불가
print(monthsL, monthsT)

#2-23(e)
monthsL.reverse()
#monthsT.reverse() #튜플 요소 변경 불가
print(monthsL, monthsT)

#2-23(f)
monthsL.sort()
#monthsT.sort() #튜플 요소 변경 불가
print(monthsL, monthsT)