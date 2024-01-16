def check_apartment(cost, area):
    if area >= 100 and cost <= 10000000:
        return "Квартира подходит"
    elif area >= 80 and cost <= 7000000:
        return "Квартира подходит"
    else:
        return "Квартира не подходит"
cost = float(input("Введите стоимость квартиры: "))
area = float(input("Введите площадь квартиры: "))
result = check_apartment(cost, area)
print(result)