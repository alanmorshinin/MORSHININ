def check_apartment(a, b):
    if b >= 100 and a <= 10000000:
        return "Квартира подходит"
    elif b >= 80 and a <= 7000000:
        return "Квартира подходит"
    else:
        return "Квартира не подходит"
a = float(input("Введите стоимость квартиры: "))
b = float(input("Введите площадь квартиры: "))
result = check_apartment(a, b)
print(result)