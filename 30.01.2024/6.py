m = int(input('Ввидите число m: '))
n = int(input('Ввидите число n: '))


def alan(m, n):
    b = []
    for i in range(1, n):
        s = sum(int(j) for j in str(i))
        if s ** 2 == m:
            b.append(i)
        return b
r = alan(m, n)
print(r)
