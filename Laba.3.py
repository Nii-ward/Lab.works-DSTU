#Task num 1
x = float(input("Задача №1: Укажите радиус окружности: "))

from math import*
S = x**2 * (pi - 1)
print(S)

#Task num 2

Spis = []

for i in range(4):
    Spis.append(float(input('Введите число: ')))

Min_spis = min(Spis)
#print(Spis.index(Min_spis)+1)