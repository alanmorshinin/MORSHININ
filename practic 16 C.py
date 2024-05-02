import random

def binary_search(arr, x, start, end, count):
    if start > end:
        return count
    mid = (start + end) // 2
    if arr[mid] == x:
        return count + 1
    elif arr[mid] > x:
        return binary_search(arr, x, start, mid-1, count+1)
    else:
        return binary_search(arr, x, mid+1, end, count+1)

def fill_array_and_sort(n):
    arr = [random.randint(1, n) for _ in range(n)]
    arr.sort()
    return arr

n = int(input("Введите размер массива: "))
arr = fill_array_and_sort(n)
print("Массив:", arr)
x = int(input("Введите число X: "))
start = 0
end = n-1
count = 0
if binary_search(arr, x, start, end, count) == 0:
    print("Число", x, "не найдено.")
else:
    print("Число", x, "найдено.")
    print("Количество сравнений:", binary_search(arr, x, start, end, count))
