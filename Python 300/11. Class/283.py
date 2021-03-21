#class _ 클래스 상속

class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class bike(car):
    def __init__(self,wheel, price):
        super().__init__(wheel, price) #car.__init__(self, wheel, price)

bicycle = bike(2,100)
print(bicycle.price)