import math

class Point:
    def setx(self, xcoord):
        self.x = xcoord
    
    def sety(self, ycoord):
        self.y = ycoord

    def get(self):
        return (self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

c = Point()
c.setx(0)
c.sety(1)
d = Point()
d.setx(1)
d.sety(0)
print(c.distance(d))
