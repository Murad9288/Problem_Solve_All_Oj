for t in range(int(input())):
    n = int(input())
    print("Case %d:"%(t+1),max(list(map(abs,map(int,input().split())))))
