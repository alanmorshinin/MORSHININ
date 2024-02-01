s = int(input("Введите площадь прямоугольника s: "))
sovpadaysie_b = []
raznimi_a = []

for a in range(1, int(s**0.5) + 1):
    if s % a == 0:
        b = s // a
        raznimi_a.append((a, b))
        if a <= b:
            sovpadaysie_b.append((a, b))

print(f'Размеры прямоугольников с площадью {s} с учетом разных перестановок: {raznimi_a}')
print(f'Размеры прямоугольников с площадью {s} без учета разных перестановок: {sovpadaysie_b}')
