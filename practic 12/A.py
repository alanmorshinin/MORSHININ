from random import randint
a, b = map(int, input('Введите границы диапазона: '))
print('Массив: ')
c = [randint(a, b) for i in range(5)]
print(' '.join(str(i) for i in c))