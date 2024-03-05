import sys

sys.setrecursionlimit(2300)


def F(n):
    return G(n - 1)


def G(n):
    if n < 10:
        return n
    if n >= 10:
        return G(n - 2) + 1


a = 0
for i in range(1, 101):
    for j in range(1, 11):
        if F(i) == j ** 2:
            a += 1

print(a)
