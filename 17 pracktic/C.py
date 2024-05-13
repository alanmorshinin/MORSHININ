s = input('Введите строку\n')
f = False
count = 0
for i in range(len(s)):
    if max(s[i]):
        count += 1
        f = True
    elif s[i] == " ":
        f = False
        print(count)