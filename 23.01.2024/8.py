n = int(input("Введите натуральное число n: "))
factorial = 1

if n < 0:
    print("Факториал не определен для отрицательных чисел")
elif n == 0:
    print("Факториал числа 0 равен 1")
else:
    for i in range(1, n + 1):
        factorial *= i
    print("Факториал числа", n, "равен", factorial)