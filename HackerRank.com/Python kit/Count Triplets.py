from collections import Counter

n,r = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
a = Counter(arr)
b = Counter()
count = 0
for i in arr:
    j = i//r
    k = i*r
    a[i]-=1
    if b[j] and a[k] and not i%r:
        count+=b[j]*a[k]
    b[i]+=1
print(count)
