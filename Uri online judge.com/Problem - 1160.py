for _ in range(int(input())):
    li = input().split()
    a = int(li[0])
    b = int(li[1])
    g_1 = float(li[2])
    g_2 = float(li[3])
    y = 0
    while a<=b:
        ca = int(a*(g_1/100))
        cb = int(b*(g_2/100))
        y += 1
        a += ca
        b += cb
        if y>100:
            break
    if (y > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos."%y)
