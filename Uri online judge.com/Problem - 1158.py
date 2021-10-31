for _ in range(int(input())):
    x, y = list(map(int,input().split()))
    s = 0
    while y:
        if x%2 != 0:
            s += x
            x += 1
            y -= 1
        else:
            x += 1
    print(s)
