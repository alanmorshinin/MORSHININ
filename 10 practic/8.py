def alan(n):
    if n == 1:
        return 1
    else:
        a = 0
        for i in range(1, n + 1):
            a += alan(n - i)
        return a
N = int(input('Введите натуральнео число: '))
print(f'Количество разложений: {alan(N)}')