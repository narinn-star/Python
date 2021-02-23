def plus (a, b):
    return a - b

result = plus(b = 30, a = 1) #지정 가능, 순서 상관 X
print(result)

def say_hello(name, age):
    return f"Hello {name} you are {age} years old"
    #OR return "Hello" + name + " you are " + age + "years old"

hello = say_hello("Narin", "22")
#OR hello = say_hello(age = "22", name = "Narin")
print(hello)