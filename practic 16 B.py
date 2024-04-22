def sort_array_and_find_unique(arr):
    sorted_arr = sorted(arr)
    unique_arr = []
    for i in range(len(sorted_arr)):
        if i == 0 or sorted_arr[i] != sorted_arr[i-1]:
            unique_arr.append(sorted_arr[i])
    return sorted_arr, len(unique_arr)

print(sort_array_and_find_unique([5, 3, 4, 2, 1, 6, 3, 2, 4]))
