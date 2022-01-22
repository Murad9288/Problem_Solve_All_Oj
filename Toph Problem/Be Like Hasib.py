n,x = map(int,input().split())
c = 0
l = 1
h = n
mid = 0
while h-l>=1:
    c += 1
    mid = (h+l)//2
    if mid < x:
        l = mid+1
    else:
        h = mid
print(c)
