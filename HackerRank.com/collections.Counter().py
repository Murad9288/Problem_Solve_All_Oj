from collections import Counter
n = int(input())
s = Counter(map(int,input().split()))
x = int(input())
res = []
for i in range(x):
    a,b = map(int,input().split())
    if s[a] > 0:
        res.append(b)
        s.subtract(Counter([a]))
    else:
        pass

print (sum(res))
