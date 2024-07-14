

import math
def discriminant(a, b, c):
    """Функция для вычисления дискриминанта"""
    global d
    d = b**2 - 4 * a * c
    return (d)
def solve(a, b, c):
    """Функция, которая вычисляет корни квадратного уравнения"""
    discriminant(a, b, c)
    if d > 0:
        x1 = int((-b - math.sqrt(d)) / (2 * a))
        x2 = int((-b + math.sqrt(d)) / (2 * a))
        return f' Дискриминант имеет 2 корня, x1 = {x1}, x2 = {x2}'

    elif d == 0:
        x = -b / 2 * a
        return f'Дискриминант имеет только один корень, x=  {x}'
    else:
        return 'Решений нет'
print(solve(1, 2, 1))
print(solve(2, 5, 3))
print(solve(1, -1, 3))

