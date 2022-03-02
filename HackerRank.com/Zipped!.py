n,x = map(int,input().split())
arr = []
for i in range(x):
    arr.append(list(map(float,input().split()))[:n])
for j in zip(*arr):
    print(sum(j)/x)
