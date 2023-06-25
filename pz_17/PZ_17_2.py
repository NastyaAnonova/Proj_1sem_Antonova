# Создайте класс "Фигура", который содержит метод расчета площади фигуры. 
# Создайте классы "Квадрат" и "Прямоугольник", которые наследуются от класса 
# "Фигура". Каждый класс должен иметь метод расчета площади собственной фигуры.

class Figure:
    def area(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

square1 = Square(5)
print("Площадь квадрата:", square1.area())

rectangle1 = Rectangle(4, 6)
print("Площадь прямоугольника:", rectangle1.area())
