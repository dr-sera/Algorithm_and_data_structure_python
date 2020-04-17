'''
Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в
этих позициях первого массива стоят четные числа.
'''
import random
import timeit
import cProfile


def fill_array(size):
    array = [random.randint(-100, 100) for i in range(size)]
    result = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result.append(i)
    return array, result


def fill_array_2(a):
    mas = []
    result = []
    for i in range(a):
        num = random.randint(-100, 100)
        mas.append(num)
        num = int(num)
        if num % 2 == 0:
            result.append(i)
        i += 1
    return mas, result


def fill(size):
    array = [random.randint(-100, 100) for i in range(size)]
    return array


def chk(mas):
    result = []
    for i in range(len(mas)):
        if mas[i] % 2 == 0:
            result.append(i)
    return result


def out(mas_1, mas_2):
    return mas_1, mas_2


def main(size):
    a = fill(size)
    b = chk(a)
    out(a, b)


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100

print('Первый вариант')
print(timeit.timeit('fill_array(10)', number=100, globals=globals()))       # 0.0013529000000000006
print(timeit.timeit('fill_array(50)', number=100, globals=globals()))       # 0.0066388
print(timeit.timeit('fill_array(100)', number=100, globals=globals()))      # 0.013160199999999997
print(timeit.timeit('fill_array(150)', number=100, globals=globals()))      # 0.018803900000000005
print(timeit.timeit('fill_array(200)', number=100, globals=globals()))      # 0.02443060000000001
print(timeit.timeit('fill_array(250)', number=100, globals=globals()))      # 0.030660999999999994
print(timeit.timeit('fill_array(300)', number=100, globals=globals()))      # 0.036439500000000014
print(timeit.timeit('fill_array(350)', number=100, globals=globals()))      # 0.0442999
print(timeit.timeit('fill_array(400)', number=100, globals=globals()))      # 0.04823559999999999
print(timeit.timeit('fill_array(450)', number=100, globals=globals()))      # 0.054059199999999974

'''На основании данных полученных могу сделать вывод, что данная функция является линейно зависимой'''
cProfile.run('fill_array(10)')      # 12    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

print('=' * 50)
print('Второй ариант')
print(timeit.timeit('fill_array_2(10)', number=100, globals=globals()))       # 0.0015863999999999982
print(timeit.timeit('fill_array_2(50)', number=100, globals=globals()))       # 0.007761399999999998
print(timeit.timeit('fill_array_2(100)', number=100, globals=globals()))      # 0.015995099999999998
print(timeit.timeit('fill_array_2(150)', number=100, globals=globals()))      # 0.023562100000000002
print(timeit.timeit('fill_array_2(200)', number=100, globals=globals()))      # 0.032803399999999996
print(timeit.timeit('fill_array_2(250)', number=100, globals=globals()))      # 0.03788180000000001
print(timeit.timeit('fill_array_2(300)', number=100, globals=globals()))      # 0.04537629999999998
print(timeit.timeit('fill_array_2(350)', number=100, globals=globals()))      # 0.052844400000000014
print(timeit.timeit('fill_array_2(400)', number=100, globals=globals()))      # 0.06078720000000001
print(timeit.timeit('fill_array_2(450)', number=100, globals=globals()))      # 0.06838459999999996

'''На основании данных полученных могу сделать вывод, что данная функция является линейно зависимой'''
cProfile.run('fill_array_2(10)')    # 15    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

print('=' * 50)
print('Третий вариант')
print(timeit.timeit('main(10)', number=100, globals=globals()))     # 0.0014259000000000008
print(timeit.timeit('main(50)', number=100, globals=globals()))     # 0.006111999999999999
print(timeit.timeit('main(100)', number=100, globals=globals()))    # 0.0126578
print(timeit.timeit('main(150)', number=100, globals=globals()))    # 0.0182731
print(timeit.timeit('main(200)', number=100, globals=globals()))    # 0.024901700000000006
print(timeit.timeit('main(250)', number=100, globals=globals()))    # 0.03012849999999999
print(timeit.timeit('main(300)', number=100, globals=globals()))    # 0.03677420000000001
print(timeit.timeit('main(350)', number=100, globals=globals()))    # 0.0421715
print(timeit.timeit('main(400)', number=100, globals=globals()))    # 0.04830219999999999
print(timeit.timeit('main(450)', number=100, globals=globals()))    # 0.053893599999999986

'''На основании данных полученных могу сделать вывод, что данная функция является линейно зависимой'''
cProfile.run('main(10)')        # 11    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}

