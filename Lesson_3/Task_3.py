'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
from random import random

s = int(input('Введите размер массива: '))
mas = []
for i in range(s):
    num = int(random()*10) + 1
    mas.append(num)
    i += 1
print(f'Ваш массив: {mas}')

mn = 0
mx = 0
for i in range(s):
    if mas[i] < mas[mn]:
        mn = i
    elif mas[i] > mas[mx]:
        mx = i
print(f'Минимальный элемент: {mn}, максимальный элемент: {mx}')
b = mas[mn]
mas[mn] = mas[mx]
mas[mx] = b

print(f'Результат обмена значениями: {mas}')
