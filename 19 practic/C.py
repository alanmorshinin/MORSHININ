def alan(s):
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    prev_value = 0

    for char in s:
        value = roman_numerals.get(char, 0)
        result += value
        if value > prev_value:
            result -= 2 * prev_value
        prev_value = value

    return result

string = input("Enter a string: ")
result = alan(string)
print("Result:")
print(result)
