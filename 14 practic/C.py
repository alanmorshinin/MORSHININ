from random import randint

n = int(input('Введите количество элементов: '))
A = [randint(0, 5) for _ in range(n)]
print(f'Массив:\n {"".join(str(i) for i in A)} ')
S = []
for i in range(n - 1):
    if A[i] == A[i + 1]:
        if (A[i] in S):
            S.append(A[i])

if len(str(S)) < len(S):
    print('Есть', ",".join(str(i) for i in S))
else:
    print('Нет')


