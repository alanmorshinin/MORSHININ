from random import randint
n = int(input('Введите кол-во элементов:\n'))
a = [randint(2, 100) for _ in range(n)]
print(f'Массив:\n{" ".join(str(i) for i in a)}')
s1 = sum(i for i in a if i < 170)
count1 = sum(1 for i in a if i < 170)
s2 = sum(i for i in a if i >= 170)
count2 = sum(1 for i in a if i >= 170)
sr1 = None if count1 == 0 else s1 / count1
sr2 = None if count2 == 0 else s2 / count2
print(f'среднее арфиметическое элементов [0,170]: {sr1}')
print(f'среднее арфиметическое элементов [170,230]: {sr2}')