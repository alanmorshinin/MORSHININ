a, b = map(int, input('Введите X и D: \n').split())
print('Массив: ')
c = []
for _ in range(5):
    c.append(a)
    a += b
print(' '.join(str(i) for i in c))