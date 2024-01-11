from random import *
a = randint(1, 6)
b = randint(1, 6)
c = randint(1, 6)
d = (a + b + c) // 3
print(f'Выпало очков:\n{a} {b} {c}')
print(f'({a}+{b}+{c})/3=',d)