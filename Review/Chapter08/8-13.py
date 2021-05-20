class Rectangle:
    def __init__(self, width = 1, length = 1):
        self.w = width
        self.l = length

    def setSize(self, width, length):
        self.w = width
        self.l = length
    
    def perimeter(self):
        return self.w*2 + self.l*2
    
    def area(self):
        return self.w*self.l

rectangle1 = Rectangle(2,4)
print(rectangle1.perimeter())

rectangle2 = Rectangle()
print(rectangle2.area())