arr = list(map(int, input('Введите массив чисел через пробел: ').split()))

max_value = max(arr)

count_max = arr.count(max_value)

print('Массив:', arr)
print(f'Максимальное значение: {max_value}')
print(f'Количество элементов: {count_max}')
