from fractions import gcd
n = int(input())
c = []
for i in range(1,n+1):
    if gcd(n,i) == 1:
        c.append(i)
print(len(set(c)))
