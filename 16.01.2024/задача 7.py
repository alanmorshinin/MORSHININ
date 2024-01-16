hours = int(input("Введите отработанные часы: "))
clothes_expenses = int(input("Введите траты на одежду: "))
food_expenses = int(input("Введите траты на еду: "))
salary = (250 * hours) / 2 ** 3 + hours
total_expenses = clothes_expenses + food_expenses
if salary >= total_expenses:
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")