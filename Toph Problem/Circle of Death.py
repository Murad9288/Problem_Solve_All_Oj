from math import factorial as f
for _ in range(int(input())):
    n,k = map(int,input().split())
    c = 0
    while(n != 0):
        c = c + (n % 2)
        n = n // 2
    if c > k:
        print(0)
    else:
        print((f(k)//f(c)//f(k-c))%(10**9+7))
