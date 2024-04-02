from random import randint


def f(n):
    if n == 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
        return True


n = int(input('Введите кол-во элементов:\n'))
a = [randint(0, 100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in a)}')
s = sum(i for i in a if f(i))
k = sum(1 for i in a if f(i))
print(s / k)
