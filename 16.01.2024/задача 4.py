age = int(input("Введите возраст: "))
if age % 10 == 1 and age % 100 != 11:
    print("Вам", age, "год.")
elif age % 10 in [2, 3, 4] and age % 100 not in [12, 13, 14]:
    print("Вам", age, "года.")
else:
    print("Вам", age, "лет.")