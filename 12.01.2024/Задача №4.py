from random import *
print('Введите три целых числа:')
a, b,c = [int(i) for i in input().split()]
if a > b and a>c:
    m = a
if b > c and b > c:
    m = b
if c > a and c > b:
    m = c
print(f'Максимальное число {m}')
