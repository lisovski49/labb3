class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def check_triangle_existence(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
            return True
        return False

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    def calculate_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter



triangle = Triangle(3, 4, 5)
if triangle.check_triangle_existence():
    area = triangle.calculate_area()
    perimeter = triangle.calculate_perimeter()
    print("Площадь треугольника:", area)
    print("Периметр треугольника:", perimeter)
else:
    print("Треугольник с такими сторонами не существует.")