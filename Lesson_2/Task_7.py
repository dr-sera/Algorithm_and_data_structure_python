'''
Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n — любое натуральное число.
'''

n = int(input('Введите целое число n: '))
sum_res = 0
for i in range(n+1):
    sum_res += i
right = n * (n + 1) // 2
print(f'Левая часть равенства: {sum_res}, правая чать равенства: {right}')
if sum_res == right:
    print('Равенство верное!')
else:
    print('Равенство не верное!')