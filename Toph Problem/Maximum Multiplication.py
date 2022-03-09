a,b,c = map(int,input().split())
mx = max(a,b)
mn = min(a,b)
s = mx-mn
if c>=s:
    mn = mx
    c -= s
else:
    mn += c
    c = 0
r = c//2
mx += r
mn += r
c -= r*2
if c:
    mx += 1
print(mx*mn)
