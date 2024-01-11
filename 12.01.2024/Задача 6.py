a = int(input('Возраст Антона: '))
b = int(input('Возраст Бориса: '))
c = int(input('Возраст Виктора: '))
if a > b and a > c:
    m = 'Антон страше всех'
if b > c and b > c:
    m = 'Борис страше всех'
if c > a and c > b:
    m = 'Виктор страше всех'
print(f'{m}')
a = int(input('Возраст Антона: '))
b = int(input('Возраст Бориса: '))
c = int(input('Возраст Виктора: '))
if a > b and b > c:
    n = 'Антон и Борис старше Виктора'
if b > c and c > a:
    n = 'Борис и Виктор страше Антона'
if c > a and a > b:
    n = 'Виктор и Антон страше Бориса'
print(f'{n}')