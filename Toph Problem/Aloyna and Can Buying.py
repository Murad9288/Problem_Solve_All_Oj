n, k = map(int,input().split())
p = list(map(int,input().split()))
print(max(set(p),key=p.count))
