age_of_Anton = int(input("Возраст Антона: "))
age_of_Boris = int(input("Возраст Бориса: "))
age_of_Victor = int(input("Возраст Виктора: "))
if age_of_Anton > age_of_Boris and age_of_Anton > age_of_Victor:
print("Антон старше всех.")
elif age_of_Boris > age_of_Anton and age_of_Boris > age_of_Victor:
print("Борис старше всех.")
elif age_of_Victor > age_of_Anton and age_of_Victor > age_of_Boris:
print("Виктор старше всех.")
elif age_of_Anton == age_of_Boris and age_of_Anton > age_of_Victor:
print("Антон и Борис старше Виктора.")
elif age_of_Anton == age_of_Victor and age_of_Anton > age_of_Boris:
print("Антон и Виктор старше Бориса.")
elif age_of_Boris == age_of_Victor and age_of_Boris > age_of_Anton:
print("Борис и Виктор старше Антона.")
else:
print("Антон, Борис и Виктор одного возраста.")