a = int(input())
b = ''
result = 0
for i in range(1, a + 1):
    b += str(i)
    result += 1
    if len(b) == a:
        break
print(result)
