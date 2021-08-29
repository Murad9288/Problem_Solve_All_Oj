T = int(input())
for t in range(T):
    a,b,c = map(int,input().split())
    for i in range(1,c+1):
        if i%a == 0 and i%b == 0:
            print(i)
    if t<T-1:
        print()
