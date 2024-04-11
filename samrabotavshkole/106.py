def maasiv4ik(a):
    maxmass = 0
    cur = 0
    for i in a:
        if i % 2 != 0:
            cur += 1
            maxmass = max(maxmass, cur)
        else:
            cur = 0
    return maxmass


a = [2, 5, 6, 7, 9, 11, 8, 10, 13]
resuktat = maasiv4ik(a)
print(f'длина наибольшего отрезка нечсетных чисел в массиве: {resuktat}')
