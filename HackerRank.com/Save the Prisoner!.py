for _ in range(int(input())):
    n,m,s = map(int,input().split())
    print((((s-1)+(m-1))%n)+1)
