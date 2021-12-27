for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in str(n):
        if int(i) != 0 and n%int(i) == 0:
            c += 1
    print(c)
