class Test:
    version = 1.02

a = Test()
b = Test()

print(a.version)
print(b.version)
print(Test.version)
Test.version = 1.03
print(a.version)
print(Test.version)
a.version = 'Latest!!'
print(Test.version)
print(b.version)
print(a.version)