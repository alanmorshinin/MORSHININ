from random import randint

a = [randint(0, 10) for _ in range(10)]
print(*a)
print(*a[(len(a) // 2) - 1:: -1], end=" ")
print(*a[:(len(a) // 2) - 1: -1])
