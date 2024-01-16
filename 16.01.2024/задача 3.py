month_number = int(input("Введите номер месяца: "))
if month_number == 1 or month_number == 2 or month_number == 12:
    print("Зима.")
elif month_number == 3 or month_number == 4 or month_number == 5:
    print("Весна.")
elif month_number == 6 or month_number == 7 or month_number == 8:
    print("Лето.")
elif month_number == 9 or month_number == 10 or month_number == 11:
    print("Осень.")
else:
    print("Неверный номер месяца.")