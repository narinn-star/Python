#class _ 클래스 소멸자

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("소멸되었습니다.")
    
    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.gender}")

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")
del(areum)