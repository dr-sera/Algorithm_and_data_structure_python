'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from collections import deque, defaultdict


def conversion(num_1, num_2):
    if len(num_1) < len(num_2):
        while len(num_1) < len(num_2):
            num_1.appendleft('0')
    elif len(num_1) > len(num_2):
        while len(num_2) < len(num_1):
            num_2.appendleft('0')
    num_1.reverse()
    num_2.reverse()
    tmp_num1 = 0
    tmp_num2 = 0
    for index, value in enumerate(num_1):
        num_1[index] = example[value]
    for _ in range(len(num_1)):
        tmp_num_1 = num_1[_] * 16**_
        tmp_num1 += tmp_num_1

    for index, value in enumerate(num_2):
        num_2[index] = example[value]
    for _ in range(len(num_2)):
        tmp_num_2 = num_2[_] * 16**_
        tmp_num2 += tmp_num_2
    return tmp_num1, tmp_num2


def addition(num_1, num_2):
    result_add = []
    res_add = num_1 + num_2
    while res_add > 0:
        tmp_res = res_add % 16
        res_add //= 16
        result_add.append(tmp_res)
    result_add.reverse()
    for index, value in enumerate(result_add):
        result_add[index] = rev_example[value]
    return print(f'Результат сложения равен: {result_add}')


def multiple(num_1, num_2):
    result_mult = []
    res_mult = num_1 * num_2
    while res_mult > 0:
        tmp_res = res_mult % 16
        res_mult //= 16
        result_mult.append(tmp_res)
    result_mult.reverse()
    for index, value in enumerate(result_mult):
        result_mult[index] = rev_example[value]
    return print(f'Результат умножения равен: {result_mult}')


def main(num1, num2):
    f_num, s_num = conversion(num1, num2)
    addition(f_num, s_num)
    multiple(f_num, s_num)


example = defaultdict(list,
                      {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                       '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
                      )

rev_example = defaultdict(list,
                          {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                           8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
                          )

a = input('Введите первое чилсло в шестнадцатиричной системе: ')
b = input('Введите второе чилсло в шестандцатиричной системе: ')
first = deque(a)
second = deque(b)
# print(first, second)
main(first, second)
