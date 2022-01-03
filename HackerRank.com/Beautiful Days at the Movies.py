n,m,k = map(int,input().split())
count = 0
for i in range(n,m+1):
    if (i - int(str(i)[::-1])) % k == 0:
        count += 1
print(count)
