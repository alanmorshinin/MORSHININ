n = int(input("Введите N: "))
print("Автоморфные числа, не превосходящие", n, ":")
for i in range(1, n + 1):
    square = i * i
    if str(square).endswith(str(i)):
        print(i, "*", i, "=", square)