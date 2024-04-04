def c(w):
    f = [i for i in w if i > 100]
    r = [i for i in w if i <= 100]

    a_f = sum(f) / len(f)
    a_r = sum(r) / len(r)

    return a_f, a_r

def m():

    w = []
    for i in range(25):
        wi = float(input(f"Введите массу {i+1}-го человека: "))
        w.append(wi)

    x, y = c(w)

    print(f"Средняя масса полных людей: {x:.2f} кг")
    print(f"Средняя масса остальных людей: {y:.2f} кг")

if __name__ == "__main__":
    m()
