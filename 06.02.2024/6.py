def line(s, t):
    k, b = map(float, s.split('x'))
    #print(f'{k:<5}{b:<5}')
    x, y = map(float, t.split(';'))
    #print(f'{x:<5}{y:<}')

    print(k * x + b == y)
line("1x+6", "1;7")