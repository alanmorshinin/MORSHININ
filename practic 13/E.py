def massiv_A(arr):
    result = 0
    s = 1
    for num in arr:
        result += s * num
        s *= -1
    return result

n = int(input('Введите количество элементов: '))


arr = []
print('Введите элементы массива: ')
for _ in range(n):
    arr.append(int(input()))

result = massiv_A(arr)

print('Знакопеременная сумма: ', result)
