def prime(number):
    if int(number * 0.5) == number * 0.5:
        return 'составное число'
    if number % 5 ==0 and number != 5:
        return 'сосатвное число'
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return 'составное число'
        return ('простое число')
for n in range(9900000, 12000000):
    print(prime(n))