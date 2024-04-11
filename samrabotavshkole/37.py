from random import randint
n = int(input('Введите количество элементов: '))
A = [randint(0, 10) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in A)}')
s = []
b = []
for i in range(n):
    if i % 2 == 0:
        s.append(i)
    if i % 10 == 0:
        b.append(i)
print("чётные", *s)
print('элементы оканчивающиеся на 0'*и)

