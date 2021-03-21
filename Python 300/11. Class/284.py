#class _ 클래스 상속

class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class bike(car):
    def __init__(self,wheel, price, 구동계):
        super().__init__(wheel, price) #car.__init__(self, wheel, price)
        self.구동계 = 구동계

bicycle = bike(2, 100, "시마노")
print(bicycle.구동계)
print(bicycle.wheel)