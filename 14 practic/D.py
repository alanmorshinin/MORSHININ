import random

arr = [random.randint(0, 100) for _ in range(10)]

min_element = min(arr)
max_element = max(arr)

min_index = arr.index(min_element)
max_index = arr.index(max_element)

print("Массив:", arr)
print(f'Минимальный элемент: A[{min_index}]={min_element}')
print(f'Максимальный элемент: A[{max_index}]={max_element}')
