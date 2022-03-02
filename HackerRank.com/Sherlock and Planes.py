for _ in range(int(input())):
    a,b,c = map(int,input().split())
    d,e,f = map(int,input().split())
    g,h,i = map(int,input().split())
    x,y,z = map(int,input().split())
    if (x==a==d==g) or (y==b==e==h) or (z==c==f==i):
        print("YES")
    else:
        print("NO")
