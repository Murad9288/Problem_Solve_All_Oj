T = int(input())
for i in range(1,T+1):
        n =list(map(int,input().split()))
        n.sort()
        print("Case %d:"%i,*n)
