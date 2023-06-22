from math import pi

default_radius = 5


def circle_perimeter(radius=default_radius):
    '''Вычисляет периметр круга'''
    return 2 * pi * radius


def circle_area(radius=default_radius):
    '''Вычисляет площадь круга'''
    return pi * (radius ** 2)
