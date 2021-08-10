for _ in range(int(input())):
    n = float(input())
    li = []
    while n > 1:
        n /= 2
        li.append(n)
    print("%s days"%(len(li)))
