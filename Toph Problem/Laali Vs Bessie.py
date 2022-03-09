n,m = map(int,input().split())
x = int(m**0.5)
solve = False
for i in range(2,x+1):
    if m%i == 0 and n>=i:
        m //= i
        n -= i
    if m%i == 0:
        solve = True
        break
if m>1 and n>=m and solve == False:
    n -= m
    m //= m
print(n,m)
