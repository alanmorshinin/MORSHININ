n = int(input("Введите число N:\n"))
while n < 0:
    print("Число N должно быть натуральным!")
    n = int(input("Введите число N: "))
sum = 0
a, b = 1, 1
while a < n:
    sum += a
    a, b = b, a + b

print("Сумма:", sum)