for t in range(int(input())):
    n = int(input())
    c = 0
    while n>1:
        n //= 2
        c += 1
    print("Case %d: %d"%(t+1,c+1))
