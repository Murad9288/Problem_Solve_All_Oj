T = int(input())
for i in range(1,T+1):
    N = int(input())
    li = list(map(int,input().split())) [:N]
    r = sum(li)
    if r%2 == 0:
        print("K-%d"%r)
    else:
        print("K-%d"%(r+T))
