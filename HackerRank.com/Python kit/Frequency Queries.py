queries = []
a = dict()

for _ in range(int(input().strip())):
    q = list(map(int,input().split()))
    if q[0] == 1:
        try:
            a[q[1]] += 1
        except:
            a[q[1]] = 1
    elif q[0] == 2:
        try:
            a[q[1]] -= 1
            if a[q[1]] == 0:
                del a[q[1]]
        except:
            continue
    elif q[0] == 3:
        if q[1] >= 10**6:
            print(0)
        elif q[1] in set (a.values()):
            print(1)
        else:
            print(0)
