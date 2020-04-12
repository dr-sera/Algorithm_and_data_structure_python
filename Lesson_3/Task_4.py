'''
Определить, какое число в массиве встречается чаще всего.
'''
from random import random

S = int(input('Введите размер массива: '))
mas = []
mas_res = []
for i in range(S):
    num = int(input(f'Введите {i+1} число массива: '))
    mas.append(num)
    i += 1
print(f'Ваш массив: {mas}')

# Вариант с автоматическим заполнением
# S = 10
# mas = []
# mas_res = []
# for i in range(S):
#     num = int(random() * 20)
#     mas.append(num)
# print(f'Ваш массив: {mas}')

num = mas[0]
max_count = 1
for el in mas:
    count = 1
    for i in range(el+1, S):
        if mas[el] == mas[i]:
            count += 1
    if max_count < count:
        max_count = count
        num = mas[el]

if max_count > 1:
    print(f'В массиве {max_count} раз(a) встречается число {num}.')
else:
    print(f'Все числа массива уникальны!')


