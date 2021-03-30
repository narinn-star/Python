import math

def points(x1,y1,x2,y2):
    if x1 == x2 == 0 or y1 == y2 == 0:
        slope = "infinity"
    else: 
        slope = (y2-y1) / (x2-x1)
        
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    slope = str(slope)
    distance = str(distance)
    
    print(f"The slope is {slope} and the distance is {distance}")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

points(x1, y1, x2, y2)
