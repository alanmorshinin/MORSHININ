x = int(input("Введите количество мальчиков: "))
y = int(input("Введите количество девочек: "))

if x > (y + 1):
    print("Ответ: Нет решения")
else:
    result = ""
    for _ in range(min(x, y)):
        result += "BG"
        x -= 1
        y -= 1
    result += "G" * y
    result += "B" * x
    print("Ответ:", result)
