def line(s, t):
    k, b = map(float, s.split())
    print(f'{k:<5}{b:<5}')
    x, y = map(float, t.split())
    print(f'{x:<5}{y:<}')
    if k * x + b == y:
        print('True')
    else:
        print('False')
line("1x+6", "1;7")