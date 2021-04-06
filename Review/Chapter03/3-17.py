#3-17(a)
print(eval('2 * 3 + 1'))

#3-17(b)
#print(eval('hello'))

#3-17(c)
print(eval("'hello' + ' ' + 'world!'"))

#3-17(d)
print(eval("'ASCII'.count('I')"))

#3-17(e)
#print(eval('x=5'))

#오류가 나는 것은 b와 e이다. 
#그 이유는 수식으로 간주하여 계산하는 것인데 hello도, x=5도 수식으로 변환될 수 없기 때문이다.