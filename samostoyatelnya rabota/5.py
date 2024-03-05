def f(n):
    if n == 0:
        return 1
    if n > 0 and n % 2 != 0:
        return f(n // 100) * (n % 10)
    if n > 0 and n % 2 == 0:
        return f(n // 100)
a = 0
for i in range(1, 4):
    for j in range(10**9, i * 10**9):
        if f(i) == 21:
            a += 1
            print(f'при {j} = {a}')
print(a)

