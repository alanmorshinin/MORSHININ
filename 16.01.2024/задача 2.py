nums = input("Введите три числа: ").split()
nums = [int(num) for num in nums]
count = 0
if nums[0] == nums[1] == nums[2]:
    count = 3
elif nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
    count = 2

if count == 0:
    print("Нет одинаковых чисел.")
elif count == 3:
    print("Все числа одинаковые.")
else:
    print("Два числа одинаковые.")