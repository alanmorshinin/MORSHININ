a = int(input('введите число отрезка: '))
b = int(input('введите число отрезка: '))
h = int(input('введите шаг:  '))
if h > 0:
    a, b = min(a, b), max(a, b) + 1
else:
    b, a = min(a, b) - 1, max(a, b)
for x in range(a, b, h):
    print(x)
