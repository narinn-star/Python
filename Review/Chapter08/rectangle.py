class Rectangle:
    
    def setSize(self, width, length):
        self.w = width
        self.l = length
    
    def perimeter(self):
        return self.w*2 + self.l*2
    
    def area(self):
        return self.w*self.l