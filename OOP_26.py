import math


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def display_sides(self):
        print(f'Длина первой стороны: {self.side1}')
        print(f'Длина второй стороны: {self.side2}')
        print(f'Длина третьей стороны: {self.side3}')

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_heights(self):
        p = self.calculate_perimeter()
        area = self.calculate_area()
        height1 = 2 * area / self.side1
        height2 = 2 * area / self.side2
        height3 = 2 * area / self.side3
        return height1, height2, height3

    @property
    def is_triangle(self):
        if self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and self.side2 + self.side3 > self.side1:
            return True
        else:
            return False


# Пример использования класса Triangle
triangle1 = Triangle(3, 5, 12)
triangle1.display_sides()
print(f'Это треугольник: {triangle1.is_triangle}')
print(f'Периметр: {triangle1.calculate_perimeter()}')
print(f'Площадь: {triangle1.calculate_area()}')
print(f'Высоты: {triangle1.calculate_heights()}')

