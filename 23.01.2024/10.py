x = int(input("Введите количество мальчиков: "))
y = int(input("Введите количество девочек: "))

if x < y or x > 2 * y + 1:
    print("Ответ: Нет решения")
else:
    result = ""
    for _ in range(min(x, y)):
        result += "BG"
        x -= 1
        y -= 1
    result += "B" * x
    result += "G" * y
    print("Ответ:", result)