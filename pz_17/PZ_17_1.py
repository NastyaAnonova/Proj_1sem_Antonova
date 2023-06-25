# Создайте класс «Круг», который имеет атрибут радиуса и методы для вычисления 
# площади, длины окружности и диаметра.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def diameter(self):
        return 2 * self.radius

circle1 = Circle(5)
print("Площадь круга:", circle1.area())
print("Длина окружности:", circle1.circumference())
print("Диаметр круга:", circle1.diameter())
