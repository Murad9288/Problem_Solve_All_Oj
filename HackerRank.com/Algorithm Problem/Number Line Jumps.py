a,c,b,d = map(int,input().split())
if c > d and (b-a) % (d-c) == 0:
    print("Yes")
else:
    print("No")
