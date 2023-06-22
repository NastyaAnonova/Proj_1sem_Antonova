a = 7
b = 2
c = 8


def triangle_perimeter(a_side=a, b_side=b, c_side=c):
    '''Вычисляет переметр треугольника'''
    return a_side+b_side+c_side


def triangle_area(a_side=a, b_side=b, c_side=c):
    '''Вычисляет площадь треугольника'''
    p = (a_side + b_side + c_side) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5
