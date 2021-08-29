# Not Accepted:

T = int(input())
for t in range(T):
    n, m = map(int,input().split())
    for i in range(0, n-1):
        for i in range(0,i+1):
            print(m,end=' ')
        print()
    for i in range(n,0 ,-1):
        for j in range(0,i):
            print(m,end=' ')
        print()

# Second rules: But not Accepted:
'''
T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    for i in range(n):
        print("%d "%m*(i+1))
    for i in range(n-1):
        print("%d "%m*(n-i-1))
    if t<T-1:
        print()
'''
