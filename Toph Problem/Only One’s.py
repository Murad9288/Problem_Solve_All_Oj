a,b = map(int,input().split())
s = len(str(a))+1
for i in range(2,s+1):
    print(i,end="")
for j in range(s-1,1,-1):
    print(j,end="")
print()
