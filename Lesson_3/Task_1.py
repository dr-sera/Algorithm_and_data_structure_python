'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

res = [0] * 8
for i in range(2, 100):
    for j in range(2, 10):
        if i % j == 0:
            res[j-2] += 1
i = 0
while i < len(res):
    print(f'Элемент {i+2} кратен {res[i]} числам.')
    i += 1