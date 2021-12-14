for _ in range(int(input())):
    n = int(input().strip())
    m = []
    for _ in range(2*n):
        m.append(list(map(int, input().rstrip().split())))
    n = len(m)
    s = 0
    for i in range(n//2):
        for j in range(n//2):
            s += max(m[i][j], m[i][n-j-1], m[n-i-1][j], m[n-i-1][n-j-1])
    print(s)
