def complexpow(a,b,k,m):
    if k == 1: 
        return a%m,b%m
    else:
        c,d = ((a*a)%m-(b*b)%m)%m,(2*a*b)%m
        x,y = complexpow(c,d,k//2,m)
        if k%2:
            e,f = (a*x-b*y)%m,(a*y+b*x)%m
            x,y = e,f
        return x,y

for _ in range(int(input())):
    print(*complexpow(*map(int,input().split())))
