n = int(input("Введите натуральное число n: "))
p = int(input("Введите целое число p: "))

sum_bi = 0
for i in range(n):
    bi = int(input(f"Введите число b{i+1}: "))
    sum_bi += bi

if sum_bi < p:
    print("Сумма чисел bi меньше p")
else:
    print("Сумма чисел bi не меньше p")