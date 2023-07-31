# Задача № 4 с презентации Напишите программу, которая вычисляет
# площадь круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е. Точность вычислений должна
# составлять не менее 42 знаков после запятой.

from decimal import Decimal
import decimal
from math import pi
decimal.getcontext().prec = 42
PI = Decimal(pi)

def calc(diameter: Decimal) -> tuple[Decimal, Decimal]:
    return (PI * diameter,
            PI * (diameter / 2) ** 2)

diam = 0
while diam <= 0 or diam > 1000:
    diam = Decimal(input('Enter diameter: '))

length, square = calc(diam)
print(f'{length=}, {square=}')