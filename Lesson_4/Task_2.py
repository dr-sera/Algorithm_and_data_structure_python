'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''
import math
import timeit
import cProfile
# Вариант с решетом Эратосфена


def erato_sieve(elem):
    result = []
    size = 10000
    sieve = [i for i in range(size)]
    sieve[1] = 0
    for i in range(2, size):
        if sieve[i] != 0:
            j = i + i
            while j < size:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    # print(f'Ваш список решета Эратосфена: {result}')
    # for i in range(len(result)):
    #     if i == elem:
    #         print(f'Интересующее Вас простое число: {result[i]}.')
    return result


# n = int(input('Введите размер решета: '))
# a = int(input('Введите интересующее Вас по счету число: '))
# erato_sieve(a)
print(timeit.timeit('erato_sieve(10)', number=100, globals=globals()))       # 0.415309
print(timeit.timeit('erato_sieve(30)', number=100, globals=globals()))       # 0.4127388
print(timeit.timeit('erato_sieve(60)', number=100, globals=globals()))       # 0.40911050000000015
print(timeit.timeit('erato_sieve(90)', number=100, globals=globals()))       # 0.4049442999999999
print(timeit.timeit('erato_sieve(100)', number=100, globals=globals()))      # 0.40131950000000005

# Делаю вывод что в алгоритм является линейным (почему является линейным я прекрасно понимаю. Видимо я тупой, раз не
# смог придумать как модифицировать... T_T

cProfile.run('erato_sieve(50)')     # 1    0.003    0.003    0.004    0.004 Task_2.py:13(erato_sieve)


def primes(size):
    sieve = set(range(2, size))
    for i in range(2, int(math.sqrt(size))):
        if i in sieve:
            sieve -= set(range(2 * i, size, i))
    return sieve


def calc(mas, elem):
    res = int
    for i in range(len(mas)):
        if i == elem:
            print(f'Интересующее Вас простое число: {mas[i]}.')
            res = mas[i]
    return res


a = int(input('Введите максимальное значение диапазона: '))
b = int(input('Введите номер интересующего Вас элемента: '))
calc(primes(a), b)

# Не идет у меня второе задание. Ставьте минус по нему.
