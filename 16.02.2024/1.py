def tr(a, b, c):
    return a + b > c and a + c > b and c + b > a


a, b, c = map(float, input('Введите ст. тр.\n').split())
if tr(a, b, c):
    print('Тр. существует')
else:
    print('Тр. не существует')