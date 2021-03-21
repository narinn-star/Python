#class _ 클래스 정의

class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price



myCar = car(2, 1000)
print(myCar.wheel)
print(myCar.price)