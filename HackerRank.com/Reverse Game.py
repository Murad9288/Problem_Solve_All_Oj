for _ in range(int(input())):
    n,k = map(int,input().split())
    print(min((n-1-k)*2, 2*k+1))
