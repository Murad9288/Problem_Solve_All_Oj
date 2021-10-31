while True:
    n = int(input())
    c = 5
    s = 0
    if n==0:
        break
    else:
        while (c>0):
            if n%2 == 0:
                s += n
                n += 1
                c -= 1
            else:
                n += 1
    print(s)
