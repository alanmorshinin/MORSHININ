from random import *
print('Введите три целых числа:')
a, b, c, d, e = [int(i) for i in input().split()]
if a > b and a > c and a > d and a > e:
    m = a
if b > c and b > c and b > d and b > e:
    m = b
if c > a and c > b and c > d and c > e:
    m = c
if d > a and d > b and d > c and d > e:
    m = d
if e > a and e > b and e > c and e > d:
    m = e
print(f'Максимальное число {m}')