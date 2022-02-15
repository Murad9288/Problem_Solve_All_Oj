for _ in range(int(input())):
    n = str(input())
    s = "0123456789"
    c = 0
    for i in range(len(n)):
        if n[i] in  s:
            c += 1
    print(c)
