'''
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции
вводятся пользователем. После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
'''

while True:
    print('Для выхода из программы введите 0.')
    sign = input('Введите знак +, -, *, /: ')
    if sign == '0':
        break
    if sign == '+' or sign == '-' or sign == '*' or sign == '/':
        x = float(input('Введите первое число: '))
        y = float(input('Введите второе число: '))
        if sign == '+':
            print(f'Сумма двух чисел равна: {x + y}')
        if sign == '-':
            print(f'Разность двух чисел равна: {x - y}')
        if sign == '*':
            print(f'Произведение двух чисел равно: {x * y}')
        if sign == '/':
            if y != 0:
                print(f'Частное двух чисел равно: {x / y}')
            else:
                print('На ноль делить нельзя!')
    else:
        print('Выбран неверный знак операции!')