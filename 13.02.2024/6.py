def alan(a, b):
    if (b == 0):
        return a
    else:
        return alan(b, a % b)
a, b = map(int, input('Введите два натуральных числа: \n').split())
summ = alan(a, b)
print(f'НОД({a},{b}) = {summ}'.)
