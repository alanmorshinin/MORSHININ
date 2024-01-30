a = 10
b = 5
c = 0.5
for i in range(11):
    for j in range(21):
        for k in range(201):
            kolr = i*a + j*b + k*c
            kolg = i + j + k
            if (kolr == 100) and kolg == 100:
                print(f'быков {i} коров {j} телят {k} остаток {100-kolr} руб')
