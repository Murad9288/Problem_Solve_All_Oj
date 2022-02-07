for _ in range(int(input())):
    n,m = list(map(int,input().split()))
    print((n // m) * (m * (m - 1) // 2) + (n % m * (n % m + 1) // 2))
