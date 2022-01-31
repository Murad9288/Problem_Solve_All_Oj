for _ in range(int(input())):
    m,n = map(int,input().split())
    s = []
    for i in range(n):
        s.append(str(input()))
    print((len(set(s)))-m)
