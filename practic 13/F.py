def c(h):
    n = sum(i > 170 for i in h)
    return n

def b(n):
    return n >= 5

def m():
    s = int(input("Введите количество учеников: "))
    h = []
    for i in range(s):
        ht = int(input(f"Введите рост ученика {i+1} в см: "))
        h.append(ht)

    nt = c(h)
    t = b(nt)

    print(f"Из {s} учеников, {nt} имеют рост больше 170 см.")

    if t:
        print("Можно сформировать команду.")
    else:
        print("Нельзя сформировать команду, так как учеников с ростом выше 170 см не хватает.")

if __name__ == "__main__":
    m()
