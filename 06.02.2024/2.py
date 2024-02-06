def alan(n):
    b = []
    if n < 0:
        n = -n
    while n > 0:
        d = n % 10
        b.append(d)
        n = n // 10
    b.reverse()
    for d in b:
        print(d)
n = int(input())
alan(n)