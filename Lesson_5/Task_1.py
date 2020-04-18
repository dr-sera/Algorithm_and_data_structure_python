'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import namedtuple

company = namedtuple('company', 'name, prft_qrt_1, prft_qrt_2, prft_qrt_3, prft_qrt_4, year')

quantity = int(input('Введите количество предприятий: '))
companys = [0 for i in range(quantity)]
income = 0

for i in range(quantity):
    name = input(f'Введите название {i+1} предприятия: ')
    qrts = [int(j) for j in input('Введите через запятую прибыль в каждом квартале: ').split(',')]
    year = 0
    for qrt in qrts:
        year += qrt
    income += year
    companys[i] = company(name, *qrts, year)
    # print(companys[i])

if quantity == 0:
    print('Предприятия по которым следует проводить подсчеты отсутствуют!')
elif quantity == 1:
    print(f'У Вас одно предприятие: {companys[0].name}. Его годовая прибыль составляет: {companys[0].year}')
else:
    average_income = income / quantity
    less = []
    more = []
    for i in range(quantity):
        if companys[i].year < average_income:
            less.append(companys[i])
        elif companys[i].year > average_income:
            more.append(companys[i])

print(f'Серднегодовая прибыль по всем предприятиям равна: {average_income}')

print(f'\nПредприятия, чья прибыль меньше среднегодовой: ')
for companys in less:
    print(f'{companys.name} прибыль составляет: {companys.year} ')

print(f'\nПредприятия, чья прибыль меньше среднегодовой: ')
for companys in more:
    print(f'{companys.name} прибыль составляет: {companys.year} ')
