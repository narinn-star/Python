#class _ 클래스 상속

class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

class bike(car):
    def __init__(self,wheel, price, 구동계):
        super().__init__(wheel, price) #car.__init__(self, wheel, price)
        self.구동계 = 구동계

class autocar(car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)
    
    def info(self):
        print("바퀴수 ", self.wheel)
        print("가격 ", self.price)    

myCar = autocar(4,1000)
myCar.info()