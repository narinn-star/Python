#class _ 인스턴스 접근

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("조아름", 25, "여자")
print("이름 : ", areum.name, " 나이 : ", areum.age, " 성별 : ", areum.gender)