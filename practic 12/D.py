from random import randint
n = int(input('Введите n: \n'))
print('Массив: ')
c = []
while len(c) < n:
    a = randint(1, n)
    if a not in c:
        c.append(a)
print(' '.join(str(i) for i in c))
