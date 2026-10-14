#Task num 1
from math import*

x = float(input("Задача №1: Укажите радиус окружности: "))
S = x**2 * (pi - 1)
print(S)

#Task num 2
print("Задание №2")

Spis = []

for i in range(4):
    Spis.append(float(input(f'Введите число №{i+1}: ')))

if len(set(Spis)) == 1:
    print("Список состоит из равных чисел")
else:
    Min_spis = min(Spis)
    for _ in range(len(Spis)):
        if Spis[_] == Min_spis:
            print('Номер элемента: ',_+1)
