def element(a):
    naiti = [i for i, elementic in enumerate(a) if str(elementic)[-1] == '0']
    return naiti

spiso4ek = [10, 20, 30, 45, 47, 50]
resultat = element(spiso4ek)
print('индексы элементов оканчи на 0', resultat)
#3