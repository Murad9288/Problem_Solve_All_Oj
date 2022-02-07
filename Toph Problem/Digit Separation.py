try:
    while True:
        s = str(input())
        c = 0
        for i in s:
            if int(i) != 0:
                c += int(i)
        print(c)
except EOFError:
    pass
