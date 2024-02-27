def alan(n):
    summ = 0
    while n:
        summ += n % 10
        n //= 10
    return summ
 
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
 
print(('b больше', 'a больше')[alan(a) > alan(b)])
