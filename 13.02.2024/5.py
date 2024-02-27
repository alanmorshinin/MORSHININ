number1 = int(input('Введите натуральное число: '))
number2 = 0

for i in str(number1):
    a = number1 % 10
    number1 = number1 // 10
    number2 = number2 * 10
    number2 = number2 + a

print(f'После переворота: {number2}')
