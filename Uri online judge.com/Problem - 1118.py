while True:
    s = 0
    c = 0
    while (c < 2):
        n = float(input())
        if n >= 0 and n <= 10:
            s += n
            c += 1
        else:
            print("nota invalida")
    print("media = %.2f" % (s / 2))
    t = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        t = int(input())
        if t == 1 or  t== 2:
            break
    if t == 2:
        break
