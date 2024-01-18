a, b = [int(i) for i in input('Введите два целых числа:\n').split()]
if a < 0 or b < 0 or a >= b:
    print('Ошибка корректнее A и B (0 < A < B)')
else:
    i = a
    while i <= b:
        print(i ** 2)
        i += 1