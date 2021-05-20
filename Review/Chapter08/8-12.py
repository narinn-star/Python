class Point:
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

    def up(self):
        self.move(0, 1)
    
    def down(self):
        self.move(0, -1)
    
    def left(self):
        self.move(-1, 0)

    def right(self):
        self.move(1, 0)

a = Point(3,4)
a.left()
print(a.get())