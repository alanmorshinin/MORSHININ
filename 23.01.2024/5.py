n = int(input('введите целое число которое 0 < n < 27: '))
count = 0
if 0 < n < 27:
    for i in range(100, 1000):
        digits_sum = sum(map(int,str(i)))
        if digits_sum == n:
            count += 1
    print(f'количество трехзначных чисел с суммой цифр {n} = {count}')
else:
    print('число n должно быть больше 0 и меньше 27')