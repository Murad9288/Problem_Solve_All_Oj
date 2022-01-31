import math
for _ in range(int(input())):
    mod = 10**9 + 7
    n,m = list(map(int,input().split()))
    m -= 1
    res = math.factorial(n+m)%mod
    a = math.factorial(n)*math.factorial(m)
    b = pow(a,mod-2,mod)
    print((res*b)%mod)
