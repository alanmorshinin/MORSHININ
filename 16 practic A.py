def sort_array(arr):
    n = len(arr)
    if n % 2 == 0:
        first_half = sorted(arr[:n//2])
        second_half = sorted(arr[n//2:], reverse=True)
        return first_half + second_half
    else:
        raise ValueError("Массив должен содержать четное количество элементов")

print(sort_array([5, 3, 4, 2, 1, 6, 3, 2]))
print(sort_array([1, 2, 3, 4, 5, 6]))
