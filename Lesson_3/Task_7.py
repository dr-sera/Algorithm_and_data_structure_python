'''
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба
являться минимальными), так и различаться.
'''
from random import random

# Вариант с автоматическим заполнением
S = 10
mas = []
mas_res = []
for i in range(S):
    num = int(random() * 20)
    mas.append(num)
print(f'Ваш массив: {mas}')

# S = int(input('Введите размер массива: '))
# mas = []
# mas_res = []
# for i in range(S):
#     num = int(input(f'Введите {i+1} число массива: '))
#     mas.append(num)
#     i += 1
# print(f'Ваш массив: {mas}')

# min_1 = 0
# min_2 = 1
# for el in range(S):
#     if mas[el] < mas[min_1]:
#         min_1 = el
# print(f'Минимальное число 1: {min_1}, минимальное число 2: ')

if mas[0] > mas[1]:
    min_1 = 0
    min_2 = 1
else:
    min_1 = 1
    min_2 = 0

for i in range(2, S):
    if mas[i] < mas[min_1]:
        b = min_1
        min_1 = i
        if mas[b] < mas[min_2]:
            min_2 = b
    elif mas[i] < mas[min_2]:
        min_2 = i

print(f'Первое минимальное значение равно: {mas[min_1]}, оно находится на {min_1+1}-й позиции')
print(f'Второе минимальное значение равно: {mas[min_2]}, оно находится на {min_2+1}-й позиции')
