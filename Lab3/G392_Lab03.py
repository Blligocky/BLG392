# Import necessary libraries 
from math import * 

# Open and read file 
file = open(r"Shape.txt")
lines = file.readlines()
file.close()

# Create class shape (parent class)
class Shape():
    def __init__(self):
        pass
    def getArea(self):
        pass


# Create classes for each shape possiblity 
class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w
    def getArea(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self, r):
        super().__init__()
        self.r = r
    def getArea(self):
        return (self.r**2) * pi 

class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__()
        self.b = b
        self.h = h
    def getArea(self):
        return self.b * self.h * .5

# Empty list to collect answers
totalShapes = [] 

# Call definitions 
for line in lines:
    components = line.split(",")
    shape = components[0] 

    if shape == "Rectangle":
        x = float(components[1])
        y = float(components[2])
        totalShapes.append(Rectangle(x,y))
    elif shape == "Circle":
        x = float(components[1])
        totalShapes.append(Circle(x))
    elif shape == "Triangle":
        x = float(components[1])
        y = float(components[2])
        totalShapes.append(Triangle(x,y))
    else:
        pass

# Print output list
for shape in totalShapes:
    print(shape.getArea())