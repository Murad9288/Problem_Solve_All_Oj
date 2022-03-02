t,x,y,z,m = map(int,input().split())
if ((x+y+z+m)//4)<=t:
    print("YES")
else:
    print("NO")
