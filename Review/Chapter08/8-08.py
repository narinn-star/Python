class Vector:
    def __init__(self, xcoord = 0, ycoord = 0):
        self.x = xcoord
        self.y = ycoord
    
    def setx(self, xcoord):
        self.x = xcoord

    def sety(self, ycoord):
        self.y = ycoord
    
    def get(self):
        return (self.x, self.y)
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def __mul__(self, vec):
        return self.x * vec.x + self.y * vec.y

    def __add__(self, vec):
        return Vector(self.x+vec.x, self.y+vec.y)

    def __repr__(self):
        return 'Vector{}'.format(self.get())