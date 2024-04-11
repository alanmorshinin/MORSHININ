def calkulat(a):
    sumapozitiv = sum(i for i in a if i > 0)
    sumanegativ = sum(abs(i) for i in a if i < 0)
    if sumanegativ == 0:
        return 'на 0 делить нельзя'
    b = sumapozitiv / sumanegativ
    return b
spiso4ek = [1, -2, 3, -4, 5]
resultat = calkulat((spiso4ek))
print(resultat)
#+3