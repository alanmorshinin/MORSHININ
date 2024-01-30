a = 185
b = 0
for i in range(a//15):
    for j in range(a // 17):
        for k in range(a // 21):
            if (i * 15 + j *17 + k * 21) > 185:
                break
            elif (i * 15 + j * 17 + k * 21) == 185:
                b += 1
print(b)