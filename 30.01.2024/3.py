N = int(input("Введите N: "))
result = []
for i in range(1, N+1):
    if all(int(digit) != 0 and i % int(digit) == 0 for digit in str(i)):
        result.append(i)

print(*result)
