num = int(input("Введите четырёхзначное число: "))

thousands = num // 1000
hundreds = (num // 100) % 10
tens = (num // 10) % 10
units = num % 10

print("Первая цифра:", thousands)
print("Вторая цифра:", hundreds)
print("Третья цифра:", tens)
print("Четвёртая цифра:", units)