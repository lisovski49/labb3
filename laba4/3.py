import math

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        area=math.pi*self.radius**2
        return area
class Square:
    def __init__(self,side):
        self.side=side

    def calculate_area(self):
        area=self.side**2
        return area
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        area=self.length*self.width
        return area

circle = Circle(5)
square = Square(4)
rectangle = Rectangle(3, 6)

circle_area=circle.calculate_area()
square_area=square.calculate_area()
rectangle_area=rectangle.calculate_area()

print("Площадь круга:", circle_area)
print("Площадь квадрата:", square_area)
print("Площадь прямоугольника:", rectangle_area)