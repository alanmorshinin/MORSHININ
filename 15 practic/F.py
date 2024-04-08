from random import randint

n = int(input('Введите количество элементов: '))
a = [randint(-100, 100) for _ in range(n)]
print(f'Массив A:\n{" ".join(str(i) for i in a)}')
element_poloshitilnie = [i for i in a if i > 0]
element_otrisatelnie = [i for i in a if i <= 0]
element_poloshitilnie.sort(reverse=True)
element_otrisatelnie.sort()
a = element_poloshitilnie + element_poloshitilnie
print('Результат:')
print(*a)
print('Количество полоительных элементов:', len(element_poloshitilnie))
