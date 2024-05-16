def alan(string):
    while "12" in string or "322" in string or "222" in string:
        if "12" in string:
            string = string.replace("12", "2", 1)
        if "322" in string:
            string = string.replace("322", "21", 1)
        if "222" in string:
            string = string.replace("222", "3", 1)
    return string
n = int(input('введите количество цифр 2'))
input_string = "1" + "2" * n

result_string = alan(input_string)
print("Результат выполнения программы:", result_string)
print("Наибольшее возможное количество цифр '2':", result_string.count("2"))
