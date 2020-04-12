'''
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его
цифр.
'''


def sum_calc(number):
    if number < 10:
        return number
    return number % 10 + sum_calc(number // 10)


num = int(input('Введите целое натурально число: '))
max_sum = 0
max_num = 0
while num != 0:
    temp_num = num
    temp_sum = sum_calc(num)
    if temp_sum > max_sum:
        max_sum = temp_sum
        max_num = temp_num
    print('Для выхода из программы введите 0')
    num = int(input('Введите целое натуральное число: '))
print(f'Число {max_num} имеет максимальную сумму цифр: {max_sum}')