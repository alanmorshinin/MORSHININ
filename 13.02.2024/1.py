def f(n):
    s = sum(int(i) for i in str(n))
    return s


n = int(input())
print(f'Сумма цифр числа {n} равна {f(n)}')
