d = 0
s = 0
x = 1
for i in range(1, 101):
    k = 1/i
    d = d+ x + k + (-1) ** (i - 1)
    s = s + x + k
    x = k
print('нат каком растоянии от дома будеьт находиться мужчина после 100 этапа', d)
print('какоц общий путь н при этом пройдет', s)