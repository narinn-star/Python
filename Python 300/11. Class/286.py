#class _ 부모 클래스 생성자 호출

class car:
    def __init__(self, wheel, price):
        self.wheel = wheel
        self.price = price

    def info(self):
        print("바퀴수 ", self.wheel)
        print("가격 ", self.price) 

class bike(car):
    def __init__(self,wheel, price, 구동계):
        super().__init__(wheel, price) #car.__init__(self, wheel, price)
        self.구동계 = 구동계

class autocar(car):
    def __init__(self, wheel, price):
        super().__init__(wheel, price)
    
       

bicycle = bike(2, 100, "시마노")
bicycle.info()
