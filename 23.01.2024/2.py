for i in range(153, 1000):
    a = (i // 100 % 10)**3
    b = (i // 10 % 10)**3
    c = (i % 10)**3
    if a + b + c == i:
        print(i)
