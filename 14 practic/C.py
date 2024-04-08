import random

arr = [random.randint(0, 10) for _ in range(10)]

seen = set()
duplicates = set(x for x in arr if x in seen or seen.add(x))

if duplicates:
    print('Массив:', arr)
    print('Есть:', duplicates)
else:
    print('Массив:', arr)
    print('Нет повторяющихся элементов')
