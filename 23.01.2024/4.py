a = int(input('a = '))
b = int(input('b = '))
if b <= a:
    print('значение b должно быть больше чем a')
else:
    sum = 0
    for i in range(a, b + 1):
        sum += i
    print(f'сумма всех чисел от {a} до {b} = {sum}')